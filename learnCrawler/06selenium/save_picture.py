from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome("chromedriver.exe")
url = "http://dingyue.ws.126.net/IeUJ9eIwIq0dWlTQ9IaqCga2HamhNNVsmWXibfFYuHBW21592631698406compressflag.jpeg"
driver.get(url)
# 超链接元素定位
element = driver.find_element(By.TAG_NAME, "img")
# 通过ActionChains的context_click进行对link元素右键操作,在按下另存为的快捷键K
ActionChains(driver).context_click(element).send_keys('V').perform()

time.sleep(10)
driver.quit()
