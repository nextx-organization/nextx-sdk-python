#!/usr/bin/env bash
# Hoàn thiện cây Python vừa sinh: lối vào gọn (create_client), VERSION, siêu dữ liệu PyPI.
# Dùng chung cho build.sh (lúc sinh) và CI kho nextx-sdk-python (kiểm mã không bị sửa tay).
set -euo pipefail
P=$1; PYVER=$2; SHA=$3
PKG=$P/nextx_sdk
cp "$(dirname "$0")/nextx.py" "$PKG/nextx.py"
printf 'VERSION = "%s"\n' "$PYVER" > "$PKG/_version.py"
cat >> "$PKG/__init__.py" <<'PYEOF'

from ._version import VERSION
from .nextx import PROD_URL, SANDBOX_URL, create_client

__all__ = (*__all__, "VERSION", "PROD_URL", "SANDBOX_URL", "create_client")
PYEOF
python3 "$(dirname "$0")/patch-pyproject.py" "$P/pyproject.toml" "$SHA"
