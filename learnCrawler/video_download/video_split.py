from moviepy.editor import VideoFileClip
import os

from learnCrawler.video_download.threadPool import ThreadPool

parts = 6
baseDir = "D:\\SP\\【700集全】地道美音 美中小学精选课程\\split"
inputDir = baseDir + "\\in\\"
outputDir = baseDir + "\\out\\"
pool = ThreadPool(2)


def split_video(file_path):
    filename = os.path.basename(file_path)
    filename.split()
    subfilename1 = filename.split("】")[0]
    subfilename2 = "】" + filename.split("】")[1]
    print(subfilename1)
    print(subfilename2)

    clip = VideoFileClip(file_path)
    duration = clip.duration  # 视频总长度
    part_duration = duration / parts  # 每部分的长度
    for i in range(parts):
        subclip = clip.subclip(part_duration * i, part_duration * (i + 1))
        output_file = outputDir + subfilename1 + f"_{i + 1}" + subfilename2  # 输出文件路径和文件名
        print(output_file)
        subclip.write_videofile(output_file)


if __name__ == "__main__":
    folder = os.path.exists(outputDir)
    if not folder:
        os.makedirs(outputDir)
    for root, dirs, files in os.walk(inputDir):
        # 遍历当前目录下的所有文件
        for file in files:
            pool.run(func=split_video, args={os.path.join(root, file)})

    pool.close()
