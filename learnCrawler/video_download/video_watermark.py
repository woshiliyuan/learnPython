import cv2
import os
from learnCrawler.video_download.threadPool import ThreadPool


baseDir = "D:\\SP\\douyin\\mix_英语小故事_7314185034326345747\\"
inputDir = baseDir
outputDir = baseDir + "\\out\\"
pool = ThreadPool(2)

def water_mark(video_path):
    # 视频文件路径
    video_path = 'input.mp4'
    # 输出视频文件路径
    output_path = 'output.mp4'
    # 水印文本
    text = 'WATERMARK'

    # 视频捕获对象
    cap = cv2.VideoCapture(video_path)
    # 获取视频的宽度、高度和帧率
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # 设置视频编码器和创建VideoWriter对象
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    # 循环读取视频帧
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            # 文本水印的位置和字体大小
            font = cv2.FONT_HERSHEY_SIMPLEX
            org = (50, 50)
            font_scale = 1
            color = (255, 255, 255)  # 白色
            thickness = 2

            # 在帧上添加水印
            cv2.putText(frame, text, org, font, font_scale, color, thickness, cv2.LINE_AA)

            # 将帧写入输出视频文件
            out.write(frame)

            # 显示帧（可选）
            cv2.imshow('Video', frame)

            # 按 'q' 退出循环
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            else:
                break

    # 释放资源
    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    folder = os.path.exists(outputDir)
    if not folder:
        os.makedirs(outputDir)
    for root, dirs, files in os.walk(inputDir):
        # 遍历当前目录下的所有文件
        for file in files:
            pool.run(func=water_mark, args={os.path.join(root, file)})

    pool.close()

