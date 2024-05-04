from pytube import Playlist

downloadDir = "D://SP//youtube//历史解密//"

# 设置YouTube视频列表的URL
playlist_url = 'https://www.youtube.com/playlist?list=PLF16d5bzacYKIgVnByfD2-T3sYXw-sPf0'

def down(start):
    # 创建Playlist对象
    playlist = Playlist(playlist_url)
    videos = playlist.videos
    # 遍历视频列表并下载每个视频
    for i, video in enumerate(videos):
        print('i：{}'.format(i))
        # 下载视频
        if i >= start - 1:
            # 选择一个视频流
            stream = video.streams.first()
            # 修改文件名称
            filename = "【" + '{:0>3}'.format(i + 1) + "】" + stream.default_filename
            print('down start：{},filename:{}'.format(i + 1, filename))
            # 下载
            stream.download(downloadDir, filename=filename)
            print('down end：{},filename:{}'.format(i + 1, filename))


if __name__ == "__main__":
    try:
        while (True):
            start = input("请输入开始编号：")
            down(int(start))
    except Exception as e:
        print(e)