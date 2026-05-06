# 新規プロジェクトの追加手順

## 簡単な方法: スラッシュコマンド

Claude Code 内で:

```
/new-project my-app
```

## 手動で追加する場合

```bash
cp -r projects/_template projects/my-app
cd projects/my-app
```

その後、以下を編集します:

1. `projects/my-app/CLAUDE.md`
   - プロジェクト名・目的を書く
   - そのプロジェクト固有の作業ルールがあれば追記

2. `projects/my-app/README.md`
   - 起動方法・前提条件を書く(人間向け)

3. 必要なら `projects/my-app/.claude/settings.json` で設定上書き

## 命名

- `kebab-case` を推奨
- 短く、目的が分かる名前(`my-app` ではなく `slack-summarizer` のように)

## 削除

ディレクトリごと消すだけです。ルート側に残骸はありません。
