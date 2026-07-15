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
"""
第一行
第二行
第三行
"""
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
st.markdown("""
# 第一級標題

## 第二級標題

### 第三級標題

- 蘋果
- 香蕉
- 西瓜

**粗體**

*斜體*

---
""")
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
