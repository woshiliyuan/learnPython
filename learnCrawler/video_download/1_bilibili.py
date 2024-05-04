import requests
import json
from tqdm import tqdm
import time
import os

from learnCrawler.video_download.threadPool import ThreadPool

session = requests.session()
ico = {}
videoInfos = []
# 视频标题上是否添加P？ 比如p1,p2,p3。。。
title_p = True
bv = "BV1c7411Z78e"
downloadDir = "D:\\SP\\【700集全】地道美音 美中小学精选课程\\"

cookie = ("buvid3=xxxxxxxxxxxxxxxxxxxxxxxx")

# cookie登录账号
def cookieLogin():
    url = "https://api.bilibili.com/x/space/myinfo"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55",
        "cookie": cookie
    }

    res = session.get(url=url, headers=headers).text
    myJSON = json.loads(res)
    userName = myJSON["data"]["name"]
    vipStatus = myJSON["data"]["vip"]["status"]
    if vipStatus == 0:
        vipStatus = "非会员"
    else:
        vipStatus = "大会员"
    print("您的账号名：" + userName + ",当前为：" + vipStatus)


# 获取视频数据
def getVideDate(bv):
    url = "https://api.bilibili.com/x/web-interface/view?bvid=" + bv
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55",
        "cookie": cookie
    }
    viderJSON = json.loads(session.get(url=url, headers=headers).text)
    ico["video"] = viderJSON["data"]["pic"]
    ico["up"] = viderJSON["data"]["owner"]["face"]

    video = viderJSON["data"]["pages"]
    print("正在获取视频数据\n视频标题：" + viderJSON["data"]["title"])

    for i in tqdm(range(len(video))):
        url = "http://api.bilibili.com/x/player/playurl?cid={cid}&bvid={bv}&qn={qn}".format(cid=video[i]["cid"], bv=bv,
                                                                                            qn=80)
        res = session.get(url=url, headers=headers).text
        res = json.loads(res)

        videoInfo = {}
        videoInfo["url"] = res["data"]["durl"][0]["url"]
        if title_p:
            videoInfo["title"] = f'P{str(video[i]["page"])} {video[i]["part"]}'
        else:
            videoInfo["title"] = video[i]["part"]

        if res["data"]["quality"] == 116:
            videoInfo["quality"] = "高清 1080P60"
        elif res["data"]["quality"] == 80:
            videoInfo["quality"] = "高清 1080P"
        elif res["data"]["quality"] == 64:
            videoInfo["quality"] = "高清 720P"
        elif res["data"]["quality"] == 32:
            videoInfo["quality"] = "清晰 480P"
        elif res["data"]["quality"] == 16:
            videoInfo["quality"] = "流畅 360P"
        global videoInfos
        videoInfos.append(videoInfo)
        time.sleep(0.2)
    print("视频数据获取完成\n")


# 打印视频数据
def printVideoDate():
    if videoInfos == []:
        print("未找到视频数据，请先获取视频数据！")
        return
    for i in range(len(videoInfos)):
        video = videoInfos[i]
        print(str(i + 1) + "：" + video["title"] + " " + video["quality"])


# 下载视频
def downVideo(dir, num):
    # 文件夹不存在，则创建文件夹
    folder = os.path.exists(dir)
    if not folder:
        os.makedirs(dir)

    url = videoInfos[num]["url"]
    videoName = videoInfos[num]["title"]
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55",
        "referer": "https://www.bilibili.com"
    }
    res = session.get(url=url, headers=headers, stream=True)
    total_size = int(int(res.headers["Content-Length"]) / 1024 + 0.5)

    with open(dir + videoName + ".mp4", "wb") as f:
        print('开始下载文件：{},当前文件大小：{}KB'.format(videoName, total_size))
        for chunk in tqdm(res.iter_content(1024), total=total_size, unit='k', desc='Downloading'):
            f.write(chunk)
    print(videoName, "下载完毕")


def showMenu():
    print("0: 显示菜单\n1: 获取视频数据\n2: 打印视频数据\n3: 下载视频\n-1: 退出程序")


if __name__ == "__main__":
    cookieLogin()
    print()
    showMenu()
    pool = ThreadPool(5)

    while (True):
        i = input("请输入功能菜单编号：")
        if i == '-1':
            break
        elif i == '0':
            showMenu()
        elif i == '1':
            if len(videoInfos) > 0:
                _op = input('当前系统内存有其他的视频，将会删除之前的视频，请确认是否继续？输入任意键继续，输入q退出')
                if _op == 'q' or _op == 'Q':
                    continue
                else:
                    print(f'清空内存数据')
                    videoInfos.clear()
            getVideDate(bv)
            printVideoDate()
        elif i == '2':
            printVideoDate()
        elif i == '3':
            num = input("请输入要下载的编号(多个视频写成数组形式，例如：[1,2,3]),默认为下载所有视频：")
            if (num == ''):
                print("预下载视频" + str(len(videoInfos)) + '个')
                for i in range(len(videoInfos)):  # 全部
                    downVideo(dir=downloadDir, num=i)
                    # pool.run(func=downVideo,args={downloadDir,i})
            elif (isinstance(eval(num), int)):  # 区间[start=num]
                for i in range(int(num), len(videoInfos)):
                    downVideo(dir=downloadDir, num=i - 1)
                # downVideo(dir=downloadDir, num=int(num) - 1)
            elif (isinstance(eval(num), list)):  # 区间[列表]
                print("预下载视频" + str(len(eval(num))) + '个')
                for i in eval(num):
                    downVideo(dir=downloadDir, num=i - 1)
        elif i == '':
            pass

    pool.close()
    print("退出成功")
