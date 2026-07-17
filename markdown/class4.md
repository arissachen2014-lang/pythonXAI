# Python 上課重點筆記（國小版）

---

# 第 1 部分：Streamlit 網頁程式

## 1. 載入套件

```python
import streamlit as st
import time
import random
```

### 功能

- `streamlit`：做網頁程式。
- `time`：可以讓程式等待幾秒鐘。
- `random`：可以隨機產生數字。

---

## 2. 按鈕

```python
st.button("按鈕名稱")
```

例如：

```python
if st.button("重新整理"):
```

按下按鈕才會執行下面的程式。

---

## 3. 顯示訊息

```python
st.success("完成！")
```

會出現綠色成功訊息。

其他常用：

```python
st.write("文字")
st.title("大標題")
st.subheader("小標題")
```

---

## 4. 等待時間

```python
time.sleep(3)
```

表示：

👉 等待 3 秒。

---

## 5. 重新整理畫面

```python
st.rerun()
```

功能：

重新執行整個程式，畫面會更新。

---

## 6. session_state（記住資料）

```python
st.session_state
```

用途：

讓資料重新整理後還會保留。

例如：

```python
st.session_state.x = []
```

建立一個購物籃。

加入商品：

```python
st.session_state.x.append(a)
```

刪除商品：

```python
st.session_state.x.pop(idx)
```

---

## 7. 輸入資料

文字輸入：

```python
st.text_input("請輸入餐點")
```

數字輸入：

```python
st.number_input("請輸入數字")
```

可以限制：

- 最小值
- 最大值
- 一次增加多少

例如：

```python
step=1
min_value=1
max_value=100
```

---

## 8. 分欄

```python
st.columns([1,2])
```

可以把畫面分成兩欄。

例如：

左邊放輸入框，右邊放按鈕。

---

## 9. 氣球動畫

```python
st.balloons()
```

猜對答案時放煙火（氣球）。

---

# 第 2 部分：算術指定運算子

這些都是把結果再存回原本的變數。

| 寫法  | 意思     |
| ----- | -------- |
| `+=`  | 加上     |
| `-=`  | 減掉     |
| `*=`  | 乘       |
| `/=`  | 除       |
| `//=` | 整數除法 |
| `%=`  | 取餘數   |
| `**=` | 次方     |

例如：

```python
a = 5
a += 2
```

等於

```python
a = a + 2
```

結果：

```
7
```

---

# 第 3 部分：運算順序

Python 會照下面順序計算：

1. `()` 括號
2. `**` 次方
3. `* / // %`
4. `+ -`
5. `== != > < >= <=`
6. `not`
7. `and`
8. `or`
9. `= += -= *= ...`

先做前面的，再做後面的。

---

# 第 4 部分：while 迴圈

格式：

```python
while 條件:
    程式
```

意思：

只要條件是真的，就一直重複。

例如：

```python
i = 0

while i < 5:
    print(i)
    i += 1
```

輸出：

```
0
1
2
3
4
```

---

# 第 5 部分：break

```python
break
```

功能：

立刻離開目前的迴圈。

例如：

```python
for i in range(5):
    if i == 3:
        break
```

結果：

```
0
1
2
3
```

到 3 就停止。

---

# 第 6 部分：random 隨機數

先匯入：

```python
import random
```

產生亂數：

```python
random.randrange(7)
```

得到：

```
0～6
```

也可以：

```python
random.randrange(1,7)
```

得到：

```
1～6
```

每次執行都可能不同。

---

# 第 7 部分：猜數字遊戲

這次學到很多以前的內容一起使用：

✅ `random`（產生答案）

✅ `session_state`（記住答案）

✅ `number_input`（輸入數字）

✅ `button`（送出答案）

✅ `if`（判斷大小）

✅ `rerun()`（更新畫面）

✅ `balloons()`（猜對放氣球）

遊戲流程：

```
開始
 ↓
隨機產生答案
 ↓
玩家輸入數字
 ↓
按下送出
 ↓
判斷大小
 ↓
更新範圍
 ↓
猜對
 ↓
放氣球
 ↓
重新開始
```

---

# 第 8 部分：字典（Dictionary）

字典是一種儲存資料的方法。

格式：

```python
{
鍵(Key):值(Value)
}
```

例如：

```python
d = {
    "a":1,
    "b":2,
    "c":3
}
```

就像：

| Key | Value |
| --- | ----- |
| a   | 1     |
| b   | 2     |
| c   | 3     |

---

## 取得 Key

```python
d.keys()
```

得到：

```
a
b
c
```

---

## 取得 Value

```python
d.values()
```

得到：

```
1
2
3
```

---

## 同時取得 Key 和 Value

```python
d.items()
```

可以一起取得：

```
a 1
b 2
c 3
```

---

## 新增資料

```python
d["d"] = 4
```

變成：

```
a 1
b 2
c 3
d 4
```

---

## 修改資料

```python
d["a"] = 5
```

原本：

```
a = 1
```

變成：

```
a = 5
```

---

## 刪除資料

```python
d.pop("a")
```

把 `"a"` 刪掉。

---

## 檢查有沒有某個 Key

```python
"a" in d
```

結果：

```
True
```

表示有。

如果沒有：

```python
"e" in d
```

結果：

```
False
```

---

# 第 9 部分：巢狀字典（字典裡面還有字典）

例如：

```python
grade = {
    "小明":{
        "國文":[90,80,70],
        "數學":[85,75,65]
    }
}
```

代表：

```
學生
 ↓
科目
 ↓
成績
```

取得數學成績：

```python
grade["小明"]["數學"]
```

結果：

```
[85,75,65]
```

取得第一次英文：

```python
grade["小美"]["英文"][0]
```

結果：

```
93
```

---

# 第 10 部分：計算平均

利用：

```python
sum()
```

把全部加起來。

利用：

```python
len()
```

算有幾個資料。

平均：

```python
平均 = sum(成績) / len(成績)
```

例如：

```python
scores = [90,80,70]

avg = sum(scores)/len(scores)
```

得到：

```
80
```

---

# 第 11 部分：len()

```python
len()
```

功能：

算資料有多少個。

例如：

```python
len([1,2,3])
```

結果：

```
3
```

字典：

```python
len(avg_grade)
```

結果：

```
3
```

因為有三個科目：

- 國文
- 數學
- 英文

---

# ⭐ 今天學到的重要指令整理

| 指令                 | 功能              |
| -------------------- | ----------------- |
| `import`             | 匯入套件          |
| `st.title()`         | 標題              |
| `st.write()`         | 顯示文字          |
| `st.button()`        | 按鈕              |
| `st.text_input()`    | 文字輸入          |
| `st.number_input()`  | 數字輸入          |
| `st.success()`       | 成功訊息          |
| `st.columns()`       | 分欄              |
| `st.session_state`   | 記住資料          |
| `st.rerun()`         | 重新整理畫面      |
| `st.balloons()`      | 播放氣球動畫      |
| `time.sleep()`       | 等待幾秒          |
| `random.randrange()` | 隨機產生數字      |
| `while`              | 條件迴圈          |
| `break`              | 跳出迴圈          |
| `+=`、`-=` 等        | 快速運算          |
| `dict`               | 字典              |
| `keys()`             | 取得所有 Key      |
| `values()`           | 取得所有 Value    |
| `items()`            | 取得 Key 和 Value |
| `pop()`              | 刪除資料          |
| `sum()`              | 全部加總          |
| `len()`              | 計算資料數量      |
| `in`                 | 檢查資料是否存在  |

---
