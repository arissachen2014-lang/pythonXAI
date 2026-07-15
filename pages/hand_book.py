import streamlit as st
with st.expander("class 1 課堂筆記"):
    st.write(
        """
# Python 入門筆記（國小版）

## 🐍 什麼是 Python？

Python 是一種程式語言，可以讓電腦照著我們寫的指令做事情，例如：

- 顯示文字
- 計算數學
- 做小遊戲
- 製作網站
- 製作 AI 程式

---

# 1. print()：顯示文字

`print()` 是最常用的指令，可以把內容顯示在畫面上。

```python
print("Hello World!")
print("Arissa")
```

畫面會顯示：

```
Hello World!
Arissa
```

### 換行

`\n` 可以讓文字換到下一行。

```python
print("不要低頭\n雙下巴會出來")
```

結果：

```
不要低頭
雙下巴會出來
```

---

# 2. 註解（給自己看的說明）

## 單行註解

用 `#`

```python
# 這是註解
print("Hello")
```

## 多行註解

用三個雙引號

```python
\"""
第一行
第二行
第三行
\"""
```

💡 註解不會被電腦執行，只是方便自己閱讀。

---

# 3. Python 的基本資料型態

Python 有很多種類的資料。

| 型態  | 名稱           | 範例        |
| ----- | -------------- | ----------- |
| int   | 整數           | 1、5、100   |
| float | 小數           | 3.14、1.5   |
| str   | 字串（文字）   | "apple"     |
| bool  | 布林值（真假） | True、False |

例如：

```python
print(10)
print(3.14)
print("apple")
print(True)
```

---

# 4. 變數（像一個盒子）

變數就像一個有名字的盒子，可以把資料放進去。

```python
a = 10
print(a)
```

畫面：

```
10
```

也可以改變內容。

```python
a = "apple"
print(a)
```

畫面：

```
apple
```

---

# 5. 數學運算

| 符號 | 功能     | 範例     |
| ---- | -------- | -------- |
| +    | 加法     | 3+2=5    |
| -    | 減法     | 5-2=3    |
| \*   | 乘法     | 3\*4=12  |
| /    | 除法     | 8/2=4    |
| //   | 取整數商 | 9//2=4   |
| %    | 取餘數   | 9%2=1    |
| \*\* | 次方     | 2\*\*3=8 |

例如：

```python
print(2+3)
print(10%3)
print(2**4)
```

---

# 6. 運算順序

跟數學一樣有先後順序。

1. ()
2. \*\*
3. - / // %
4. - -

例如：

```python
print((3+2)*5)
```

---

# 7. 字串運算

## 字串相加

```python
print("apple"+"pen")
```

結果：

```
applepen
```

---

## 字串重複

```python
print("apple "*3)
```

結果：

```
apple apple apple
```

---

# 8. f-string（把變數放進文字）

```python
name = "Apple"
age = 18

print(f"Hello, my name is {name}, I'm {age} years old.")
```

結果：

```
Hello, my name is Apple, I'm 18 years old.
```

只要把變數放進 `{ }` 就可以。

---

# 9. len()：計算長度

可以計算文字有幾個字。

```python
print(len("apple"))
```

結果：

```
5
```

---

# 10. type()：查看資料種類

可以知道資料是哪一種型態。

```python
print(type(1))
print(type(3.14))
print(type("apple"))
print(type(True))
```

結果：

```
int
float
str
bool
```

---

# 11. 型態轉換

有時候可以把資料變成另一種型態。

```python
int(3.14)
```

變成：

```
3
```

其他常用：

```python
float(5)
str(100)
bool(1)
```

### 注意！

下面這個會錯誤：

```python
int("hello")
```

因為 `"hello"` 不是數字。

---

# 12. input()：讓使用者輸入資料

```python
name = input("請輸入名字：")
```

使用者輸入：

```
Arissa
```

變數 `name` 就會存成：

```
Arissa
```

如果要輸入數字，要加上 `int()` 或 `float()`。

例如：

```python
age = int(input("請輸入年齡："))
```

或

```python
score = float(input("請輸入分數："))
```

---

# 13. 小練習：計算圓面積

公式：

> 圓面積 = π × 半徑²

```python
r = float(input("請輸入半徑："))
print(f"圓面積為：{3.14*r**2}")
```

---

# 14. 小練習：計算平均分數

```python
mid = float(input("請輸入期中成績："))
final = float(input("請輸入期末成績："))

print(f"平均為：{(mid+final)/2}")
```

---

# 15. Streamlit（做網頁）

先匯入 Streamlit：

```python
import streamlit as st
```

`st` 是 Streamlit 的簡稱。

---

## (1) 標題

```python
st.title("這是標題")
```

會顯示大大的標題。

---

## (2) st.write()

最常用，可以顯示：

- 文字
- 數字
- 表格
- Markdown

```python
st.write("Hello")
```

---

## (3) st.text()

只能顯示純文字。

```python
st.text("Hello")
```

---

## (4) st.markdown()

可以使用 Markdown 排版。

例如：

```python
st.markdown(\"""
# 第一級標題

## 第二級標題

### 第三級標題

- 蘋果
- 香蕉
- 西瓜

**粗體**

*斜體*

---
\""")
```

可以做出：

- 大標題
- 小標題
- 項目符號
- 粗體
- 斜體
- 分隔線
- 程式碼區塊

---

# 🌟 今天學到的重點整理

✅ `print()`：把內容顯示在畫面上。
✅ `#`、`""" """`：寫註解，不會被執行。
✅ 四種基本資料型態：`int`、`float`、`str`、`bool`。
✅ 變數：用來存放資料，例如 `a = 10`。
✅ 數學運算：`+`、`-`、`*`、`/`、`//`、`%`、`**`。
✅ 字串可以用 `+` 連接、`*` 重複。
✅ `f"..."` 可以把變數放進文字裡。
✅ `len()` 計算文字長度。
✅ `type()` 查看資料型態。
✅ `int()`、`float()`、`str()`、`bool()` 可以轉換資料型態。
✅ `input()` 可以讓使用者輸入資料。
✅ 可以利用輸入的數字做計算，例如圓面積和平均分數。
✅ `Streamlit` 可以把 Python 程式做成簡單的網頁，常用的有 `st.title()`、`st.write()`、`st.text()` 和 `st.markdown()`。

---

## 🎯 小提醒

1. 字串一定要加引號，例如 `"Hello"`。
2. 數字不用加引號，例如 `123`。
3. 想輸入數字時，記得用 `int()` 或 `float()` 轉換。

"""
    )
with st.expander("class 2 課堂筆記"):
    st.write(
        """
# 🐍 Python 入門筆記（二）── 判斷、按鈕與迴圈（國小版）

這次學到的內容，可以讓程式**自己做判斷、重複工作**，還能做出**可以按按鈕的網頁**！

---

# 第一章：比較運算子（比較大小）

比較運算子可以比較兩個資料，結果只有兩種：

* `True`（正確、是真的）
* `False`（錯誤、是假的）

| 運算子  | 意思   | 範例     | 結果    |
| ---- | ---- | ------ | ----- |
| `==` | 等於   | `3==3` | True  |
| `!=` | 不等於  | `3!=3` | False |
| `>`  | 大於   | `5>3`  | True  |
| `<`  | 小於   | `2<1`  | False |
| `>=` | 大於等於 | `5>=5` | True  |
| `<=` | 小於等於 | `3<=5` | True  |

例如：

```python
print(5==5)
print(5>8)
print(7!=3)
```

輸出：

```
True
False
True
```

---

# 第二章：邏輯運算子

有時候一個判斷還不夠，可以把很多條件放在一起。

## 1️⃣ and（而且）

兩個條件**都要成立**，結果才會是 True。

| 第一個   | 第二個   | 結果    |
| ----- | ----- | ----- |
| True  | True  | True  |
| True  | False | False |
| False | True  | False |
| False | False | False |

例如：

```python
print(5>3 and 10>8)
```

結果：

```
True
```

---

## 2️⃣ or（或者）

只要**有一個條件成立**，就是 True。

例如：

```python
print(5>10 or 3<8)
```

結果：

```
True
```

---

## 3️⃣ not（不是）

把 True 變 False，把 False 變 True。

例如：

```python
print(not True)
print(not False)
```

結果：

```
False
True
```

---

# 第三章：運算順序

Python 會照下面的順序計算：

1. `( )` 括號
2. `**` 次方
3. `* / // %`
4. `+ -`
5. 比較運算子（`== != > < >= <=`）
6. `not`
7. `and`
8. `or`

💡 如果不確定，可以多加括號 `( )`，程式會更容易閱讀。

---

# 第四章：if 判斷式

`if` 可以讓程式自己做決定。

例如：

```python
score = 90

if score >= 60:
    print("及格")
```

如果條件成立，就會執行下面的程式。

---

## if、elif、else

如果有很多種情況，可以使用：

```python
if 條件:
    做事情

elif 另一個條件:
    做事情

else:
    其他情況
```

例如密碼檢查：

```python
password = input("請輸入密碼：")

if password == "1234":
    print("歡迎 Jeffery")

elif password == "5678":
    print("歡迎 Tim")

elif password == "0000":
    print("歡迎 Chloe")

else:
    print("密碼錯誤")
```

程式會依序檢查：

* 第一個條件
* 第二個條件
* 第三個條件
* 如果都不是，就執行 `else`。

---

## if 和 elif 的差別

### 使用 if、elif

✔ 找到符合的條件後，就不會再往下檢查，所以速度比較快。

例如：

```
if
 ↓
符合 ✔
停止檢查
```

---

### 使用很多個 if

每一個 if 都會檢查一次。

```
if
 ↓
if
 ↓
if
 ↓
全部都檢查
```

所以當條件很多時，通常使用 **if + elif + else** 比較好。

---

# 第五章：Streamlit 數字輸入

可以讓使用者在網頁輸入數字。

```python
number = st.number_input(
    "請輸入一個數字",
    step=1,
    min_value=0,
    max_value=100
)
```

參數說明：

| 參數        | 功能     |
| --------- | ------ |
| step      | 每次增加多少 |
| min_value | 最小值    |
| max_value | 最大值    |

例如：

只能輸入 **0～100 的整數**。

---

# 第六章：顯示輸入的資料

```python
st.markdown(f"你輸入的數字是：{number}")
```

會在網頁顯示：

```
你輸入的數字是：50
```

---

# 第七章：成績判斷

利用 if 判斷成績。

```python
if n>=90:
    A

elif 80<=n<90:
    B

elif 70<=n<80:
    C

elif 60<=n<70:
    D

else:
    F
```

例如：

| 分數 | 等級 |
| -- | -- |
| 95 | A  |
| 88 | B  |
| 76 | C  |
| 61 | D  |
| 40 | F  |

---

# 第八章：按鈕（Button）

可以在網頁放按鈕。

```python
st.button("按我一下")
```

畫面會出現一個按鈕。

---

## 判斷有沒有按下按鈕

```python
if st.button("按我"):
    print("你按下去了")
```

只有按下按鈕時，程式才會執行。

---

## balloons（氣球）

```python
if st.button("放氣球"):
    st.balloons()
```

按下按鈕後，畫面會出現很多🎈。

---

## snow（下雪）

```python
if st.button("下雪"):
    st.snow()
```

按下按鈕後，畫面會出現❄️。

---

## key 的用途

如果有很多按鈕，要給每個按鈕不同名字。

例如：

```python
st.button("按我", key="button1")
```

這樣 Python 才知道是哪一個按鈕。

---

# 第九章：for 迴圈

有時候想做很多次相同的事情，就可以使用 **for 迴圈**。

例如：

```python
for i in range(5):
    print(i)
```

輸出：

```
0
1
2
3
4
```

總共做了 **5 次**。

---

# 第十章：range()

`range()` 可以產生一串數字。

## ① range(5)

```python
range(5)
```

會產生：

```
0
1
2
3
4
```

⚠ 不包含 5。

---

## ② range(1,5)

```python
range(1,5)
```

會產生：

```
1
2
3
4
```

也是不包含 5。

---

## ③ range(1,10,2)

第三個數字代表每次增加多少。

```python
range(1,10,2)
```

會得到：

```
1
3
5
7
9
```

每次加 2。

---

# 第十一章：迴圈變數

例如：

```python
for i in range(5):
    print(i)
```

`i` 會依序變成：

```
0
1
2
3
4
```

每做一次迴圈，就會換成下一個數字。

---

# 第十二章：迴圈中的計算

例如：

```python
for i in range(5):
    a = i * 2

print(a)
```

每一次都會重新計算：

| i | a=i×2 |
| - | ----- |
| 0 | 0     |
| 1 | 2     |
| 2 | 4     |
| 3 | 6     |
| 4 | 8     |

因為最後一次 `i=4`，

所以最後印出的是：

```
8
```

---

# 🌟 本次重點整理

✅ **比較運算子**：比較兩個資料，結果只有 `True` 或 `False`。
✅ **and**：全部都成立才是 True。
✅ **or**：只要有一個成立就是 True。
✅ **not**：把 True 和 False 相反。
✅ **if**：判斷條件是否成立。
✅ **elif**：檢查其他可能的條件。
✅ **else**：前面的條件都不符合時執行。
✅ **Streamlit** 的 `st.number_input()` 可以輸入數字。
✅ **st.button()** 可以建立按鈕。
✅ **st.balloons()** 可以放氣球動畫。
✅ **st.snow()** 可以播放下雪動畫。
✅ **for 迴圈** 可以重複做同一件事情。
✅ **range()** 可以產生一串數字，**結束值不會包含在內**。

---

# 💡 學習小提醒

1. `==` 是「比較是否相等」，`=` 是「把資料存進變數」，兩個意思不一樣。
2. `if`、`elif`、`else` 後面都要加冒號 `:`。
3. `for` 迴圈中的程式要記得縮排，Python 才知道哪些程式屬於迴圈。
4. `range()` 的最後一個數字**不會被包含**，這是很多初學者最容易忘記的地方。
"""
    )