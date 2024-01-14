# encoding=utf-8
"""
网络爬虫1：演示最简单的get请求； 如何get请求获取文本内容
应用场景：文本，小说的获取

参考链接：https://cuijiahua.com/blog/2020/04/spider-6.html
"""

import requests
from bs4 import BeautifulSoup


# 最简单的爬虫示例，获取网页文本信息
def get_most_concise():
    response = requests.get("http://www.baidu.com")
    # 可能因为requests是老外写的，默认使用'ISO-8859-1'编码，中文就乱码了
    response.encoding = 'utf-8'
    # response是一个对象，里面有status_code, text, content等key值
    print(response.text)


# 例子二
def get_txt():
    target = 'https://www.xbiquge.la/24/24770/34750753.html'
    response = requests.get(target)
    response.encoding = 'utf-8'
    bs = BeautifulSoup(response.text)
    content_html = bs.find('div', id='content')
    # 开头的4个空格去掉
    print(content_html.text.split('\xa0' * 4))


if __name__ == '__main__':
    # 1. 调用最简洁的的get请求
    get_most_concise()

    # 2. 获取txt文本内容
    get_txt()
