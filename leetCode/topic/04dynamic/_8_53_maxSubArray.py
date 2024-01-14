# coding=utf-8
"""
53. 最大子数组和
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
子数组 是数组中的一个连续部分。

https://leetcode-cn.com/problems/maximum-subarray/
"""
from typing import List


class Solution:
    # 1. 动态规划: 前一个数大于0，加上; nums[i]: 以i为结尾的字符能有的最大和
    def maxSubArray0(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            # 如果之前的nums[i-1]为负数，那么不应加上，nums[i]还是本身
            if nums[i - 1] > 0: nums[i] += nums[i - 1]
        return max(nums)

    # 2. 还是动态规划一样的思想, 记录下answer;
    def maxSubArray2(self, nums: List[int]) -> int:
        answer = nums[0]
        for i in range(1, len(nums)):
            # 这样的复杂度算 o(2n), 还是o(n)呢
            nums[i] = max(nums[i-1] + nums[i], nums[i])
            answer = max(answer, nums[i])
        return answer

    # 2. 贪心算法?：之前和小于0，丢掉; 但是这不就是动态规划思想嘛
    def maxSubArray(self, nums: List[int]) -> int:
        left_sum, answer = nums[0], nums[0]
        for i in range(1, len(nums)):
            if left_sum > 0:
                nums[i] += left_sum
            left_sum = nums[i]
            answer = max(answer, nums[i])
        return answer


s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6)
print(s.maxSubArray([1]) == 1)
print(s.maxSubArray([5, 4, -1, 7, 8]) == 23)
