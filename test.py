# 鼠标操作函数	
# move(x,y)、 moveTo(x,y)	移动鼠标，前者移动相对位置，后者移动到指定位置
# click(x,y)、doubleClick、rightClick	单击/双击/右击，无参版本在当前位置点击鼠标
# drag(x,y)、dragTo(x,y)	拖动鼠标
# mouseDown、mouseUp	按下按键，松开按键
# scroll	向下滚动鼠标滚轮的函数

# 键盘操作函数	
# press('left',press=3)	
# hotkey('ctrl','s')	按下Ctrl+S组合键
# keyDown、keyUp	按下和松开键盘按键

# 提示框函数	
# alert(text='',title='',button=['OK','Cancle'])	显示警告对话框
# confirm()	显示确认对话框
# prompt()	显示提示对话框
# password()	显示密码输入对话框

# 屏幕截图和定位函数	
# screenshot('image.png')	保存截图并返回截图，无参版本直接返回截图不保存
# center('image.png')	从屏幕上寻找图片位置，返回框位置
# locateOnScreen('img')	从屏幕寻找图片位置，直接返回坐标


# 查看安装位置
import sys

print(sys.executable)
print("hello")

# python config:
# D:\Program Files\python381\Scripts
# pip install opencv_python-4.5.3.56-cp38-cp38-win_amd64.whl
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pandas
