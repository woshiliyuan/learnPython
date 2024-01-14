import time

import win32api
import win32con
import win32gui


# 模拟鼠标点击
def mouse_click(x, y):
    time.sleep(5)
    win32api.SetCursorPos([x, y])
    time.sleep(3)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    time.sleep(3)
    # 键盘按键
    win32api.keybd_event(77, 0, 0, 0)  # 键盘按下  68  M
    win32api.keybd_event(55, 0, 0, 0)  # 键盘按下  67 7


def test():
    # 获取鼠标当前位置的坐标
    win32api.GetCursorPos()
    # 将鼠标移动到坐标处
    win32api.SetCursorPos((200, 200))
    # 左点击
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 200, 200, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 200, 200, 0, 0)
    # 获取窗口句柄
    win32gui.FindWindow(None, 'TIM')
    win32gui.FindWindow('TXGuiFoundation', None)
    # 通过坐标获取窗口句柄
    hw = win32gui.WindowFromPoint(win32api.GetCursorPos())
    # 获取窗口class name
    win32gui.GetClassName(hw)
    # 获取窗口标题
    win32gui.GetWindowText(hw)


if __name__ == "__main__":
    mouse_click(55, 1050)
