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
├── design/                  # Claude Design 連携(原本・ハンドオフ・プロトタイプ)
├── docs/                    # 規約・設計書(必要時に参照)
├── projects/                # 個別プロジェクト
│   └── _template/           # 新規プロジェクトのひな形
└── .gitignore
```

## Quick Start

このリポジトリを **初めて触る人向け**の 5 分手順:

### 1. クローン

```bash
git clone https://github.com/Syo-M/ClaudeCode_workspace.git
cd ClaudeCode_workspace
```

### 2. Claude Code を起動

```bash
claude
```

ステータスバーに `[ClaudeCode_workspace] | <branch> | <model>` が出れば設定が効いています。

### 3. はじめての対話で確認すること

最初のメッセージで `CLAUDE.md` を読みましょう。続けて以下を試すと感覚が掴めます:

```
/plan このリポジトリで TODO アプリを作る計画を立てて
/escalate              ← 今のタスクに最適なモデルを提案
/explore design/       ← サブエージェントでディレクトリ探索
```

### 4. 新規プロジェクトを始める

```
/new-project my-app
```

または手動で `cp -r projects/_template projects/my-app`。

### 5. トークン節約のクセを付ける

- タスクが終わったら `/clear`(セッションを長く引きずらない)
- 設計フェーズは `Shift+Tab` で **Plan Mode** に入る
- 重い実装が必要になるまで Opus に切り替えない

詳細は [docs/token-saving.md](docs/token-saving.md)。

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
