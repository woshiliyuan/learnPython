# coding=utf-8
"""
221. 最大正方形
在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。

https://leetcode-cn.com/problems/maximal-square/
"""
from typing import List


class Solution:
    # 1. 好像试试暴力破解，待续。。。

    # 2. 动态规划 by myself
    def maximalSquare(self,matrix: List[List[str]]) -> int:
        max_area,row,col = 0,len(matrix),len(matrix[0])

        for i in range(row):
            for j in range(col):
                if i == 0 or j == 0:
                    matrix[i][j] = int(matrix[i][j])
                else:
                    if matrix[i][j] == "0":
                        matrix[i][j] = 0
                    else:
                        matrix[i][j] = min(matrix[i - 1][j - 1],matrix[i - 1][j],matrix[i][j - 1]) + 1

                max_area = max(max_area,matrix[i][j])
        # print(matrix)
        return max_area ** 2

    # 3. 动态规划
    def maximalSquare3(self,matrix: List[List[str]]) -> int:
        pass


s = Solution()
print(s.maximalSquare([["1","0","1","0","0"],
                       ["1","0","1","1","1"],
                       ["1","1","1","1","1"],
                       ["1","0","0","1","0"]]) == 4)
print(s.maximalSquare([["0","1"],["1","0"]]) == 1)
print(s.maximalSquare([["0"]]) == 0)
print(s.maximalSquare([["1"]]) == 1)
# 这个例子真是绝了
print(s.maximalSquare([["0","0","0","1"],
                       ["1","1","0","1"],
                       ["1","1","1","1"],
                       ["0","1","1","1"],
                       ["0","1","1","1"]]) == 9)
print(s.maximalSquare([["1","1"],
                       ["1","1"]]) == 4)
