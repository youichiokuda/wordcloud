
# 🌀 WordCloud DX Viewer

社内DX推進におけるキーワードを可視化する、Streamlit製ワードクラウドアプリです。  
日本語フォントに対応し、誰でも簡単にブラウザ上でキーワード分析ができます。

---

## 📸 スクリーンショット

![screenshot](https://github.com/youichiokuda/wordcloud/blob/main/screenshot.png)

---

## 🚀 使い方

### 1. 環境準備

Python 3.8以上 & pip 推奨。以下でライブラリをインストール：

```bash
pip install -r requirements.txt
```

### 2. アプリの起動

```bash
streamlit run wordcloud_app.py
```

### 3. ブラウザで表示

```bash
http://localhost:8501
```

---

## 📝 機能

- 日本語対応ワードクラウド生成（フォント：`NotoSansJP-Bold.ttf`）
- テキストボックスに入力したキーワードを即時描画
- StreamlitベースなのでWebブラウザだけで操作可能

---

## 📁 構成

```
.
├── wordcloud_app.py        # アプリ本体
├── requirements.txt        # 依存ライブラリ
└── NotoSansJP-Bold.ttf     # 日本語フォント（同梱）
```

---

## 🌐 デプロイ方法（例）

ローカルまたは社内サーバーでの共有：

```bash
streamlit run wordcloud_app.py --server.port 8501 --server.headless true
```

RenderやVPSでの外部公開については `docs/deploy.md` を参照（※必要なら追加します）

---

## 📄 ライセンス

MIT License

---

## 🙋‍♂️ 作者

- Okuda（@youichiokuda）
