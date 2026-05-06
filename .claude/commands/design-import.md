---
description: Claude Design の Handoff Bundle を design/handoff/ に取り込む
---

Claude Design からの Handoff Bundle URL または zip を `design/handoff/` に取り込んでください。

入力(URL またはローカル zip パス): $ARGUMENTS

## 手順

1. 入力が `api.anthropic.com/v1/design/` 系の URL なら、WebFetch で内容を確認(または curl で zip を取得)
2. 入力が空なら、ユーザーに URL を聞く
3. 取り込み先ディレクトリ名を生成: `design/handoff/<YYYYMMDD>-<short-name>/`
   - short-name はユーザーに確認するか、URL/zip 内の情報から推測
4. 以下を保存:
   - `bundle.zip` (取得した場合)
   - `source-url.txt` (URL を 1 行で)
   - `notes.md` (目的・コンテキストの空テンプレ)
5. zip を取得した場合は同ディレクトリに展開し、HTML エントリポイントを特定
6. `design/prototypes/` にもコピーして、すぐ確認できる状態にする

## 出力

3 行以内で報告:
- 保存先パス
- HTML プロトタイプのエントリポイント
- 次にやるべきこと(プレビュー、または `/projects/<name>` への適用)

## 注意

- bundle.zip が大きい(>20MB)場合は警告を出す
- ハンドオフ URL は失効する可能性があるため、必ずローカル保存を優先
- 取り込み後、生成 HTML を **本番コードに直接マージしない** よう促す
