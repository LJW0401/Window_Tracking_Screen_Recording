import pyautogui
import cv2
import numpy as np

# 截取屏幕的第一帧并显示
screenshot = pyautogui.screenshot()
frame = np.array(screenshot)
frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

# 创建一个窗口来显示截取的第一帧
cv2.imshow('First Frame', frame)

# 创建一个回调函数，用于记录鼠标事件
rect_start = None
def on_mouse(event, x, y, flags, param):
    global rect_start
    if event == cv2.EVENT_LBUTTONDOWN:
        rect_start = (x, y)
    elif event == cv2.EVENT_LBUTTONUP:
        rect_end = (x, y)
        # 绘制矩形框选区域
        cv2.rectangle(frame, rect_start, rect_end, (0, 255, 0), 2)
        cv2.imshow('First Frame', frame)
        # 保存矩形框选区域的坐标
        print("Selected region coordinates:", rect_start, rect_end)

# 注册鼠标事件回调函数
cv2.setMouseCallback('First Frame', on_mouse)

# 等待按下任意键退出
cv2.waitKey(0)

# 关闭窗口
cv2.destroyAllWindows()
