# encoding=utf-8
"""
牛气冲天的视频下载，如何破解vip免费看视频
https://cuijiahua.com/blog/2020/05/spider-9.html
"""

import os
import ffmpy3
import requests
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool as ThreadPool

# 1. 调用搜索接口，获取搜索列表
search_keyword = '越狱第一季'
search_url = 'http://www.jisudhw.com/index.php'
search_params = {
    'm': 'vod-search'
}
search_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/81.0.4044.122 Safari/537.36',
    'Referer': 'http://www.jisudhw.com/',
    'Origin': 'http://www.jisudhw.com',
    'Host': 'www.jisudhw.com'
}
search_datas = {
    'wd': search_keyword,
    'submit': 'search'
}
search_res = {}
video_dir = ''

r = requests.post(url=search_url, params=search_params, headers=search_headers, data=search_datas)
r.encoding = 'utf-8'

search_html = BeautifulSoup(r.text, 'lxml')
# 1. 视频搜索页，这里返回的是一个列表，会有多个的，所以最好search_keyword设置的全一些，让这里变少；
search_spans = search_html.find_all('span', class_='xing_vb4')
server = 'http://www.jisudhw.com'
for span in search_spans:
    url = server + span.a.get('href')
    name = span.a.string
    print(name)
    print(url)
    video_dir = name
    if name not in os.listdir('/'):
        os.mkdir(name)

    # 2. 获取视频列表页
    detail_url = url
    r = requests.get(url=detail_url)
    r.encoding = 'utf-8'
    detail_bf = BeautifulSoup(r.text, 'lxml')
    num = 1
    # url - num； 每一集url和集数映射起来

    for each_url in detail_bf.find_all('input'):
        if 'm3u8' in each_url.get('value'):
            url = each_url.get('value')
            if url not in search_res.keys():
                search_res[url] = num
            print('第%03d集:' % num)
            print(url)
            num += 1


def downVideo(url):
    num = search_res[url]
    name = os.path.join(video_dir, '第%03d集.mp4' % num)
    ffmpy3.FFmpeg(inputs={url: None}, outputs={name: None}).run()


# 开8个线程池
pool = ThreadPool(8)
results = pool.map(downVideo, search_res.keys())
pool.close()
pool.join()
