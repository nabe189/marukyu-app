import requests
from bs4 import BeautifulSoup
import streamlit as st
import pandas as pd

buzz_tokyo = [
    ['BUZZ赤坂', 'https://buzz-st.com/akasaka2'],
    ['BUZZ六本木', 'https://buzz-st.com/roppongi'],
    ['BUZZ BAYSIDE(浜松町)', 'https://buzz-st.com/bayside'],
    ['BUZZ池袋サンシャイン', 'https://buzz-st.com/ikebukuro7'],
    ['BUZZ池袋東口BASE', 'https://buzz-st.com/ikebukuro5'],
    ['BUZZ池袋本店', 'https://buzz-st.com/ikebukuro4'],
    ['BUZZ池袋西口タワー', 'https://buzz-st.com/ikebukuro3'],
    ['BUZZ池袋西口PARK', 'https://buzz-st.com/ikebukuro6'],
    ['BUZZ代々木', 'https://buzz-st.com/yoyogi'],
    ['BUZZ渋谷', 'https://buzz-st.com/shibuya'],
    ['BUZZ渋谷MARKCITY', 'https://buzz-st.com/shibuya4'],
    ['BUZZ渋谷東口SQUARE', 'https://buzz-st.com/shibuya3'],
    ['BUZZ渋谷PARK', 'https://buzz-st.com/shibuya2'],
    ['BUZZ渋谷宮下PARK', 'https://buzz-st.com/shibuya5'],
    ['BUZZ高田馬場', 'https://buzz-st.com/takadanobaba'],
    ['BUZZ高田馬場2丁目', 'https://buzz-st.com/takadanobaba2'],
    ['BUZZ新宿', 'https://buzz-st.com/shinjuku'],
    ['BUZZ新宿ハウス', 'https://buzz-st.com/shinjuku2'],
    ['BUZZ新宿4丁目', 'https://buzz-st.com/shinjuku3'],
    # ['BUZZ 新宿コンシェルジュ', 'https://buzz-st.com/shinjuku4'],
    ['BUZZ神田', 'https://buzz-st.com/kanda'],
    ['BUZZ秋葉原', 'https://buzz-st.com/akihabara'],
    ['BUZZ秋葉原駅前', 'https://buzz-st.com/akihabara2'],
    ['BUZZ上野', 'https://buzz-st.com/ueno2'],
    ['BUZZ日暮里', 'https://buzz-st.com/nippori'],
    ['BUZZ西日暮里', 'https://buzz-st.com/nishinippori'],
    ['BUZZ巣鴨', 'https://buzz-st.com/sugamo'],
    # ['BUZZ竹ノ塚', 'https://buzz-st.com/takenotsuka'],
    # ['BUZZ田無', 'https://buzz-st.com/tanashi'],
    # ['BUZZ八王子', 'https://buzz-st.com/hachioji'],
    # ['BUZZ国分寺', 'https://buzz-st.com/kokubunji'],
    # ['BUZZ西国分寺', 'https://buzz-st.com/nishikokubunji'],
    # ['BUZZ羽村', 'https://buzz-st.com/hamura'],
    # ['BUZZ esports 上野', 'https://buzz-st.com/esports-ueno'],
    # ['BUZZフィットネス大久保', 'https://buzz-st.com/fitness'],
    # ['BUZZ LABO', 'https://buzz-st.com/labo'],
    # ['BUZZ Live 赤坂', 'https://buzz-st.com/live-akasaka'],
    # ['バズスタ新宿', 'https://buzz-st.com/photo-shinjuku'],
    # ['バズスタ赤坂', 'https://buzz-st.com/photo-akasaka'],
    # ['バズスタライト神田', 'https://buzz-st.com/photo-kanda']
]


# 表を検索して各行を処理し、条件に応じてマークをつける
def get_reservation_state(table):
    marked_table = []
    rows = table.find_all('tr')
    for row in rows:
        marked_row = []
        cells = row.find_all('td')
        for cell in cells:
            button = cell.find('button')
            if button:
                button_class = button.get('class')
                # reserve_modal_trigger: ◯
                # studio_reserve_time_table_close: ×
                if 'studio_reserve_time_table_close' in button_class:
                    marked_row.append("×")
                elif 'reserve_modal_trigger' in button_class:
                    marked_row.append("◯")
            else:
                marked_row.append(cell.text.strip())
        marked_table.append(marked_row)
    return marked_table

def main():
    st.title("BUZZ予約表一覧")

    st.write("東京のBUZZスタジオの予約表一覧です。日付を入力するとのその日の空き状況が確認できます。5人ほどなら15～20㎡、10人なら25～30㎡、それ以上なら40㎡以上が広さの目安となります。")

    col1, col2, col3 = st.columns([2,1,1])
    with col1:
        selected_date = st.date_input("日付")
    
    time_list = ['6:00', '6:30', '7:00', '7:30', '8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30', '22:00', '22:30', '23:00', '23:30']
    with col2:
        start_time = st.selectbox("開始時刻", time_list, index=8)
    with col3:
        end_time = st.selectbox("終了時刻", time_list, index=14)

    selected_time = time_list[time_list.index(start_time):time_list.index(end_time)]

    if st.button("予約表一覧を取得する"):
        for studio_name, studio_url in buzz_tokyo:
            table_url = f'{studio_url}/{selected_date}#time_table'
            response = requests.get(table_url)
            soup = BeautifulSoup(response.text, "html.parser")

            # スタジオ名/アクセスの表示
            st.markdown(f"[{studio_name}]({table_url}): {soup.find(class_='top_info_catch').text}")

            # 予約表の一覧
            table = soup.find('table', class_="studio_all_reserve_time_table")
            table_columns = ['Time'] + [div.text for div in table.find_all('div', class_="studio_reserve_time_table_studio_name")]
            reservation_state = get_reservation_state(table)
            reservation_table = pd.DataFrame(reservation_state, columns=table_columns).set_index('Time').T[selected_time]
            st.write(reservation_table)
            
            # 部屋のスペック
            room_names = []
            all_specs = []
            for room in soup.find_all(class_='studio_item'):
                room_name = room.find(class_='studio_title').text.replace(' ', '')
                spec = room.find(class_='studio_spec').find('span').text.split()[1]
                room_names.append(room_name)
                all_specs.append(spec)
            spec_table = pd.DataFrame(all_specs, index=room_names, columns=['広さ']).T
            st.write(spec_table)