# ubu 머신 blowup 모듈 exit 137 원인 진단 — 2026-04-14

> `project_blowup_module_sigkill.md` 미해결 항목 후속. 이번 세션에서 원격 진단 수행.

## 1. 문제 요약

- macOS 측 SIGKILL 은 해결됨 (`project_hexa_binary_deploy_block.md`):
  - 원인: AppleSystemPolicy adhoc codesign 누락
  - 해결: `codesign --sign - --force` + canonical 경로 배포
- **ubu Linux 머신**: 동일 blowup 모듈이 여전히 exit 137 → **별개 원인**

exit 137 = 128 + 9 = SIGKILL 수신 후 종료.

## 2. 이번 세션 측정

```
$ ssh ubu 'uname -a && uptime'
Linux aiden-B650M-K 6.17.0-20-generic Ubuntu SMP
12:16:41 up 5 days, 17:43
```

### 2.1 리소스 (메모리 원인 아님)

| 항목 | 값 | 판정 |
|---|---|---|
| RAM 총량 | 30 Gi | 여유 |
| RAM 사용 | 1.9 Gi | — |
| **RAM 여유** | **28 Gi** | **OOM 불가능** |
| Swap 총량 | 8 Gi | — |
| Swap 사용 | 2.8 Gi | 정상 |
| 디스크 여유 | 643 Gi / 915 Gi | 여유 |

### 2.2 cgroup/ulimit

```
$ ssh ubu 'cat /sys/fs/cgroup/user.slice/user-1000.slice/memory.max'
max
```

→ 사용자 cgroup 메모리 제한 **없음**. cgroup OOM 불가.

```
$ ssh ubu 'ulimit -a'
core file size              (blocks, -c) 0
max locked memory           (kbytes, -l) 3993124   ← 4 GB
max memory size             (kbytes, -m) unlimited
open files                          (-n) 1024      ← 의심
stack size                  (kbytes, -s) 8192
virtual memory              (kbytes, -v) unlimited
max user processes                  (-u) 124075
```

### 2.3 실행 중 워치독

```
$ ssh ubu 'ps aux | grep -iE "watchdog|guard"'
root  112  S  [watchdogd]    ← 커널 워치독, 유저 프로세스 kill 안 함
```

→ `n6_guard`, `launcher_cap`, `resource_coordinator` 등 **유저 워치독 없음**.

### 2.4 systemd user 서비스

```
airgenome-harvest.service  activating start  ← 6축 genome collection
```

→ airgenome 이 유일한 사용자 데몬. blowup 과 무관.

### 2.5 dmesg

```
dmesg: 커널 버퍼 읽기 실패: 명령을 허용하지 않음
```

→ root 권한 필요. dmesg OOM killer 로그 확인 불가 (다음 세션 `sudo dmesg` 또는 `journalctl -k`).

## 3. 남은 가설 (우선순위)

### H1. `open files 1024` 초과 (★★★ 유력)

blowup 모듈이 5 모듈 × 다수 .json/.hexa 동시 로드 시 fd 1024 초과 가능.

**검증**: `ssh ubu 'ulimit -n 65536 && blowup.hexa --fast --max-rounds 1'` 로 재시도.

### H2. `max locked memory 4 GB` 초과 (★★ 중)

hexa VM 이 mlock 시 4 GB 제한 hit.

**검증**: `ssh ubu 'ulimit -l unlimited && blowup.hexa ...'` 재시도.

### H3. SSH/tmux disconnect SIGHUP → exit 129 (∗ 낮음, 하지만 137 과 혼동 가능)

tmux/nohup 미사용 시 SSH 끊기면 SIGHUP. 하지만 exit code 137 ≠ 129.

### H4. 외부 프로세스 kill (∗ 낮음)

airgenome-harvest 가 blowup 프로세스를 kill? 가능성 희박 — 별도 서비스.

### H5. 커널 OOM killer (cgroup 아닌 system-wide) (∗ 낮음)

시스템 전역 OOM killer. 28 Gi 여유라 현실적으로 거의 불가능.

**검증**: `ssh ubu 'sudo dmesg | grep -i oom'` 또는 `journalctl -k -g oom`.

## 4. 우회 (즉시 가용)

- **macOS 측**: `HEXA_BIN=hexa.patched BLOWUP_LOCAL=1 blowup.hexa` (이미 검증됨, `--fast --max-rounds 2` 40초 PASS)
- **ubu 측**: H1 우회 — `ulimit -n 65536` 선행 실행 권장. 본 세션에서 실제 재현 미수행.

## 5. 다음 세션 액션

1. `ssh ubu 'ulimit -n 65536 && HEXA_BIN=hexa.patched blowup.hexa --fast --max-rounds 1'` 실행 → exit code 기록
2. 실패 시 `journalctl -k -g "kill\|oom" --since "1 hour ago"` 확인 (sudo 필요)
3. `strace -f -e trace=signal blowup.hexa` 로 SIGKILL 송신자 식별
4. H1~H5 순차 배제

## 6. 정직 기록

- 본 세션은 **원격 진단만 수행**. 실제 ubu 에서 blowup 재현 안 함 (시간 제약).
- H1 (fd 1024) 이 가장 유력하나 미검증.
- 결론: ubu exit 137 은 메모리 원인이 아님 — fd/mlock/외부 kill 중 하나로 좁혀짐.
- 메모리 `project_blowup_module_sigkill.md` 의 "미해결" 항목 유지. 다음 세션에 실측 필요.
