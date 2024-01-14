# coding=utf-8
"""
字典序排序
https://blog.csdn.net/weixin_30765475/article/details/97597556
题目描述:
给定整数n和m, 将1到n的这n个整数按字典序排列之后, 求其中的第m个数。
对于n=11, m=4, 按字典序排列依次为1, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 因此第4个数是2.
对于n=200, m=25, 按字典序排列依次为1 10 100 101 102 103 104 105 106 ... 97 98 99
因此第25个数是120…

示例1
输入: 11 4   输出: 2

示例2
输入: 200 25   输出: 120
"""


class Solution:
    def get_dict_order1(self,number,position):
        """
        python自带排序就能搞定
        """
        data = list(str(i) for i in range(1,number + 1))
        data.sort()
        print("data2 ",data)
        return data[position - 1]

    def get_dict_order(self,number,position):
        """
        自己重写比较逻辑，
        1. 使用插入排序 数组越界问题，简直让人崩溃，/(ㄒoㄒ)/~~
        2. 还是换冒泡得了
        """

        # 1. 初始化数据
        data = list(str(i) for i in range(1,number + 1))

        # 2. 来个简单的冒泡排序
        for i in range(number - 1):
            for j in range(number - 1 - i):
                if self.compare(data[j],data[j + 1]) == 1:
                    data[j],data[j + 1] = data[j + 1],data[j]

        print("data ",data)
        return data[position - 1]

    def compare(self,s1,s2):
        size = min(len(s1),len(s2))
        for i in range(size):
            if s1[i] < s2[i]:
                return -1
            elif s1[i] > s2[i]:
                return 1
        return 0


solution = Solution()
print(solution.get_dict_order(11,4))
print(solution.get_dict_order(200,25))
