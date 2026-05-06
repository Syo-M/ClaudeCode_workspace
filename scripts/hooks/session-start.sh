#!/usr/bin/env bash
# SessionStart フック — Claude にトークン節約と現状の要点を最初に伝える
#
# settings.json から呼ばれ、stdout がセッション冒頭の追加コンテキストとして
# Claude に渡される。出力は短く保つこと(コンテキスト消費を最小化)。

set -euo pipefail

cd "$(dirname "$0")/../.."

branch=$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "?")
modified=$(git status --porcelain 2>/dev/null | wc -l | tr -d ' ')

cat <<EOF
## セッション開始時の確認(自動挿入)

- ブランチ: \`${branch}\` / 未コミット変更: ${modified} 件
- トークン節約のため次を意識:
  - 設計フェーズは Plan Mode (\`Shift+Tab\`)
  - 不必要に Opus を使わない(\`/escalate\` で適正モデル確認)
  - タスクが終わったら \`/clear\` でセッションを切る
- 詳細: \`docs/token-saving.md\` を必要時に Read

EOF
