import streamlit as st
from PIL import Image
from apps import home, danpane_divider, buzz_reservation

def main():
    logo = Image.open("image/logo.jpg")
    st.set_page_config(
        page_title="まるきゅうApp",
        page_icon=logo,
        layout="wide",
        menu_items={}
    )
    
    with st.sidebar:
        st.markdown("""
            # まるきゅうApp          
            [![Twitter](https://img.shields.io/badge/開発者Twitter-%40_nabex999-1DA1F2?logo=twitter&style=flat-square)](https://twitter.com/nabex999)
            [![Discord](https://img.shields.io/discord/1240489571821555763?logo=Discord&label=Discord&style=flat-square)](https://discord.gg/k9s64p8h)
            
            ---
        """)
    
    #st.title("まるきゅうApp")

    selected_page = st.sidebar.radio("App一覧", ["home", "ダンパネ分割", "BUZZ予約表"])

    if selected_page == "home":
        home.main()
    elif selected_page == "ダンパネ分割":
        danpane_divider.main()
    elif selected_page == "BUZZ予約表":
        buzz_reservation.main()
    else:
        pass

if __name__ == "__main__":
    main()