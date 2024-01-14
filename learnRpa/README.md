====#Selenium====
用于Web应用程序测试的工具。Selenium测试直接运行在浏览器中，就像真正的用户在操作一样。支持的浏览器包括IE，Mozilla Firefox，Safari，Google Chrome，Opera等。
效果演示

Request爬虫：
req = requests.get(url = target)
获取的是初次页面加载html, 后端ajax异步加载出来的dom，数据需要另外调用接口
而selenium可以使用时间等待让浏览器自己加载完成后再获取数据。

selenium页面等待：
time.sleep(5)
显示等待：
WebDriverWait 默认情况下会每500毫秒调用一次ExpectedCondition直到结果成功返回。 ExpectedCondition成功的返回结果是一个布尔类型的true或是不为null的返回值。
隐式等待：
driver.implicitly_wait(10)

selenium ide： 录制动作，转为python代码
====#pywin32====
方便python开发者快速调用windows API，较重要的三个模块就是win32api、win32gui和win32con。

win32api：
鼠标键盘
截图
操作注册表

win32gui：
创建图形化界面窗体 
查找并选中正在运行的窗口，例如FindWindow

win32con：
定义了windows API内的宏，例如MessageBox内的MB_OK
====#Pyaugui====
可以模拟鼠标移动、拖动，单机双击等。键盘输入，组合键等。
截图，定位图片元素。


