import streamlit as st
from PIL import Image
from apps import danpane_divider, buzz_reservation

def main():
    logo = Image.open("image/logo.jpg")
    st.set_page_config(
        page_title="まるきゅうApp",
        page_icon=logo,
        layout="wide",
        menu_items={}
    )

    selected_page = st.sidebar.radio("アプリ一覧", ["ホーム", "ダンパネ分割", "BUZZ予約表"])

    if selected_page == "ホーム":
        st.title("まるきゅうApp")
    elif selected_page == "ダンパネ分割":
        danpane_divider.main()
    elif selected_page == "BUZZ予約表":
        buzz_reservation.main()
    else:
        pass

if __name__ == "__main__":
    main()