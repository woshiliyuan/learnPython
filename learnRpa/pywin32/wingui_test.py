import win32gui, win32con
import time


def write_notepad():
    time.sleep(5)
    # 1. 查找窗体 && 子窗口
    win = win32gui.FindWindow('Notepad', '新建文本文档.txt - 记事本')
    tid = win32gui.FindWindowEx(win, None, 'Edit', None)
    # if 没找到窗体，返回0
    print("%x" % tid)
    print("%x" % win)

    # 2. 窗口至于最前，不放到前面也不影响后续操作
    # 感觉这句非常不好用，窗口最小化状态，还会失效
    win32gui.SetForegroundWindow(win)

    # 3. 写入内容，回车
    win32gui.SendMessage(tid, win32con.WM_SETTEXT, None, '你好hello word!')
    win32gui.PostMessage(tid, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)

    # 4. 关闭窗口
    time.sleep(5)
    win32gui.PostMessage(win, win32con.WM_CLOSE, 0, 0)


def set_front_win(windowsname, filename):
    # 获取窗口句柄
    handle = win32gui.FindWindow(None, windowsname)
    # 将窗口放在前台，并激活该窗口（窗口不能最小化）
    win32gui.SetForegroundWindow(handle)
    # 获取窗口DC
    hdDC = win32gui.GetWindowDC(handle)
    # 根据句柄创建一个DC
    newedDC = win32gui.CreateDCFromHandle(hdDC)
    # 创建一个兼容设备内存的DC
    saveDC = newedDC.CreateCompatibleDC()
    # 创建bitmap保存图片
    saveBitmap = win32gui.CreateBitmap()

    # 获取窗口的位置信息
    left, top, right, bottom = win32gui.GetWindowRect(handle)
    # 窗口长宽
    width = right - left
    height = bottom - top
    # bitmap初始化
    saveBitmap.CreateCompatibleBitmap(newedDC, width, height)
    saveDC.SelectObject(saveBitmap)
    saveDC.BitBlt((0, 0), (width, height), newedDC, (0, 0), win32con.SRCCOPY)
    saveBitmap.SaveBitmapFile(saveDC, filename)


if __name__ == "__main__":
    set_front_win("腾讯视频", "截图.png")
