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
with st.expander("class 3 課堂筆記"):
    st.write(
        """
# 🐍 Python 入門筆記（三）

## List（串列）、金字塔、Streamlit 排版與 Session State（國小版）

這次學到的內容，可以讓程式**記住很多資料、做出漂亮的網頁排版，還能記住按鈕按了幾次！**

---

# 第一章：數字金字塔

可以利用 **for 迴圈** 重複顯示文字。

```python
a = st.number_input("請輸入一個數字:", step=1, min_value=1, max_value=9)

for i in range(a+1):
    st.write(str(i) * i)
```

如果輸入 **5**

畫面會顯示：

```
1
22
333
4444
55555
```

## 💡 重點

```python
str(i) * i
```

代表：

把數字變成文字，再重複很多次。

例如：

```python
str(3) * 3
```

結果：

```
333
```

---

# 第二章：List（串列）

## List 是什麼？

List（串列）就像一個**可以放很多東西的盒子**。

可以放：

* 數字
* 文字
* True、False
* 甚至另一個 List

例如：

```python
[]
```

空的 List。

```python
[1,2,3]
```

有三個數字。

```python
["蘋果","香蕉","西瓜"]
```

放三個水果。

也可以混合：

```python
[1, True, "apple", 3.14]
```

---

# 第三章：讀取 List 裡面的資料

例如：

```python
L = [1,2,3,"a","b","c"]
```

每個資料都有自己的位置（Index）。

| Index | 資料  |
| ----- | --- |
| 0     | 1   |
| 1     | 2   |
| 2     | 3   |
| 3     | "a" |
| 4     | "b" |
| 5     | "c" |

取得資料：

```python
print(L[0])
```

結果：

```
1
```

取得第四個資料：

```python
print(L[3])
```

結果：

```
a
```

💡 **Index 永遠從 0 開始，不是從 1。**

---

# 第四章：List 切片（Slice）

切片就是一次取很多資料。

## 1️⃣ 全部每隔兩個取一次

```python
L[::2]
```

結果：

```
[1,3,'b']
```

---

## 2️⃣ 從第1個取到第3個（不包含4）

```python
L[1:4]
```

結果：

```
[2,3,'a']
```

---

## 3️⃣ 每隔兩個取一次

```python
L[1:4:2]
```

結果：

```
[2,'a']
```

### 切片格式

```
List[開始:結束:間隔]
```

和 `range()` 很像。

---

# 第五章：append()

append 可以在最後面新增資料。

例如：

```python
L=[1,2,3]

L.append(4)
```

變成：

```
[1,2,3,4]
```

💡 append 永遠加在最後面。

---

# 第六章：remove()

remove 可以刪除指定內容。

例如：

```python
L=["a","b","c","a"]

L.remove("a")
```

結果：

```
["b","c","a"]
```

只會刪掉第一個找到的 `"a"`。

---

如果想全部刪掉，可以配合迴圈。

---

# 第七章：pop()

pop 是按照位置(Index)刪除。

例如：

```python
L=["a","b","c","d"]

L.pop(1)
```

結果：

```
["a","c","d"]
```

因為 index=1 是 `"b"`。

如果沒有寫數字：

```python
L.pop()
```

就會刪掉最後一個。

---

# 第八章：sort()

可以把資料排序。

```python
L=[3,1,5,2]

L.sort()
```

結果：

```
[1,2,3,5]
```

由小排到大。

⚠ 注意：

sort() 會直接修改原本的 List。

---

# 第九章：Streamlit Columns（欄位）

Columns 可以讓網頁分成很多欄。

例如：

```python
col1,col2 = st.columns(2)
```

畫面：

```
| 左邊 | 右邊 |
```

---

## 不同寬度

```python
st.columns([1,2])
```

代表：

```
| 小 |     大     |
```

第二欄比較寬。

---

## 三欄

```python
st.columns([1,2,3])
```

畫面：

```
| 小 | 中 |   大   |
```

---

# 第十章：with

可以把很多元件放進同一欄。

例如：

```python
with col1:
    st.button("按鈕")
    st.write("文字")
```

代表：

按鈕和文字都會放在第一欄。

---

# 第十一章：利用 for 建立很多按鈕

不用一直重複寫。

```python
cols = st.columns(4)

for i in range(4):
    with cols[i]:
        st.button(f"按鈕{i+1}")
```

畫面：

```
按鈕1   按鈕2   按鈕3   按鈕4
```

---

# 第十二章：文字輸入

```python
text = st.text_input(
    "請輸入文字",
    value="這是預設文字"
)
```

使用者可以輸入文字。

例如：

```
你好
```

就可以顯示：

```
你輸入的是：你好
```

---

# 第十三章：Session State

這是今天最重要的新觀念！

## 一般變數

```python
ans = 1
```

按按鈕之後：

```
ans = 2
```

可是重新整理後：

```
ans 又變回 1
```

因為程式重新開始執行。

---

## Session State

Session State 可以幫忙**記住資料**。

例如：

```python
if "ans1" not in st.session_state:
    st.session_state.ans1 = 1
```

第一次建立：

```
ans1 = 1
```

按按鈕：

```python
st.session_state.ans1 += 1
```

變成：

```
2
3
4
5
……
```

重新整理也不會馬上消失。

可以想像成：

> Session State 就像一本「小筆記本」，可以幫程式暫時記住資料。

---

# 第十四章：st.rerun()

有時候按按鈕後畫面沒有更新。

可以使用：

```python
st.rerun()
```

意思就是：

> 「請重新執行一次程式！」

畫面就會更新。

---

# 🌟 今天重點整理

✅ **List（串列）**：可以一次存放很多資料。
✅ **Index（索引）**：資料的位置，從 **0** 開始。
✅ **切片（Slice）**：一次取出很多資料，格式是 `List[開始:結束:間隔]`。
✅ **append()**：在 List 最後新增資料。
✅ **remove()**：刪除指定內容（只刪第一個找到的）。
✅ **pop()**：依照位置刪除資料，沒寫位置就刪最後一個。
✅ **sort()**：把 List 排序，由小到大。
✅ **st.columns()**：把網頁分成很多欄。
✅ **with**：把很多元件放到同一欄。
✅ **st.text_input()**：建立文字輸入框。
✅ **st.session_state**：讓程式記住資料，不會因重新整理就消失。
✅ **st.rerun()**：重新執行程式，更新畫面。
✅ **for 迴圈**：可以快速建立很多按鈕或重複做事情。

---

# 💡 學習小提醒

1. **List 的位置（Index）從 0 開始，不是從 1 開始。**
2. `append()` 是新增，`remove()` 和 `pop()` 是刪除，三個功能不要搞混。
3. `sort()` 排序後，原本的 List 會直接改變。
4. `st.columns()` 可以讓網頁排版更整齊。
"""
    )
with st.expander("class 4課堂筆記"): 
    st.write(
        """
        
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

* `streamlit`：做網頁程式。
* `time`：可以讓程式等待幾秒鐘。
* `random`：可以隨機產生數字。

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

* 最小值
* 最大值
* 一次增加多少

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

| 寫法    | 意思   |
| ----- | ---- |
| `+=`  | 加上   |
| `-=`  | 減掉   |
| `*=`  | 乘    |
| `/=`  | 除    |
| `//=` | 整數除法 |
| `%=`  | 取餘數  |
| `**=` | 次方   |

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

* 國文
* 數學
* 英文

---

# ⭐ 今天學到的重要指令整理

| 指令                   | 功能             |
| -------------------- | -------------- |
| `import`             | 匯入套件           |
| `st.title()`         | 標題             |
| `st.write()`         | 顯示文字           |
| `st.button()`        | 按鈕             |
| `st.text_input()`    | 文字輸入           |
| `st.number_input()`  | 數字輸入           |
| `st.success()`       | 成功訊息           |
| `st.columns()`       | 分欄             |
| `st.session_state`   | 記住資料           |
| `st.rerun()`         | 重新整理畫面         |
| `st.balloons()`      | 播放氣球動畫         |
| `time.sleep()`       | 等待幾秒           |
| `random.randrange()` | 隨機產生數字         |
| `while`              | 條件迴圈           |
| `break`              | 跳出迴圈           |
| `+=`、`-=` 等          | 快速運算           |
| `dict`               | 字典             |
| `keys()`             | 取得所有 Key       |
| `values()`           | 取得所有 Value     |
| `items()`            | 取得 Key 和 Value |
| `pop()`              | 刪除資料           |
| `sum()`              | 全部加總           |
| `len()`              | 計算資料數量         |
| `in`                 | 檢查資料是否存在       |

---
"""
)