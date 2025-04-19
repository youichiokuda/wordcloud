
import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# タイトル
st.title("DX課題ワードクラウド")

# テキスト入力（初期値あり）
text_data = st.text_area("ワードクラウドに使うテキストを入力してください", """
紙ベース 紙ベース 紙ベース 電子化 電子化 現場理解 段階導入 スマホ QRコード 非接触 予約システム 一部電子化
バックヤード バックヤード バックヤード デジタル化 デジタル化 物品管理 勤怠管理 手作業 棚卸し 業務フロー最適化 成功事例 成功事例
推進体制不在 推進体制不在 総務課兼任 旗振り役不在 調整負担 スピード感不足 定例会 定例会 情報整理 資料作成 Webアンケート Webアンケート
現場の声 現場の声 見える化 見える化 課題不明 KPI ゴール モニタリング モニタリング 合意形成 可視化レポート
導入タイミング 導入タイミング ステップ設計 小さく始める 柔軟提案 相談ベース 選択肢提示 選択肢提示
""", height=300)

# フォントパス（社内環境に合わせて調整）
font_path = "NotoSerifJP-Bold.ttf"

# 生成ボタン
if st.button("ワードクラウド生成"):
    if text_data.strip():
        wordcloud = WordCloud(
            font_path=font_path,
            width=800,
            height=400,
            background_color="white",
            collocations=False
        ).generate(text_data)

        # プロット表示
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis("off")
        st.pyplot(fig)
    else:
        st.warning("テキストを入力してください。")
