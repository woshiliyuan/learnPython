"""
selenium 简单入门：hello world
"""
from selenium import webdriver


# 1. 初始化一个谷歌浏览器实例
driver = webdriver.Chrome(executable_path='chromedriver.exe')

# 2. 访问链接
driver.get("http://www.sohu.com")

# 3. do something: 例如截图
driver.get_screenshot_as_file(r"./1.png")
