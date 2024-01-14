"""
selenium api例子：
百度自动键入搜索值，登录qq邮箱，并发送邮件
"""

from selenium import webdriver
from selenium.webdriver import ActionChains
from utils.config import *
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

# 1. 初始化一个谷歌浏览器实例
driver = webdriver.Chrome(executable_path='chromedriver.exe')


# 2. 访问链接，初始化窗口大小
# driver.get('http://www.sohu.com')
# print('init successfully')
# driver.maximize_window()
# driver.set_window_size(600, 800)


# 1. --------------   填充表单   -----------------------------------
def login_baidu():
    # 打开百度地址
    driver.get('https://www.baidu.com/')
    # 窗口最大化
    driver.maximize_window()
    # 隐式等待
    driver.implicitly_wait(2)

    # 输入搜索内容
    driver.find_element(By.ID, "kw").send_keys("selenium官方教程")
    # 点击百度一下按钮
    driver.find_element(By.ID, "su").click()

    # 点击登录按钮
    driver.find_element(By.LINK_TEXT, '登录').click()
    # 定位用户名登录元素
    driver.find_element(By.ID, 'TANGRAM__PSP_11__changePwdCodeItem').click()
    # 定位账号输入框，并输入账号
    driver.find_element(By.ID, 'TANGRAM__PSP_11__userName').send_keys(get_config('baidu', 'username'))
    # 定位密码输入框，并输入密码
    driver.find_element(By.ID, 'TANGRAM__PSP_11__password').send_keys(get_config('baidu', 'password'))
    # 点击登录按钮
    driver.find_element(By.ID, 'TANGRAM__PSP_11__submit').click()

    # do something: 例如截图
    driver.get_screenshot_as_file(r'./1.png')


def login_mp_weixin():
    driver.get('https://wx.qq.com/')
    # 1. 切换到用户名密码框
    driver.find_element(By.LINK_TEXT, '使用帐号登录').click()
    # 动态加载的，直接点击无效
    # driver.find_element(By.CLASS_NAME, 'login__type__container__select-type').click()

    # 2. 账号密码登录
    driver.find_element(By.NAME, 'account').send_keys(get_config('weixin', 'username'))
    driver.find_element(By.NAME, 'password').send_keys(get_config('weixin', 'password'))
    driver.find_element(By.NAME, 'btn_login').click()


# 2. --------------------   如何更优雅的查找元素    ----------------------------
def login_qq_mail():
    driver.get('https://mail.qq.com/')

    # 1. 切换到登陆frame（!!!!!!!!必须先切换!!!!!!!!）
    driver.switch_to.frame('login_frame')

    # 2. 用户名，密码输入
    driver.find_element(By.ID, 'u').send_keys(get_config('qqmail', 'username'))
    driver.find_element(By.ID, 'p').send_keys(get_config('qqmail', 'password'))
    time.sleep(3)
    driver.find_element(By.ID, 'login_button').click()

    # 3. 最有意思的，滑动验证码
    # time.sleep(3)
    # drag_pic()

    # 4. 可能需要手机验证码：显示等待
    # wait = WebDriverWait(driver, 30)
    # element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'get-sms')))
    # print(driver.find_element(By.CLASS_NAME, 'get-sms').text)
    # element.click()

    # 隐式等待
    # driver.implicitly_wait(15)
    # driver..find_element(By.CLASS_NAME, 'get-sms').click()

    # 5. 显示等待来发送邮件玩玩
    wait = WebDriverWait(driver, 30)
    element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, '写信')))
    print(element.text)
    send_qq_mail()


# 拖拽验证码进度条；现在是失败的，待改造
def drag_pic():
    # 接着上面的 distance = y * (280 / 680) - 21 继续
    # 模拟人为拖动按钮
    # distance = 800
    element = driver.find_element(By.ID, 'tcaptcha_drag_button')
    # has_gone_dist = 0
    # remaining_dist = distance
    # distance += randint(-10, 10)
    # 按下鼠标左键
    # ActionChains(driver).click_and_hold(element).perform()
    # time.sleep(2)
    # ActionChains(driver).move_by_offset(500, 0).perform()
    if element.is_displayed():
        print('display')
        ActionChains(driver).drag_and_drop_by_offset(element, 178, 0)
        ActionChains(driver).release(on_element=element).perform()
    else:
        print('no display')

    # while remaining_dist > 0:
    #     ratio = remaining_dist / distance
    #
    #     if ratio < 0.2:
    #         # 开始阶段移动较慢
    #         span = random.randint(5, 8)
    #     elif ratio > 0.8:
    #         # 结束阶段移动较慢
    #         span = random.randint(5, 8)
    #     else:
    #         # 中间部分移动快
    #         span = random.randint(10, 16)
    #
    #     ActionChains(driver).move_by_offset(span, random.randint(-5, 5)).perform()
    #     remaining_dist -= span
    #     has_gone_dist += span
    #     time.sleep(random.randint(5, 20) / 100)
    #     ActionChains(driver).move_by_offset(remaining_dist, random.randint(-5, 5)).perform()


def send_qq_mail():
    # 写信
    # 单击写信按钮
    driver.find_element(By.LINK_TEXT, '写信').click()
    time.sleep(2)
    # 切换到mainFrame
    driver.switch_to.frame('mainFrame')
    time.sleep(2)
    # 输入收件人
    driver.find_element(By.XPATH,"'//*[@id='toAreaCtrl']/div[2]/input").send_keys(get_config('qqmail', 'mailTo'))
    # 输入主题
    driver.find_element(By.ID, 'subject').send_keys('test selenium')
    # 输入正文
    body_frame = driver.find_element(By.CLASS_NAME, 'qmEditorIfrmEditArea')
    driver.switch_to.frame(body_frame)
    # 添加正文
    driver.find_element(By.XPATH, '/html/body').send_keys(
        '您好！\n 月落乌啼霜满天，江枫渔火对愁眠！打扰了，测试程序如何自动发送垃圾邮件~')
    # 退回大Frame再点击发送
    driver.switch_to.parent_frame()
    driver.find_element(By.XPATH, "//*[@id='toolbar']/div/a[1]").click()

    # content = driver.find_element(By.CLASS_NAME, 'qmEditorIfrmEditArea')
    # content[0].click()  # !!!!!!!must click!!!!!!!
    # content[0].send_keys('您好！\n 月落乌啼霜满天，江枫渔火对愁眠！')
    # 点击发送按钮
    # driver.find_element(By.XPATH, '//*[@id='toolbar']/div/a[1]').click()
    # driver.find_element(By.XPATH, '//a[@name='sendbtn' and @tabindex='9']').click()
    # 断言发送成功
    # assert u'酷不酷，再写一封？' in driver.page_source


if __name__ == '__main__':
    # 1. 如何填充表单
    # login_mp_weixin()
    login_baidu()

    # 2. 如何定位元素
    # login_qq_mail()

    # 3. 时间等待
    time.sleep(10)
    driver.quit()
