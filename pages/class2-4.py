import streamlit as st
a = st.number_input("請輸入一個數字:", step=1, min_value=1, max_value=9)
for i in range (a+1):
    st.write("數字金字塔:",str(i)*i)