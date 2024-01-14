import pyautogui
import time


# 1. 判断坐标，屏幕大小
def show_coordinate():
    # 判断(x,y)是否在屏幕上
    x, y = 122, 244
    flag = pyautogui.onScreen(x, y)  # 结果为true
    print(flag)

    width, height = pyautogui.size()  # 屏幕的宽度和高度
    print("screen size: ", width, height)


def move_mouse():
    # 1. 打印当前坐标
    currentMouseX, currentMouseY = pyautogui.position()  # 鼠标当前位置
    print(currentMouseX, currentMouseY)
    time.sleep(5)

    # 2. 鼠标移动位置
    pyautogui.moveTo(500, 500, duration=0.25)
    time.sleep(3)
    pyautogui.moveRel(100, 0)  # 从当前位置右移100像素
    pyautogui.moveRel(0, -100, duration=0.25)  # 向下
    time.sleep(3)

    # 3. 鼠标拖拽
    pyautogui.moveTo(500, 500, duration=0.25)
    # 按住鼠标左键，把鼠标拖拽到(600, 500)位置
    pyautogui.dragRel(200, 0, button='left', duration=0.5)
    # 按住鼠标左键，用1秒钟把鼠标向上拖拽
    pyautogui.dragRel(0, -100, duration=1)
    pyautogui.dragRel(-200, 0, duration=1)
    pyautogui.dragRel(0, 100, duration=1)


def mouse_click():
    time.sleep(5)
    coords = pyautogui.locateOnScreen('A.png')
    print(coords)
    x, y = pyautogui.center(coords)
    pyautogui.leftClick(x, y)
    # pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')
    # 其中，button属性可以设置成left，middle和right。
    pyautogui.click(425, 125, 2, 0.25, button='left')
    time.sleep(6)

    pyautogui.doubleClick(x=400, y=700)  # 鼠标当前位置左击两下


def keyboard():
    time.sleep(5)
    pyautogui.typewrite('Hello world!')  # 输入Hello world!字符串
    pyautogui.press('enter')  # 按下并松开（轻敲）回车键
    pyautogui.typewrite('pyautogui is so cool!', interval=0.25)


def deal_pic():
    # 显示一个简单的带文字和OK按钮的消息弹窗。用户点击后返回button的文字。
    b = pyautogui.alert(text='要开始程序么？', title='请求框', button='OK')
    print(b)  # 输出结果为OK
    # 截全屏并设置保存图片的位置和名称
    pyautogui.screenshot('my_screenshot.png')
    # 不截全屏，截取区域图片。截取区域region参数为：左上角XY坐标值、宽度和高度
    pyautogui.screenshot(r'region_screenshot.png', region=(300, 300, 600, 600))


if __name__ == "__main__":
    # show_coordinate()
    # move_mouse()
    # mouse_click()
    # keyboard()
    deal_pic()
