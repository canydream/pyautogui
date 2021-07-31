import pyautogui
import time

time.sleep(1)

distance = 100

pyautogui.moveTo(400, 300)
while distance > 0:
    pyautogui.drag(distance, 0, duration=0.1)
    distance -= 5
    pyautogui.drag(0, distance, duration=0.1)
    pyautogui.drag(-distance, 0, duration=0.1)
    distance -= 5
    pyautogui.drag(0, -distance, duration=0.1)
    print(distance)
