# coding=utf-8
"""
461. 汉明距离
两个整数之间的 汉明距离 指的是这两个数字对应二进制位不同的位置的数目。
给你两个整数 x 和 y，计算并返回它们之间的汉明距离。

https://leetcode-cn.com/problems/hamming-distance/
"""


class Solution:
    # 1. 先异或 再除2求个数
    def hammingDistance(self,x: int,y: int) -> int:
        xor = x ^ y
        answer = 0
        while xor != 0:
            # answer += xor % 2
            # xor = xor // 2

            answer += xor & 1
            xor >>= 1

        return answer

    # 2. 进阶版 Brian Kernighan 算法
    def hammingDistance(self,x: int,y: int) -> int:
        xor = x ^ y
        answer = 0
        while xor != 0:
            # x & (x-1) 抹掉右边第一个1
            xor &= xor - 1
            answer += 1

        return answer


s = Solution()
print(s.hammingDistance(1,4) == 2)
print(s.hammingDistance(3,1) == 1)
