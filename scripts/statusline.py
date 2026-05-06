#!/usr/bin/env python3
"""Claude Code ステータスバー表示スクリプト.

settings.json の statusLine.command から呼ばれる。
標準入力に JSON が渡され、標準出力の 1 行が表示される。

入力 JSON の主なフィールド:
  - workspace.current_dir: 現在の作業ディレクトリ
  - model.display_name:    モデル名
  - cost.total_cost_usd:   セッション中の累計コスト(参考値)
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path


def git_branch(cwd: str) -> str:
    try:
        out = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=1,
        )
        return out.stdout.strip() if out.returncode == 0 else ""
    except (subprocess.SubprocessError, FileNotFoundError):
        return ""


def git_dirty(cwd: str) -> bool:
    try:
        out = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=1,
        )
        return bool(out.stdout.strip())
    except (subprocess.SubprocessError, FileNotFoundError):
        return False


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        payload = {}

    cwd = payload.get("workspace", {}).get("current_dir") or os.getcwd()
    project = Path(cwd).name
    model = payload.get("model", {}).get("display_name", "")

    branch = git_branch(cwd)
    if branch:
        marker = "*" if git_dirty(cwd) else ""
        branch_part = f" | {branch}{marker}"
    else:
        branch_part = ""

    model_part = f" | {model}" if model else ""

    print(f"[{project}]{branch_part}{model_part}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
