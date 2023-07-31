import pyautogui
import cv2
import numpy as np

class AreaSelector():
    def __init__(self, image:np.ndarray) -> None:
        self.image = image
        self.rect_start = (0,0)
        self.rect_end = (0,0)
        self.click_counter = 0
        self.pos_mous_down = (0,0)
        self.pos_mous_up = (0,0)


    def select_area(self):
        cv2.imshow('image', self.image)
        # 注册鼠标事件回调函数
        cv2.setMouseCallback('image', self.on_mouse)
        # 等待按下任意键退出
        cv2.waitKey(0)
        # 关闭窗口
        cv2.destroyAllWindows()


    def on_mouse(self,event, x, y, flags, param):
        '''创建一个回调函数，用于记录鼠标事件'''
        position = (x, y)
        if event == cv2.EVENT_LBUTTONDOWN:
            self.click_counter += 1
            self.pos_mous_down = position
            if self.click_counter == 1:
                self.rect_start = position
            elif self.click_counter == 2:
                self.rect_end = position
        elif event == cv2.EVENT_LBUTTONUP:
            self.pos_mous_up = position
            if np.linalg.norm(np.array(self.pos_mous_down) - np.array(self.pos_mous_up)) > 5:#如果用户选择直接按住拉取矩形框也会被记录
                self.rect_end = position
                self.click_counter += 1
        
        if self.click_counter == 1:
            image = self.image.copy()
            cv2.rectangle(image, self.rect_start, position, (0, 255, 0), 2)
            cv2.imshow('image', image)
        elif self.click_counter == 2:
            # 保存矩形框选区域的坐标
            print("Selected region coordinates:", self.rect_start, self.rect_end)
            self.click_counter = 0


class Recorder():
    def __init__(self) -> None:
        pass


if __name__ == "__main__":
    # 截取屏幕的第一帧并显示
    screenshot = pyautogui.screenshot()
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    
    # 在图像上指定ROI的坐标（左上角和右下角的点坐标）
    x1, y1 = 100, 100  # 左上角坐标
    x2, y2 = 400, 400  # 右下角坐标

    # 切片提取ROI区域
    roi = frame[y1:y2, x1:x2]
    area_selector = AreaSelector(roi)
    area_selector.select_area()