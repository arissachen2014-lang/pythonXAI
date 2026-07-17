import streamlit as st
import os

# --- 1. 初始化資料與狀態 ---
# 使用字典 (dict) 來管理所有商品的資訊
# 商品順序：apple -> banana -> bg -> orange
if "products" not in st.session_state:
    st.session_state.products = {
        "apple": {
            "name": "Apple",
            "image": "image/apple.png",
            "price": 10,
            "stock": 10
        },
        "banana": {
            "name": "Banana",
            "image": "image/banana.png",
            "price": 10,
            "stock": 10
        },
        "bg": {
            "name": "BG",
            "image": "image/bg.png",
            "price": 10,
            "stock": 10
        },
        "orange": {
            "name": "Orange",
            "image": "image/orange.png",
            "price": 10,
            "stock": 10
        }
    }

st.title("🍎 網頁版購物平台")

# --- 2. 第一行：控制顯示的欄位數量 ---
# 起始數是 1，每次加 1，最多是 4 個欄位
num_columns = st.number_input(
    "請輸入顯示欄位數：", 
    min_value=1, 
    max_value=4, 
    value=1, 
    step=1
)

# 將商品的 key 轉換成 list，方便依索引存取
product_keys = list(st.session_state.products.keys())

# --- 3. 商品展示區 ---
# 根據使用者輸入的欄位數量，動態建立 columns
cols = st.columns(num_columns)

# 依據設定的欄位數量，逐一放入對應的商品
for i in range(num_columns):
    # 取得當前欄位對應的商品 key
    p_key = product_keys[i]
    p_info = st.session_state.products[p_key]
    
    with cols[i]:
        # 1. 顯示圖片
        # 注意：請確保你的專案目錄下有 image/ 資料夾，且內含對應的圖片檔
        if os.path.exists(p_info["image"]):
            st.image(p_info["image"], use_container_width=True)
        else:
            # 沒找到圖片時的替代顯示
            st.warning(f"找不到 {p_info['image']}")
            
        # 2. 顯示商品名稱
        st.subheader(p_info["name"])
        
        # 3. 顯示價格
        st.write(f"價格：{p_info['price']} 元")
        
        # 4. 顯示庫存量
        st.write(f"庫存：{p_info['stock']}")
        
        # 5. 購買按鈕：點下去該商品庫存少 1
        if st.button(f"購買 {p_info['name']}", key=f"buy_{p_key}"):
            if p_info["stock"] > 0:
                p_info["stock"] -= 1
                st.success(f"成功購買 {p_info['name']}！")
                st.rerun()  # 立即重整畫面，更新上下的庫存數據
            else:
                st.error(f"{p_info['name']} 已經沒有庫存了！")

st.write("---")

# --- 4. 新增商品庫存區 ---
st.subheader("➕ 新增商品庫存")

# 第一行：左邊選擇商品，右邊新增商品數量
col_select, col_add = st.columns(2)

with col_select:
    # 選擇商品的下拉選單（包含四個商品選項）
    selected_name = st.selectbox(
        "選擇商品：", 
        options=["Apple", "Banana", "BG", "Orange"]
    )

with col_add:
    # 新增數量：起始值為 1，每次加 1，無上限 (max_value=None)
    add_qty = st.number_input(
        "新增商品的數量：", 
        min_value=1, 
        step=1, 
        value=1
    )

# 執行新增庫存的按鈕
if st.button("確認新增庫存", key="btn_add_stock"):
    # 根據選擇的名稱找到對應的 key (轉為小寫即可對應字典 key)
    selected_key = selected_name.lower()
    st.session_state.products[selected_key]["stock"] += add_qty
    st.success(f"成功將 {selected_name} 庫存增加 {add_qty} 個！")
    st.rerun()

st.write("---")

# --- 5. 目前商品庫存清單 ---
st.subheader("📊 目前商品庫存")

# 建立 4 個欄位並排顯示所有商品的即時庫存資訊
stock_cols = st.columns(4)
for idx, key in enumerate(product_keys):
    p_info = st.session_state.products[key]
    with stock_cols[idx]:
        st.metric(label=p_info["name"], value=f"{p_info['stock']} 個")