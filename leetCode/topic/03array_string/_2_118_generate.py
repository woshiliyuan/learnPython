# coding=utf-8
"""
118. 杨辉三角
给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
在「杨辉三角」中，每个数是它左上方和右上方的数的和。

https://leetcode-cn.com/problems/pascals-triangle/
"""
from typing import List


class Solution:
    def generate(self,numRows: int) -> List[List[int]]:
        answer = [[1]]
        for _ in range(numRows - 1):
            temp = [1] + answer[-1]
            for j in range(1,len(temp) - 1):
                temp[j] += temp[j + 1]
            answer.append(temp)
        return answer


s = Solution()
print(s.generate(5) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]])
print(s.generate(1) == [[1]])
