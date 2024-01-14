# encoding=utf-8
"""
网络爬虫二：get再发挥，获取 斗罗大陆，小三的英雄事迹
"""
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup


def get_content(target):
    req = requests.get(url=target)
    req.encoding = 'utf-8'
    html = req.text
    bf = BeautifulSoup(html, 'html.parser')
    texts = bf.find('div', id='content')
    if texts is None:
        return ""
    content = texts.text.strip().split('\xa0' * 4)
    return content


def get_chapters(book_name, chapter_list_url):
    # 1. 获取小说章节列表页
    req = requests.get(url=chapter_list_url)
    req.encoding = 'utf-8'
    html = req.text
    # 'lxml', html.parser都是beautifulSoup的不同解析器而已
    chapter_bs = BeautifulSoup(html, 'html.parser')
    chapters = chapter_bs.find('div', id='list')
    chapters = chapters.find_all('a')
    # tqdm是显示进度条的，让程序更加优雅
    server = 'https://www.xbiquge.la'
    for chapter in tqdm(chapters):
        # 每一章节的章节名称&链接
        chapter_name = chapter.string
        url = server + chapter.get('href')
        print(chapter_name, ": ", url)

        # 2. 根据章节链接获取章节内容
        content = get_content(url)

        # 3. 写入文本
        with open(book_name, 'a', encoding='utf-8') as f:
            f.write(chapter_name)
            f.write('\n')
            f.write('\n'.join(content))
            f.write('\n')


if __name__ == '__main__':
    book_name = "斗罗大陆5重生唐三.txt"
    chapter_list_url = "https://www.xbiquge.la/24/24770/"

    get_chapters(book_name, chapter_list_url)

    # content = get_content("https://www.xbiquge.la/24/24770/31527525.html")
    # print(content)
