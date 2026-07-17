


import streamlit as st
import time

if st.button("重新整理", key="button1"):  # 如果按鈕被按下
    st.success("準備重新整理")  # 顯示綠色訊息
    time.sleep(3)  # 等待3秒
    st.rerun()  # 重新整理整個頁面

if "x" not in st.session_state:
    st.session_state.x = []  # 如果session_state中沒有x，則初始化為空列表

st.title("點餐機")
col1, col2 = st.columns([1,2])
with col1:
    a=st.text_input("請輸入餐點:")

with col2:
    if st.button("加入", key="button2"):
        st.session_state.x.append(a)  
        st.rerun()  # 加入後立即重新整理以更新畫面
st.write("購物籃")
# 顯示購物籃商品與專屬刪除按鈕
# 我們用 enumerate 取得商品的索引 (idx) 與名稱 (item)
for idx, item in enumerate(st.session_state.x):
    # 建立兩欄，左邊放商品名稱，右邊放刪除按鈕
    item_col, btn_col = st.columns([4, 1])
    
    with item_col:
        st.write(item)  # 這裡直接顯示 item，不加上點點 "•"
        
    with btn_col:
        # 使用 f"delete_{idx}" 作為唯一的 key，避免重複
        if st.button("刪除", key=f"delete_{idx}"):
            st.session_state.x.pop(idx)  # 移出該索引的商品
            st.rerun()  # 刪除後立即重新整理以更新畫面            