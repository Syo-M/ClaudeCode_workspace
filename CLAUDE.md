# claudeCodeVibes — ルート方針

このリポジトリは Claude Code を使った複数プロジェクトの母艦です。
ルートの方針はここに**最小限だけ**記述し、詳細は必要時に参照します。

## 作業ルール

- 個別プロジェクトの作業時は `projects/<name>/CLAUDE.md` を最優先で読む
- ルート直下にプロジェクトコードを置かない。新規プロジェクトは `projects/<name>/` に作る
- ドキュメント生成系(README.md など)はユーザーが明示的に依頼した時だけ作成

## 参照ポインタ(必要時に読む)

CLAUDE.md は毎ターン全文がコンテキストに載るため、以下は**必要時だけ Read** します。

- `docs/conventions.md` — コーディング規約・コミット規約
- `docs/architecture.md` — リポジトリ全体の設計
- `docs/new-project.md` — 新規プロジェクト追加手順
- `.claude/commands/` — スラッシュコマンド(短いプロンプトテンプレ)
- `.claude/skills/` — スキル(複数ファイルを伴う再利用ユニット)
- `.claude/rules/` — ファイル種別ごとのルール(編集時に自動参照)
- `.claude/agents/` — サブエージェント定義
- `memory/README.md` — auto memory の保存先と運用

## トークン節約の指針

- 探索は Explore サブエージェントに委譲(`docs/` 全文走査などはメインに持ち込まない)
- 大きな出力(`git log` 全件、`find /` など)は head/tail で絞ってから読む
- 同じ指示を 2 回書きそうになったら `.claude/commands/` に切り出す
