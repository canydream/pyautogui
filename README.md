# pyautogui
pyautogui Study
标题

header1
===
# header1

header2
---

# header1  #标准写法后需要一个空格
## header2
### header3
#### header4
##### headr5
###### headr6
粗体与斜体
*斜体* or _斜体_

**粗体** or __粗体__

***粗斜体*** or ___粗斜体___

> 引用
> 引用的第二行

> 这是另一个引用


[link](https://note.youdao.com/)

![替代文本](https://note.youdao.com/favicon.ico)

图片可以使用https://sm.ms/生成链接


header 1 | header 2
---|---
row 1 col 1 | row 1 col 2
row 2 col 1 | row 2 col 2


header 1 | header 2|header3
---|---|---
row 1 col 1 | row 1 col 2|blank
row 2 col 1 | row 2 col 2|


```
some code
some coding 
some code 
def find_and_click(image):
    # if open takes 1 positional argument but 2 were given
    x, y = pyautogui.locateCenterOnScreen(image, confidence=0.9)
    pyautogui.click(x, y)
find_and_click(f)
```

`one line code
hello world
def find_and_click(image):
    # if open takes 1 positional argument but 2 were given
    x, y = pyautogui.locateCenterOnScreen(image, confidence=0.9)
    pyautogui.click(x, y)
find_and_click(f)`

`这是代码`
    
    `coding`

***
上面是分割线
