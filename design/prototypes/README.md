# Prototypes

Claude Design が生成した HTML プロトタイプの保管場所。

## 命名

```
prototypes/
└── YYYYMMDD-<feature-name>/
    ├── index.html
    ├── assets/         # 画像・フォント
    └── README.md       # 何のプロトタイプか
```

## 扱いの原則

- **そのまま本番コードに入れない**。あくまで仕様確認用
- 採用が決まったら、各 `projects/<name>/` 側で既存のトークン・コンポーネントを使って書き直す
- アクセシビリティ(`prefers-reduced-motion`、コントラスト等)は別途確認

## 確認方法

```bash
# シンプルに開く
open prototypes/<dir>/index.html

# ローカルサーバーで(モジュール読み込み等が必要な場合)
python3 -m http.server -d prototypes/<dir> 8000
```
