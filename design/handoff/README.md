# Handoff

Claude Design からの **Handoff Bundle** を受け取る場所。

## 命名規則

```
handoff/
└── YYYYMMDD-<short-name>/
    ├── bundle.zip          # Claude Design から DL した zip
    ├── source-url.txt      # api.anthropic.com/v1/design/h/<hash> の URL
    └── notes.md            # この引き継ぎの目的・コンテキスト
```

## 取り込み手順

1. Claude Design で「Handoff to Claude Code」を実行
2. クリップボードに引き継ぎコマンドがコピーされる
3. Claude Code に貼り付ける、または `/design-import <URL>` を実行
4. Claude が自動で `handoff/YYYYMMDD-<name>/` に保存

## なぜ git に残すか

- ハンドオフ URL は失効する可能性があるため、`bundle.zip` をローカル保存
- 後から「あの時のデザイン参照」が辿れるように

## 大きすぎる場合

`bundle.zip` が数十 MB を超えるなら git LFS を検討。
緊急時は `.gitignore` で個別除外も可。
