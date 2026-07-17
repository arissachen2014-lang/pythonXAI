import streamlit as st
import random

# 1. 最頂端放標題
st.title("🎯 猜數字遊戲")

# 2. 初始化遊戲狀態 (使用 st.session_state 記住目前的狀態)
# 一開始隨機產生 1 ~ 100 的答案
if "answer" not in st.session_state:
    st.session_state.answer = random.randrange(1, 101)  # 1~100 (不包含101)
    st.session_state.min_val = 1
    st.session_state.max_val = 100
    st.session_state.feedback = ""      # 用來記錄提示文字（太大、太小、猜對了）
    st.session_state.game_over = False  # 紀錄遊戲是否結束

# 3. 接下來寫猜數字的範圍 (一開始顯示 1 - 100)
st.subheader(f"目前的範圍是：{st.session_state.min_val} - {st.session_state.max_val}")

# 4. 遊戲主邏輯（如果遊戲還沒結束就顯示輸入框）
if st.session_state.game_over == False:
    # 限制輸入範圍 min_value 與 max_value，並設定 step=1（只能輸入整數）
    guess = st.number_input(
        "請輸入你的答案：",
        step=1,
        min_value=st.session_state.min_val,
        max_value=st.session_state.max_val
    )
    
    # 確定送出的按鈕
    if st.button("確定送出", key="submit_btn"):
        if guess == st.session_state.answer:
            st.session_state.feedback = "你猜對了"
            st.session_state.game_over = True
        elif guess < st.session_state.answer:
            st.session_state.feedback = "太小了"
            # 依照你的規則：如果猜 60 且答案是 70，下限直接變成 60
            st.session_state.min_val = guess
        else:
            st.session_state.feedback = "太大了"
            # 如果猜太大，上限直接變成 guess
            st.session_state.max_val = guess
            
        # 點按鈕更新數值後，強制重新整理畫面，這樣最上方的範圍 subheader 就會立即改變
        st.rerun()

# 5. 猜錯或猜對的提示訊息，必須顯示在輸入答案的下方
if st.session_state.feedback != "":
    st.write(st.session_state.feedback)
    
    # 如果猜對了，就播放氣球特效！
    if st.session_state.game_over == True:
        st.balloons()

# 6. 如果猜對了，顯示重新開始按鈕
if st.session_state.game_over == True:
    if st.button("重新開始", key="reset_btn"):
        # 清除 session_state，讓整個遊戲回到初始狀態
        del st.session_state.answer
        del st.session_state.min_val
        del st.session_state.max_val
        del st.session_state.feedback
        del st.session_state.game_over
        st.rerun()