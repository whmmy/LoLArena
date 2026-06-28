#!/usr/bin/env bash
# ============================================================
#  LoLArena — 一键安装脚本 (CentOS + uv)
#
#  用法 (在项目根目录, 即 requirements.txt 所在处执行):
#      bash deploy/install.sh
#
#  做的事:
#    1. 用 uv 建 Python 虚拟环境 + 装依赖 (uv sync 优先, 回退 uv pip install -r)
#    2. 生成 .env (若不存在) — 自动把 LOLA_HOST 改成 0.0.0.0 (首次部署)
#    3. 生成并安装 systemd service (开机自启 + 崩溃自动重启)
#    4. 开放防火墙端口
#    5. 安装后做一次 sanity check
#
#  可调环境变量:
#      PYTHON_VERSION=3.11     # 改用其它 Python 版本
#      LOLA_PORT=8000          # 监听端口
#      LOLA_HOST=0.0.0.0      # 监听地址 (部署到服务器通常改 0.0.0.0)
#      SKIP_FIREWALL=1         # 跳过 firewalld/iptables 配置
#      SKIP_ENV_EDIT=1         # 不动 .env (你自己手动配)
# ============================================================
set -euo pipefail

# --- 解析路径 ---
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INSTALL_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
SERVICE_NAME="lolarena"
RUN_USER="$(whoami)"
PYTHON_VERSION="${PYTHON_VERSION:-3.11}"
LOLA_PORT="${LOLA_PORT:-8000}"
LOLA_HOST="${LOLA_HOST:-0.0.0.0}"

echo "=========================================================="
echo "  LoLArena 安装"
echo "  安装目录: $INSTALL_DIR"
echo "  运行用户: $RUN_USER"
echo "  Python  : $PYTHON_VERSION (via uv)"
echo "  监听    : $LOLA_HOST:$LOLA_PORT"
echo "=========================================================="

# --- 0. 基本检查 ---
if [ ! -f "$INSTALL_DIR/requirements.txt" ] || [ ! -d "$INSTALL_DIR/src" ]; then
    echo "❌  未在 $INSTALL_DIR 找到 requirements.txt / src/"
    echo "    请在项目根目录执行本脚本 (deploy/install.sh)"
    exit 1
fi

# --- 1. 检查 uv ---
if ! command -v uv >/dev/null 2>&1; then
    echo "[1/5] uv 未安装, 正在安装..."
    if [ -f "$HOME/.local/bin/env" ]; then
        # shellcheck disable=SC1091
        source "$HOME/.local/bin/env"
    fi
    if ! command -v uv >/dev/null 2>&1; then
        curl -LsSf https://astral.sh/uv/install.sh | sh
        # shellcheck disable=SC1091
        source "$HOME/.local/bin/env"
    fi
fi
echo "[1/5] uv: $(uv --version)"

# --- 2. 建虚拟环境 + 装依赖 ---
cd "$INSTALL_DIR"
if [ ! -d ".venv" ]; then
    echo "[2/5] 创建虚拟环境..."
    uv venv --python "$PYTHON_VERSION"
else
    echo "[2/5] 虚拟环境已存在, 复用: .venv"
fi

echo "      安装依赖..."
if uv sync --frozen 2>/dev/null; then
    echo "      ✓ uv sync (frozen) 完成"
elif uv sync 2>/dev/null; then
    echo "      ✓ uv sync 完成"
else
    echo "      uv sync 不可用, 回退到 uv pip install -r requirements.txt"
    uv pip install -r requirements.txt
fi

# --- 3. 生成 / 修正 .env ---
if [ ! -f "$INSTALL_DIR/.env" ]; then
    echo "[3/5] 生成 .env (从 .env.example)..."
    cp .env.example .env
    echo "      ⚠️  请编辑 .env 填入 API key:"
    echo "          vi $INSTALL_DIR/.env"
fi

if [ "${SKIP_ENV_EDIT:-0}" != "1" ] && [ -f "$INSTALL_DIR/.env" ]; then
    # 把 LOLA_HOST 改成 0.0.0.0, LOLA_PORT 改成目标端口 (幂等).
    # 部署到服务器必须监听 0.0.0.0 才能从外部访问; 127.0.0.1 只在本机有效.
    echo "      校正 .env 监听地址 -> $LOLA_HOST:$LOLA_PORT"
    if grep -qE '^[[:space:]]*LOLA_HOST=' "$INSTALL_DIR/.env"; then
        sed -i.bak -E "s|^[[:space:]]*LOLA_HOST=.*|LOLA_HOST=$LOLA_HOST|" "$INSTALL_DIR/.env"
    else
        echo "LOLA_HOST=$LOLA_HOST" >> "$INSTALL_DIR/.env"
    fi
    if grep -qE '^[[:space:]]*LOLA_PORT=' "$INSTALL_DIR/.env"; then
        sed -i -E "s|^[[:space:]]*LOLA_PORT=.*|LOLA_PORT=$LOLA_PORT|" "$INSTALL_DIR/.env"
    else
        echo "LOLA_PORT=$LOLA_PORT" >> "$INSTALL_DIR/.env"
    fi
fi

# --- 4. 安装 systemd service ---
echo "[4/5] 安装 systemd service..."
SERVICE_SRC="$INSTALL_DIR/deploy/lolarena.service"
SERVICE_DST="/etc/systemd/system/${SERVICE_NAME}.service"

if [ ! -f "$SERVICE_SRC" ]; then
    echo "❌  找不到 service 模板: $SERVICE_SRC"
    exit 1
fi

# 占位符替换: __INSTALL_DIR__ / __USER__ / __LOLA_HOST__ / __LOLA_PORT__
sudo sed \
    -e "s|__INSTALL_DIR__|$INSTALL_DIR|g" \
    -e "s|__USER__|$RUN_USER|g" \
    -e "s|__LOLA_HOST__|$LOLA_HOST|g" \
    -e "s|__LOLA_PORT__|$LOLA_PORT|g" \
    "$SERVICE_SRC" > "$SERVICE_DST"

sudo systemctl daemon-reload
sudo systemctl enable "$SERVICE_NAME"
echo "      service 已安装并设为开机自启。"

# --- 5. 开放防火墙 + sanity check ---
if [ "${SKIP_FIREWALL:-0}" = "1" ]; then
    echo "[5/5] SKIP_FIREWALL=1, 跳过防火墙配置"
else
    echo "[5/5] 开放防火墙 $LOLA_PORT 端口..."
    if command -v firewall-cmd >/dev/null 2>&1; then
        sudo firewall-cmd --permanent --add-port="$LOLA_PORT/tcp" && sudo firewall-cmd --reload
        echo "      firewalld 已放行 $LOLA_PORT/tcp。"
    elif command -v iptables >/dev/null 2>&1; then
        sudo iptables -I INPUT -p tcp --dport "$LOLA_PORT" -j ACCEPT
        echo "      iptables 已放行 $LOLA_PORT/tcp (注意: 重启后可能需持久化)。"
    else
        echo "      ⚠️  未检测到 firewalld/iptables, 请手动放行 $LOLA_PORT/tcp。"
    fi
fi

# --- Sanity check ---
echo ""
echo "[sanity] 检查依赖 + 入口模块..."
if .venv/bin/python -c "
import importlib, sys
for m in ('fastapi', 'uvicorn', 'yaml', 'dotenv', 'apscheduler', 'openai', 'anthropic', 'google.genai'):
    importlib.import_module(m)
# 入口模块在 src/ 下, 路径里要能 import 到
sys.path.insert(0, '.')
from src import cli  # noqa: F401
print('      ✓ 关键模块 OK')
" 2>&1 | grep -q "关键模块 OK"; then
    :
else
    echo "      ⚠️  模块导入失败, 请检查上面的错误日志。"
fi

# --- 完成 ---
echo ""
echo "=========================================================="
echo "  ✅ 安装完成!"
echo "=========================================================="
echo ""
echo "  启动服务:   sudo systemctl start $SERVICE_NAME"
echo "  查看状态:   sudo systemctl status $SERVICE_NAME"
echo "  查看日志:   sudo journalctl -u $SERVICE_NAME -f"
echo "  停止/重启:  sudo systemctl {stop|restart} $SERVICE_NAME"
echo ""
echo "  首次使用前务必填好 .env (API key 等):"
echo "      vi $INSTALL_DIR/.env"
echo "      sudo systemctl restart $SERVICE_NAME"
echo ""
echo "  访问: http://<服务器IP>:$LOLA_PORT"
echo "  (别忘了云厂商控制台的「安全组」也要放行 $LOLA_PORT/tcp)"
echo ""
