# claudeCodeVibes

Claude Code を使った複数プロジェクトの作業用モノレポです。
共通の設定・スラッシュコマンド・サブエージェントをルートで一元管理し、各プロジェクトは `projects/` 配下に分離して育てます。

## ディレクトリ構成

```
claudeCodeVibes/
├── CLAUDE.md                # ルートの作業方針(薄く保つ)
├── README.md                # このファイル(人間向け)
├── .mcp.json                # MCP サーバ設定(空ひな形)
├── .claude/
│   ├── settings.json        # 共有設定(コミット対象)
│   ├── settings.local.json  # 個人設定(.gitignore)
│   ├── commands/            # スラッシュコマンド(短いテンプレ)
│   ├── skills/              # スキル(複数ファイル束ねた能力)
│   ├── rules/               # paths スコープ付きルール
│   ├── agents/              # サブエージェント定義
│   └── hooks/               # 自動化フック
├── scripts/
│   └── statusline.py        # ステータスバー表示
├── memory/                  # auto memory のドキュメント(実体は ~/.claude 配下)
├── docs/                    # 規約・設計書(必要時に参照)
├── projects/                # 個別プロジェクト
│   └── _template/           # 新規プロジェクトのひな形
└── .gitignore
```

## はじめかた

```bash
# Claude Code を起動
claude

# 新しいプロジェクトを始める
cp -r projects/_template projects/my-project
cd projects/my-project
```

## 設計の意図

### CLAUDE.md は「機械向け」、README.md は「人間向け」
- `CLAUDE.md` は Claude が毎ターン読み込む方針書(短く)
- `README.md` は人間が読むドキュメント(詳しく)

### トークン節約のための分離
- ルート `CLAUDE.md` には共通方針だけ。プロジェクト固有のことは `projects/<name>/CLAUDE.md` に書き、その作業中のみコンテキストに乗るようにする
- 規約・設計の詳細は `docs/` に置き、Claude が必要なときだけ Read する

### 共有設定 vs 個人設定
- `.claude/settings.json` はチーム共通(コミット)
- `.claude/settings.local.json` は個人用(`.gitignore` 済み)

## よく使うスラッシュコマンド

`.claude/commands/` 配下の Markdown ファイルが自動的に `/コマンド名` として使えます。

- `/plan` — 実装プランを立てる
- `/refactor` — 既存コードのリファクタ
- `/explore` — リポジトリ探索
- `/save-memory` — 学んだことを memory に保存

## 新規プロジェクトの追加

詳細手順は [docs/new-project.md](docs/new-project.md) を参照。
