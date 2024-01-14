# encoding=utf-8
"""
python如何下载图片
"""

import requests
from urllib.request import urlretrieve


# 原生的requests肯定可以的，只是写起来麻烦
def save_by_requests():
    url = "http://dingyue.ws.126.net/IeUJ9eIwIq0dWlTQ9IaqCga2HamhNNVsmWXibfFYuHBW21592631698406compressflag.jpeg";
    response = requests.get(url)
    print(response)
    print(response.content)
    with open("tangsan.jpg", "wb") as f:
        for data in response.iter_content(chunk_size=1024):
            f.write(data)


def save_by_urllib():
    url = "http://dingyue.ws.126.net/IeUJ9eIwIq0dWlTQ9IaqCga2HamhNNVsmWXibfFYuHBW21592631698406compressflag.jpeg";
    urlretrieve(url, "1.jpg")


if __name__ == "__main__":
    # save_by_requests()
    save_by_urllib()
