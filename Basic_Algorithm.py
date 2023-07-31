import pyautogui
import cv2
import numpy as np

# 设置录屏的分辨率和帧率
screen_width, screen_height = pyautogui.size()
fps = 30

# 设置视频编码器和输出文件名
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 使用H.264编码器保存为mp4格式
output_file = 'E:/#LJW/#Python_APPs/Window_Tracking_Screen_Recording/output/screencast.mp4'

# 创建VideoWriter对象
out = cv2.VideoWriter(output_file, fourcc, fps, (screen_width, screen_height))

try:
    # 设置录屏的时长（秒）
    duration = 5

    # 开始录屏
    for i in range(fps * duration):
        screenshot = pyautogui.screenshot()
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        out.write(frame)
        print(f"Recording frame {i + 1}/{fps * duration}")

    print("Screen recording completed.")

except KeyboardInterrupt:
    print("Screen recording interrupted.")

finally:
    # 释放资源
    out.release()
