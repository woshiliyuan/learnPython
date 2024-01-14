# coding=utf-8
"""
448. 找到所有数组中消失的数字
给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数字，并以数组的形式返回结果。

https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array/
"""
from typing import List


class Solution:
    # 1. 申请visited数组记录是否访问过了
    def findDisappearedNumbers1(self, nums: List[int]) -> List[int]:
        visited = [0] * (len(nums) + 1)
        for num in nums:
            visited[num] = 1

        answer = []
        for i in range(1, len(visited)):
            if visited[i] == 0:
                answer.append(i)
        return answer

    # 2. 不使用额外数组记录, 这种做法怎么可能想得到呢？
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length = len(nums)
        for num in nums:
            i = (num - 1) % length
            nums[i] += length

        # answer = [i + 1 for i, num in enumerate(nums) if num <= length]
        answer = []
        for i in range(length):
            if nums[i] <= length:
                answer.append(i + 1)
        return answer


s = Solution()
print(s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6])
print(s.findDisappearedNumbers([1, 1]) == [2])
