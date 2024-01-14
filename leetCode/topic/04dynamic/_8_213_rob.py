# coding=utf-8
"""
213. 打家劫舍 II
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。

https://leetcode.cn/problems/house-robber-ii/
"""
from typing import List


class Solution:
    # 1. 动态规划
    # b[i]: 表示[0, i]中可偷取的最大金额，nums[i]可选可不选
    def rob(self,nums: List[int]) -> int:
        size = len(nums)
        if size < 3: return max(nums)

        # 一定选第一个了
        a1,b1 = nums[0],nums[0]
        # 一定不选第一个
        a2,b2 = 0,nums[1]
        for i in range(2,size):
            if i < size - 1:
                a1,b1 = b1,max(nums[i] + a1,b1)
            a2,b2 = b2,max(nums[i] + a2,b2)
        # return max(a1, b1, nums[-1], b2)  # nums[-1] + a2 >= nums[-1]; b1 > =a1
        return max(b1,b2)


s = Solution()
print(s.rob([1,2,3,1]) == 4)
print(s.rob([3,2,1,1]) == 4)
print(s.rob([2,3,2]) == 3)
print(s.rob([1,2,3]) == 3)
print(s.rob([3,2,1]) == 3)
print(s.rob([1]) == 1)
print(s.rob([1,2]) == 2)
print(s.rob([3,2]) == 3)
