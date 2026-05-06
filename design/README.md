# Design

Claude Design ↔ Claude Code 連携のための共通アセット置き場です。

## ディレクトリ構成

```
design/
├── system/        # Claude Design に投入する原本(ブランド・色・タイポ・コンポーネント)
├── handoff/       # Claude Design からの Handoff Bundle 受け取り場所
└── prototypes/    # 生成された HTML プロトタイプの保管場所
```

## 想定ワークフロー

1. `design/system/` を Claude Design にアップロード(またはリポジトリ URL を渡す)
2. Claude Design でデザイン制作
3. 完成したら Claude Design から「Handoff to Claude Code」
4. クリップボードのコマンドを Claude Code に貼り付け
5. `/design-import` で `design/handoff/` に取り込み
6. 必要に応じて `design/prototypes/` の HTML を参考に各 `projects/<name>/` 側で実装

詳細は [../docs/design-workflow.md](../docs/design-workflow.md) を参照。

## プロジェクト固有のデザイン

プロジェクト固有のデザインシステムは `projects/<name>/design/` 配下に置きます。
ルートの `design/` は **組織共通のブランドアセット** を置く場所です。
