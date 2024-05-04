import os
import shutil

baseDir = "D:\\SP\\douyin\\user_朗朗英语故事_MS4wLjABAAAAPPemeQQ5PqwskiNaIAirCv2sib1CmLLt_FTFiYsb-lSVM7qQnV3YJBkQBySg6zuw"
inputDir = baseDir
outputDir = baseDir + "\\0_out\\"

if __name__ == "__main__":
    folder = os.path.exists(outputDir)
    if not folder:
        os.makedirs(outputDir)
    i = 0
    for root, dirs, files in os.walk(inputDir):
        # 遍历当前目录下的所有文件
        for file in files:

            file_name = os.path.basename(file)
            if file_name.endswith(".mp4"):
                i = i + 1
                file_name_pre = "【" + '{:0>3}'.format(i) + "】"

                print('===============copy start：{},filename:{}'.format(i , file_name))
                dest_path = outputDir + "【" + '{:0>3}'.format(i) + "】" + file_name
                shutil.copy2(os.path.join(root, file), dest_path)
                print('===============copy end===============')
