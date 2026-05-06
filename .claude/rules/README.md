# Rules

ここには **path スコープ付きのルール** を 1 ファイル 1 トピックで置きます。
CLAUDE.md を肥大化させずに、特定ファイルを触るときだけ Claude が読むようにできます。

## フォーマット

```markdown
---
paths: ["**/*.py"]   # このパターンに合致するファイルを編集する時だけ読まれる
---

- ルール 1
- ルール 2
```

`paths:` を書かない場合は全ファイル対象(常時適用)。

## 命名

- `<対象>-<トピック>.md` 形式を推奨
  - `python-style.md`, `typescript-imports.md`, `sql-naming.md`
- 1 ファイルは 30 行以内を目安(短く保つ)

## 既存ルール

- `python.md` — Python のスタイル
- `typescript.md` — TypeScript のスタイル
- `markdown.md` — Markdown ドキュメントの書き方
