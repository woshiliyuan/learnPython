# coding=utf-8
"""
遇见遍历所有可能的可以使用搜索算法：

1. 深度优先
   递归，栈

2. 广度优先
   队列
"""
import os


# 1. 深度优先
# 1.1 遍历文件夹
def allfile(basepath,brank):
    for item in os.listdir(basepath):  # 循环目录下的每一个元素（目录或文件）
        path = os.path.join(basepath,item)  # 路径拼接：要查询目录 + 第一级目录/文件
        if os.path.isfile(path):  # 判断：若果为文件，直接输出path
            print(brank + item)
        else:
            print(brank.replace(" ","-") + item)
            allfile(path,brank + "    ")  # 如果仍是是目录，递归调用当前函数


if __name__ == "__main__":
    allfile(r"D:\code\python_workplace\learnPython\study","")
