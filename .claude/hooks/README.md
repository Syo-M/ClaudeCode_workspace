# Hooks

このディレクトリには Claude Code のイベントフックスクリプトを置きます。
フック自体は `.claude/settings.json` の `hooks` フィールドで宣言します。

## 例: コミット前に lint を走らせる

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "command": ".claude/hooks/pre-commit-lint.sh"
      }
    ]
  }
}
```

## 注意

- フックの追加は `update-config` スキルに任せると安全
- ハードな自動化はトークンも時間も食う。本当に必要なものだけ
