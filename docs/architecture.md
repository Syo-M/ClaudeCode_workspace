# アーキテクチャ

> このファイルは CLAUDE.md からは自動参照されません。Claude が必要時に Read します。

## モノレポ方針

このリポジトリは「Claude Code 用の作業環境」を共通化するためのモノレポです。
各プロジェクトは独立して動き、共通リソース(設定・コマンド・規約)だけをルートから継承します。

```
claudeCodeVibes/         ← 共通リソースの母艦
├── .claude/             ← 共通の Claude Code 設定
├── docs/                ← 共通の規約・設計書
└── projects/
    ├── _template/       ← 新規プロジェクトのひな形
    ├── projectA/        ← 独立したプロジェクト
    │   ├── CLAUDE.md    ← プロジェクト固有方針(優先)
    │   └── .claude/     ← 必要なら設定上書き
    └── projectB/
```

## 継承の優先順位

1. `projects/<name>/CLAUDE.md` — プロジェクト固有(最優先)
2. `claudeCodeVibes/CLAUDE.md` — ルート共通
3. `~/.claude/CLAUDE.md` — ユーザーグローバル(あれば)

## 設定ファイルの読まれる順

`.claude/settings.json` は階層的にマージされます。
プロジェクト側で同じキーを定義するとそちらが勝ちます。

## トークン消費の考え方

- ルート `CLAUDE.md` は全プロジェクトで毎ターン読まれる → 50〜100 行に抑える
- プロジェクト `CLAUDE.md` はそのプロジェクト作業時のみ → 詳細はここに書く
- `docs/*.md` は明示的に Read した時のみ → 大きな設計書はここへ
