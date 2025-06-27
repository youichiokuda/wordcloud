import streamlit as st
import requests
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Flask課金APIのURL
API_BASE = "https://billing-api-tyez.onrender.com"

st.set_page_config(page_title="DX課題ワードクラウド", layout="wide")
st.title("DX課題ワードクラウド（有料版）")

# 🔐 Clerkトークンの入力
token = st.text_input("Clerkトークンを入力してください", type="password")
if not token:
    st.stop()

# 🔎 課金チェックAPI呼び出し
res = requests.get(f"{API_BASE}/check-access", headers={"Authorization": f"Bearer {token}"})
if not res.ok or not res.json().get("has_access"):
    st.error("アクセスが許可されていません。")
    if st.button("💳 サブスクリプション登録"):
        checkout = requests.post(
            f"{API_BASE}/create-checkout-session",
            headers={"Authorization": f"Bearer {token}"},
            json={"type": "subscription"}
        )
        if checkout.ok:
            checkout_url = checkout.json().get("url")
            st.markdown(f"[➡️ Stripeで登録する]({checkout_url})", unsafe_allow_html=True)
        else:
            st.error("Stripeセッションの作成に失敗しました。")
    st.stop()

# ✅ ワードクラウド生成UI
st.success("✅ アクセス認証成功！")

text_data = st.text_area("ワードクラウドに使うテキストを入力してください", """
紙ベース 紙ベース 紙ベース 電子化 電子化 現場理解 段階導入 スマホ QRコード 非接触 予約システム 一部電子化
バックヤード バックヤード バックヤード デジタル化 デジタル化 物品管理 勤怠管理 手作業 棚卸し 業務フロー最適化 成功事例 成功事例
推進体制不在 推進体制不在 総務課兼任 旗振り役不在 調整負担 スピード感不足 定例会 定例会 情報整理 資料作成 Webアンケート Webアンケート
現場の声 現場の声 見える化 見える化 課題不明 KPI ゴール モニタリング モニタリング 合意形成 可視化レポート
導入タイミング 導入タイミング ステップ設計 小さく始める 柔軟提案 相談ベース 選択肢提示 選択肢提示
""", height=300)

font_path = "NotoSerifJP-Bold.ttf"

if st.button("ワードクラウド生成"):
    if text_data.strip():
        wordcloud = WordCloud(
            font_path=font_path,
            width=800,
            height=400,
            background_color="white",
            collocations=False
        ).generate(text_data)

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis("off")
        st.pyplot(fig)
    else:
        st.warning("テキストを入力してください。")
