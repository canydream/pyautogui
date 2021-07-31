import pyautogui
import time

time.sleep(3)

# Windows计算器的按钮截图
f = 'start.png'
d = 'chrome.png'


# 图片识别和点击的函数


def find_and_click(image):
    # if open takes 1 positional argument but 2 were given
    x, y = pyautogui.locateCenterOnScreen(image, confidence=0.9)
    pyautogui.click(x, y)


# 执行5*8=
find_and_click(f)
