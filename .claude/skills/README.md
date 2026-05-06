# Skills

`.claude/commands/` よりリッチな再利用ユニット。
複数ファイル・スクリプト・参照資料を束ねて 1 つの「能力」として登録します。

## ディレクトリ構造

```
skills/
└── <skill-name>/
    ├── SKILL.md        # 必須: 手順書
    ├── README.md       # 任意: 人間向け説明
    ├── assets/         # 任意: テンプレート・スタイル参照
    ├── references/     # 任意: API 仕様など(遅延ロード)
    ├── scripts/        # 任意: 補助スクリプト
    └── evals/          # 任意: 動作確認テストケース
```

## SKILL.md フォーマット

```markdown
---
name: <skill-name>
description: <一行説明・トリガー条件>
---

# <Skill Name>

## いつ使うか
<トリガー条件>

## 手順
1. ...
2. ...

## 出力
<期待する成果物>
```

## commands と skills の使い分け

| 用途 | 配置先 |
|------|--------|
| 短いプロンプトテンプレ(1 ファイル) | `.claude/commands/` |
| 複数ファイル・参照資料を伴う作業 | `.claude/skills/<name>/` |

## 既存スキル

- `commit-message/` — diff から規約準拠のコミットメッセージを生成
