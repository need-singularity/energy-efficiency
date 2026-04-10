"""
HEXA-SENSE: BCI 뉴로피드백 4D 지각 시스템
OpenBCI Cyton+Daisy 16ch → 두정엽 공간처리 모니터링 → 4D 과제 피드백

필수: pip install brainflow numpy websockets
선택: pip install sounddevice (4D 공간 청각)
"""

import argparse
import asyncio
import json
import time
import numpy as np
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds
from brainflow.data_filter import DataFilter, FilterTypes, WindowOperations

# ── n=6 상수 ──
N = 6
PHI = 2
TAU = 4
SIGMA = 12
SOPFR = 5
J2 = 24

# ── 채널 매핑 (10-20 시스템, OpenBCI 16ch) ──
# 16 = phi^tau = 2^4 = Tesseract 꼭짓점
CHANNELS = {
    # 두정엽 (tau=4ch) — 공간 처리 핵심
    "parietal": {"P3": 0, "P4": 1, "P7": 2, "P8": 3},
    # 후두엽 (phi=2ch) — 시각 기저선
    "occipital": {"O1": 4, "O2": 5},
    # 전두엽 (tau=4ch) — 주의력/작업기억
    "frontal": {"F3": 6, "F4": 7, "F7": 8, "F8": 9},
    # 측두엽 (phi=2ch) — 청각 공간
    "temporal": {"T7": 10, "T8": 11},
    # 중심부 (tau=4ch) — 운동/판단
    "central": {"C3": 12, "C4": 13, "Fp1": 14, "Fp2": 15},
}

# ── 주파수 밴드 (n=6 산술) ──
BANDS = {
    "delta":  (1, TAU),            # 1-4 Hz
    "theta":  (TAU, SIGMA - TAU),  # 4-8 Hz
    "alpha":  (SIGMA - TAU, SIGMA),# 8-12 Hz
    "beta":   (SIGMA, SIGMA + J2), # 12-36 Hz (집중, 공간)
}


class HexaSense:
    """BCI 뉴로피드백 4D 지각 훈련 시스템"""

    def __init__(self, serial_port=None, synthetic=False):
        self.params = BrainFlowInputParams()
        if synthetic:
            self.board_id = BoardIds.SYNTHETIC_BOARD
        else:
            self.board_id = BoardIds.CYTON_DAISY_BOARD
            if serial_port:
                self.params.serial_port = serial_port

        self.board = None
        self.sampling_rate = 0
        self.eeg_channels = []

        # 뉴로피드백 상태
        self.baseline_alpha = None  # 캘리브레이션 기저선
        self.spatial_activation = 0.0  # 두정엽 공간 활성도 (0~1)
        self.feedback_score = 0  # 누적 피드백 점수
        self.trial_count = 0
        self.correct_count = 0

        # w축 상태
        self.current_w = 0.0  # 현재 4D 과제의 w좌표

        # 웹소켓 클라이언트 목록
        self.ws_clients = set()

    def start(self):
        """보드 시작"""
        BoardShim.enable_dev_board_logger()
        self.board = BoardShim(self.board_id, self.params)
        self.board.prepare_session()
        self.board.start_stream()
        self.sampling_rate = BoardShim.get_sampling_rate(self.board_id)
        self.eeg_channels = BoardShim.get_eeg_channels(self.board_id)
        ch_count = len(self.eeg_channels)
        print(f"[HEXA-SENSE] 보드 시작: {ch_count}ch, {self.sampling_rate}Hz")
        print(f"[HEXA-SENSE] {ch_count} = phi^tau = {PHI}^{TAU} = Tesseract 꼭짓점")

    def stop(self):
        """보드 정지"""
        if self.board:
            self.board.stop_stream()
            self.board.release_session()
            print("[HEXA-SENSE] 보드 정지")

    def get_band_power(self, data, ch_idx, band_name):
        """특정 채널의 주파수 밴드 파워 계산"""
        if ch_idx >= len(self.eeg_channels):
            return 0.0
        ch = self.eeg_channels[ch_idx]
        signal = data[ch]
        if len(signal) < self.sampling_rate:
            return 0.0

        # 밴드패스 필터
        low, high = BANDS[band_name]
        DataFilter.perform_bandpass(
            signal, self.sampling_rate,
            (low + high) / 2, high - low,
            4, FilterTypes.BUTTERWORTH, 0
        )
        # PSD 계산
        psd = DataFilter.get_psd_welch(
            signal, 256,
            256 // 2,
            self.sampling_rate,
            WindowOperations.HANNING
        )
        # 밴드 파워
        bp = DataFilter.get_band_power(psd, low, high)
        return bp

    def compute_spatial_activation(self, data):
        """두정엽 공간 처리 활성도 계산

        공간 주의 시 두정엽 알파(8-12Hz) 억제 발생.
        알파 파워가 낮을수록 공간 처리 활성.
        """
        parietal_chs = list(CHANNELS["parietal"].values())
        occipital_chs = list(CHANNELS["occipital"].values())

        # 두정엽 알파 파워 (tau=4 채널 평균)
        parietal_alpha = np.mean([
            self.get_band_power(data, ch, "alpha")
            for ch in parietal_chs
        ])

        # 후두엽 알파 (기저선 대조)
        occipital_alpha = np.mean([
            self.get_band_power(data, ch, "alpha")
            for ch in occipital_chs
        ])

        # 두정엽 세타 (공간 탐색 지표)
        parietal_theta = np.mean([
            self.get_band_power(data, ch, "theta")
            for ch in parietal_chs
        ])

        # 공간 활성도 = 알파 억제 비율 + 세타 증가
        if occipital_alpha > 0 and self.baseline_alpha and self.baseline_alpha > 0:
            alpha_suppression = 1.0 - (parietal_alpha / self.baseline_alpha)
            theta_boost = parietal_theta / (parietal_alpha + 1e-10)
            activation = np.clip(alpha_suppression * 0.7 + theta_boost * 0.3, 0, 1)
        else:
            activation = 0.0

        self.spatial_activation = activation
        return {
            "parietal_alpha": float(parietal_alpha),
            "occipital_alpha": float(occipital_alpha),
            "parietal_theta": float(parietal_theta),
            "spatial_activation": float(activation),
        }

    def calibrate(self, duration_sec=30):
        """기저선 캘리브레이션 (3D 과제로 기저선 EEG 측정)"""
        print(f"[캘리브레이션] {duration_sec}초간 편안히 눈 감고 대기...")
        time.sleep(2)

        alphas = []
        start = time.time()
        while time.time() - start < duration_sec:
            data = self.board.get_current_board_data(self.sampling_rate)
            parietal_chs = list(CHANNELS["parietal"].values())
            pa = np.mean([
                self.get_band_power(data, ch, "alpha")
                for ch in parietal_chs
            ])
            alphas.append(pa)
            time.sleep(1)

        self.baseline_alpha = np.mean(alphas)
        print(f"[캘리브레이션] 기저선 알파 = {self.baseline_alpha:.4f}")
        print(f"[캘리브레이션] 알파 범위 = {BANDS['alpha']} Hz = (sigma-tau, sigma)")
        return self.baseline_alpha

    def generate_4d_trial(self):
        """4D 공간 과제 생성

        w축 방향 판단: "소리/진동이 w+ 방향인가 w- 방향인가?"
        """
        self.current_w = np.random.choice([-1.0, -0.5, 0.5, 1.0])
        self.trial_count += 1
        return {
            "trial": self.trial_count,
            "w_target": float(self.current_w),
            "w_audio_freq": 130 + (self.current_w + 1) * 935,  # 130~2000Hz
            "w_vibration": (self.current_w + 1) / 2,  # 0~1 진동 강도
        }

    def evaluate_response(self, user_answer):
        """사용자 응답 평가 + 뉴로피드백"""
        correct = (user_answer > 0) == (self.current_w > 0)
        if correct:
            self.correct_count += 1

        accuracy = self.correct_count / max(1, self.trial_count)

        return {
            "correct": correct,
            "trial": self.trial_count,
            "accuracy": float(accuracy),
            "spatial_activation": float(self.spatial_activation),
            "feedback": "STRENGTHEN" if correct and self.spatial_activation > 0.5 else
                       "CORRECT" if correct else "RETRY",
        }

    def get_realtime_state(self):
        """실시간 상태 (웹소켓 전송용)"""
        data = self.board.get_current_board_data(self.sampling_rate)
        metrics = self.compute_spatial_activation(data)

        return {
            "timestamp": time.time(),
            "metrics": metrics,
            "trial_count": self.trial_count,
            "correct_count": self.correct_count,
            "accuracy": self.correct_count / max(1, self.trial_count),
            "current_w": float(self.current_w),
            "n6": {
                "channels": len(self.eeg_channels),
                "channels_n6": f"phi^tau = {PHI}^{TAU} = {PHI**TAU}",
                "parietal_count": TAU,
                "alpha_band": f"{SIGMA-TAU}-{SIGMA} Hz",
                "modalities": SOPFR,
            },
        }

    async def ws_handler(self, websocket):
        """웹소켓 핸들러 — 실시간 EEG 데이터 스트리밍"""
        self.ws_clients.add(websocket)
        try:
            async for message in websocket:
                msg = json.loads(message)
                if msg.get("type") == "response":
                    result = self.evaluate_response(msg["answer"])
                    await websocket.send(json.dumps({"type": "feedback", **result}))
                elif msg.get("type") == "new_trial":
                    trial = self.generate_4d_trial()
                    await websocket.send(json.dumps({"type": "trial", **trial}))
                elif msg.get("type") == "calibrate":
                    self.calibrate(duration_sec=10)
                    await websocket.send(json.dumps({"type": "calibrated", "baseline": float(self.baseline_alpha or 0)}))
        finally:
            self.ws_clients.discard(websocket)

    async def broadcast_loop(self):
        """실시간 EEG 브로드캐스트 (초당 n=6회)"""
        while True:
            if self.ws_clients and self.board:
                state = self.get_realtime_state()
                msg = json.dumps({"type": "eeg_state", **state})
                dead = set()
                for ws in self.ws_clients:
                    try:
                        await ws.send(msg)
                    except Exception:
                        dead.add(ws)
                self.ws_clients -= dead
            await asyncio.sleep(1.0 / N)  # n=6 Hz 전송

    async def run_server(self, host="localhost", port=6600):
        """웹소켓 서버 시작"""
        import websockets
        print(f"[HEXA-SENSE] 웹소켓 서버: ws://{host}:{port}")
        print(f"[HEXA-SENSE] 전송 주기: {N}Hz (= n)")

        broadcast_task = asyncio.create_task(self.broadcast_loop())
        async with websockets.serve(self.ws_handler, host, port):
            await asyncio.Future()  # 영원히 대기


def main():
    parser = argparse.ArgumentParser(description="HEXA-SENSE: BCI 뉴로피드백 4D 지각 시스템")
    parser.add_argument("--port", default="/dev/cu.usbserial-DM0258EI",
                        help="OpenBCI 시리얼 포트")
    parser.add_argument("--synthetic", action="store_true",
                        help="OpenBCI 없이 가상 데이터로 테스트")
    parser.add_argument("--ws-port", type=int, default=6600,
                        help="웹소켓 포트 (기본 6600 = n*1100)")
    parser.add_argument("--calibrate", type=int, default=30,
                        help="캘리브레이션 시간 (초)")
    args = parser.parse_args()

    sense = HexaSense(serial_port=args.port, synthetic=args.synthetic)

    try:
        sense.start()
        sense.calibrate(duration_sec=args.calibrate)
        asyncio.run(sense.run_server(port=args.ws_port))
    except KeyboardInterrupt:
        print("\n[HEXA-SENSE] 종료")
    finally:
        sense.stop()


if __name__ == "__main__":
    main()
