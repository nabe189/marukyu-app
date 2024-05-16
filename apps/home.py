import streamlit as st
import os

def main():
    st.markdown("# まるきゅうAppへようこそ！")
    st.markdown("当サイトはnabe([@nabex999](https://twitter.com/nabex999))が個人で運用しているまるきゅうProjectお役立ちツールのまとめサイトになります。ご意見等ありましたら気兼ねなくコンタクトしてください。")
    
    st.markdown("## ツール一覧")
    st.markdown("---")

    st.markdown("### ダンパネ分割")
    st.write("ダンパネ作成のために画像ファイルを任意のA4枚数で分割する")
    with st.expander("使い方"):
        st.write("※A4でポスター印刷することを想定")
        st.write("このような画面が出てくるので必要な情報をインプット")
        st.image("image/danpane_01.png")
        st.write("そうするとプレビューが出てくる(プレビュー後もNumber of Columns/Rowsは調整可)")
        st.image("image/danpane_02.png")
        st.write("「Generate Zip」「Generate PDF」をクリックすると「Download Zip」「Download PDF」というボタンが現れる。これをクリックすると、プレビュー通りに分割された画像がまとまったファイルがダウンロードされる。PDFファイルがおすすめ。")
        st.write("「Direction」をhorizontalにすると画像が90°回転される")
        st.image("image/danpane_03.png")
        st.write("⚠️注意：印刷プレビューを確認してから印刷するようにするのがおすすめです。")

    st.markdown("### BUZZ予約表一覧")
    st.write("都内BUZZの予約状況を一覧で取得する")
    with st.expander("使い方"):
        st.write("日付を入力して「予約表一覧を取得する」を押す")
        st.write("すると該当日の全スタジオの予約表をスクレイピングで取得した結果が表示される")
        st.image("image/buzz_01.png")
