# Claude Design ↔ Claude Code 連携ワークフロー

> 必要時に Read します。CLAUDE.md からは自動参照されません。

## 全体像

```
[design/system/]  →  Claude Design  →  [design/handoff/]  →  実装(projects/<name>/)
   (原本)           (Web で制作)         (ハンドオフ)            (Claude Code)
```

## いつ Claude Design を使うか

- ✅ **使う**: ワイヤーフレーム探索、複数案の比較、ピッチデック、LP モック
- ❌ **使わない**: 既存 UI の小修正、ロジック実装、テスト、デバッグ

## 使う前の準備

1. `design/system/` の以下を最新化:
   - `brand-guide.md`
   - `colors.md`
   - `typography.md`
   - `components/` のスクショ
2. リポジトリを GitHub にプッシュ(URL を Claude Design に渡す場合)

## 制作フロー

1. Claude Design を開く
2. **入力を渡す**:
   - リポジトリ URL を貼る(自動でデザインシステム抽出)、**または**
   - `design/system/` のファイルをアップロード
3. チャットで要件を伝える(「ECサイトの商品詳細ページを作って」等)
4. キャンバスで生成結果を確認、インラインコメントで微修正
5. 完成したら **「Handoff to Claude Code」**

## Claude Code 側で受け取る

```
/design-import <ハンドオフURL>
```

または手動で zip を `design/handoff/YYYYMMDD-<name>/bundle.zip` に保存。

## 実装に降ろす(重要)

ハンドオフはプロトタイプ。**本番コードに直接コピペしない**。手順:

1. `design/prototypes/<dir>/index.html` をブラウザで確認
2. 採用範囲を決める(全部?ヒーローだけ?)
3. `projects/<name>/` 側で:
   - 既存のトークン(`colors.md` など)を使って書き直す
   - 既存のコンポーネントを再利用
   - アクセシビリティを別途確認
4. プロトタイプは `design/prototypes/` に残しておく(差分の参照に使う)

詳細チェックは [.claude/rules/design-handoff.md](../.claude/rules/design-handoff.md) を参照。

## トークン消費の注意

- Claude Design は通常チャットより重い(画像生成・大量出力を含む)
- **Pro プランでは Claude Design の使用を厳選**。ハンドオフ後の実装は Claude Code 側でやり、Claude Design に戻る回数を減らす
- 微修正は Claude Design に戻らず、Claude Code でコードを直接編集する方が安い

## デザインシステム更新の手順

1. `design/system/*.md` を編集してコミット・プッシュ
2. Claude Design の Organization 設定 → デザインシステム → 「リミックス」
3. 過去のハンドオフは古いシステムベースなので、必要なら再生成

## トラブルシューティング

- **ハンドオフ URL が失効した** → `design/handoff/<dir>/bundle.zip` を直接使う
- **生成が安定しない** → `design/system/components/` のスクショを充実させる
- **ブランドが反映されない** → リポジトリ URL を渡し直し、または個別アセット再投入
