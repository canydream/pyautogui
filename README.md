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


header 1 | header 2|header3
---|---|---
row 1 col 1 | row 1 col 2|blank
row 2 col 1 | row 2 col 2|


```
print("hello world")
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

`必须使用缩进`
    
    `coding`


***
~~上面是分割线~~


**bold**
*Italic*
~~删除线~~
++下划线++
==高亮Mark==

Hello
---

Hello
===

horizontal rule
> quote
> quote
somethong

>quote

- one
- 2
- 3

1. 1
2. 2
3. 3
4. 4

- [ ] 1
- [ ] 2
- [ ] 3
- [ ] 4

- [x] 1
- [x] 2

<html>
    <!--在这里插入内容-->
    html:
    <p style="font-size:40px;">some</p>
    <a href="dict.php" style='text-decoration: none;' class="fontColor">金华站通道词典</a>
</html>


```
code
```


```math
E = mc^2
```

TB，从上到下
TD，从上到下
BT，从下到上
RL，从右到左
LR，从左到右

```
graph LR
A-->B
B-->c
B-->d
d-->A
```

```
graph TB
  A
  B[bname]
  C(cname)
  D((dname))
  E>ename]
  F{fname}
```
```
graph TB
  A1-->B1
  A2---B2
  A3--text---B3
  A4--text-->B4
  A5-.-B5
  A6-.->B6
  A7-.text.-B7
  A8-.text.->B8
  A9===B9
  A10==>B10
  A11==text===B11
  A12==text==>B12
```

```
graph LR
  start("input x") --> handler("x > 0?")
  handler --yes--> yes("output x")
  handler --no--> start
  yes --> exit("exit")

```

```
graph LR
  subgraph g1
    a1-->b1
  end
  
  subgraph g2
    a2-->b2
  end
  
  subgraph g3
    a3-->b3
  end
  
  a3-->a2
```

```
gantt
dateFormat YYYY-MM-DD
section S1
T1: 2014-01-01, 9d
section S2
T2: 2014-01-11, 9d
section S3
T3: 2014-01-02, 9d
section S4
T3: 2014-01-02, 5d
```

```
sequenceDiagram

participant 客户端
participant 控制器
participant 业务

客户端->>业务:提交数据店铺
Note right of 客户端:提交数据进行验证
控制器->>控制器:验证数据完整性
Note left of 控制器:返回错误的字段信息
控制器-->>客户端:数据不完整
Note over 客户端: 用户输入通行证的账号、密码
控制器->>业务:保存店铺到数据库
业务-->>业务:save店铺数据
```
