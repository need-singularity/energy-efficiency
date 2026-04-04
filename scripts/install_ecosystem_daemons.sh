#!/usr/bin/env bash
set -euo pipefail
# ═══════════════════════════════════════════════════════════════
# install_ecosystem_daemons.sh — 전 리포 launchd 데몬 설치
# ═══════════════════════════════════════════════════════════════
# 재부팅/터미널 닫아도 끊기지 않는 영구 성장 루프
# 각 리포 15분(900s) 간격, 자원 적응형
#
# Usage:
#   bash scripts/install_ecosystem_daemons.sh          # 설치 + 시작
#   bash scripts/install_ecosystem_daemons.sh --status  # 상태 확인
#   bash scripts/install_ecosystem_daemons.sh --stop    # 전부 중지
#   bash scripts/install_ecosystem_daemons.sh --uninstall # 완전 제거

LAUNCH_DIR="$HOME/Library/LaunchAgents"
LOG_DIR="$HOME/Library/Logs/n6-growth"
mkdir -p "$LAUNCH_DIR" "$LOG_DIR"

# ── Repo definitions ────────────────────────────────────────────
# repo:interval_sec:label
REPOS=(
    "n6-architecture:900:com.n6.growth.n6arch"
    "TECS-L:900:com.n6.growth.tecsl"
    "sedi:900:com.n6.growth.sedi"
    "brainwire:900:com.n6.growth.brainwire"
    "hexa-lang:900:com.n6.growth.hexalang"
    "fathom:900:com.n6.growth.fathom"
    "papers:1800:com.n6.growth.papers"
)

# Orchestrator (manages staggered launch)
ORCH_LABEL="com.n6.growth.orchestrator"

generate_plist() {
    local repo="$1" interval="$2" label="$3"
    local script="$HOME/Dev/$repo/scripts/infinite_growth.sh"
    local logfile="$LOG_DIR/${repo}.log"

    cat <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>$label</string>
    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>$script</string>
        <string>--max-cycles</string>
        <string>999</string>
        <string>--interval</string>
        <string>$interval</string>
    </array>
    <key>StartInterval</key>
    <integer>$interval</integer>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <dict>
        <key>SuccessfulExit</key>
        <false/>
    </dict>
    <key>WorkingDirectory</key>
    <string>$HOME/Dev/$repo</string>
    <key>StandardOutPath</key>
    <string>$logfile</string>
    <key>StandardErrorPath</key>
    <string>$logfile</string>
    <key>EnvironmentVariables</key>
    <dict>
        <key>PATH</key>
        <string>/usr/local/bin:/usr/bin:/bin:$HOME/.cargo/bin:$HOME/.local/bin</string>
        <key>HOME</key>
        <string>$HOME</string>
    </dict>
    <key>ProcessType</key>
    <string>Background</string>
    <key>LowPriorityIO</key>
    <true/>
    <key>Nice</key>
    <integer>10</integer>
</dict>
</plist>
PLIST
}

install_all() {
    echo "╔═══════════════════════════════════════════════════════════╗"
    echo "║  Installing Ecosystem Growth Daemons                     ║"
    echo "║  ${#REPOS[@]} repos + orchestrator                               ║"
    echo "╚═══════════════════════════════════════════════════════════╝"
    echo ""

    local installed=0
    for entry in "${REPOS[@]}"; do
        IFS=':' read -r repo interval label <<< "$entry"
        local script="$HOME/Dev/$repo/scripts/infinite_growth.sh"
        local plist="$LAUNCH_DIR/${label}.plist"

        if [ ! -f "$script" ]; then
            echo "  ⏭️  $repo: no growth script"
            continue
        fi

        # Unload existing if any
        launchctl unload "$plist" 2>/dev/null || true

        # Generate and write plist
        generate_plist "$repo" "$interval" "$label" > "$plist"

        # Load
        launchctl load "$plist" 2>/dev/null && {
            echo "  ✅ $repo (${interval}s) → $label"
            installed=$((installed + 1))
        } || {
            echo "  ❌ $repo: launchctl load failed"
        }
    done

    echo ""
    echo "Installed: $installed/${#REPOS[@]} daemons"
    echo "Logs: $LOG_DIR/"
    echo ""
    echo "Check: bash $0 --status"
}

show_status() {
    echo "╔═══════════════════════════════════════════════════════════╗"
    echo "║  Ecosystem Growth Daemon Status                          ║"
    echo "╠═══════════════════════════════════════════════════════════╣"
    for entry in "${REPOS[@]}"; do
        IFS=':' read -r repo interval label <<< "$entry"
        local plist="$LAUNCH_DIR/${label}.plist"
        local logfile="$LOG_DIR/${repo}.log"

        if [ ! -f "$plist" ]; then
            printf "║  %-17s ⚫ not installed\n" "$repo"
            continue
        fi

        # Check if loaded
        local loaded="NO"
        launchctl list 2>/dev/null | grep -q "$label" && loaded="YES"

        # Check PID
        local pid_info=""
        local pid
        pid=$(launchctl list 2>/dev/null | grep "$label" | awk '{print $1}') || pid="-"

        # Check last log activity
        local last_activity=""
        if [ -f "$logfile" ]; then
            local log_age
            log_age=$(python3 -c "
import os, time
mtime = os.path.getmtime('$logfile')
age = int(time.time() - mtime)
if age < 60: print(f'{age}s ago')
elif age < 3600: print(f'{age//60}m ago')
else: print(f'{age//3600}h ago')
" 2>/dev/null || echo "?")
            last_activity=" last=$log_age"
        fi

        if [ "$loaded" = "YES" ] && [ "$pid" != "-" ] && [ "$pid" != "0" ]; then
            printf "║  %-17s ✅ PID %-6s %ss%s\n" "$repo" "$pid" "$interval" "$last_activity"
        elif [ "$loaded" = "YES" ]; then
            printf "║  %-17s 🔄 loaded (waiting)%s\n" "$repo" "$last_activity"
        else
            printf "║  %-17s ❌ not loaded\n" "$repo"
        fi
    done

    # Nexus6 daemon (separate)
    local n6_label="com.nexus6.growth"
    local n6_loaded="NO"
    launchctl list 2>/dev/null | grep -q "$n6_label" && n6_loaded="YES"
    if [ "$n6_loaded" = "YES" ]; then
        local n6_pid
        n6_pid=$(launchctl list 2>/dev/null | grep "$n6_label" | awk '{print $1}') || n6_pid="-"
        printf "║  %-17s ✅ PID %-6s (nexus6 daemon)\n" "nexus6" "$n6_pid"
    else
        printf "║  %-17s ⚫ separate daemon\n" "nexus6"
    fi

    echo "╚═══════════════════════════════════════════════════════════╝"
}

stop_all() {
    echo "Stopping all growth daemons..."
    for entry in "${REPOS[@]}"; do
        IFS=':' read -r repo interval label <<< "$entry"
        local plist="$LAUNCH_DIR/${label}.plist"
        launchctl unload "$plist" 2>/dev/null && echo "  ⏹️  $repo" || true
    done
    # Kill any remaining processes
    for pid in $(ps aux | grep 'infinite_growth.*max-cycles' | grep -v grep | awk '{print $2}'); do
        kill "$pid" 2>/dev/null || true
    done
    rm -f /tmp/*growth*.pid /tmp/n6_infinite*.pid /tmp/n6_orchestrator.pid 2>/dev/null
    echo "All stopped."
}

uninstall_all() {
    stop_all
    echo ""
    echo "Removing plist files..."
    for entry in "${REPOS[@]}"; do
        IFS=':' read -r repo interval label <<< "$entry"
        rm -f "$LAUNCH_DIR/${label}.plist" && echo "  🗑️  $label" || true
    done
    echo "Uninstalled."
}

# ── Main ────────────────────────────────────────────────────────
case "${1:-}" in
    --status)    show_status ;;
    --stop)      stop_all ;;
    --uninstall) uninstall_all ;;
    *)           install_all ;;
esac
