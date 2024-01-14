# coding=utf-8
"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。

链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
"""
from typing import List


class Solution:
    # 1. 直接扫描一遍，o(n)复杂度
    def searchRange0(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]
        for i in range(len(nums)):
            if nums[i] == target:
                if result[0] == -1:
                    result[0], result[1] = i, i
                else:
                    result[1] = i
        return result

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                result[0], result[1] = middle, middle

                # 貌似官方题解不是我这么解的，左右边界继续用的二分查找法
                # 寻找右边边界
                for index in range(middle + 1, len(nums)):
                    if nums[index] == target:
                        result[1] = index
                    else:
                        break
                # 寻找左边边界
                for index in range(middle - 1, -1, -1):
                    if nums[index] == target:
                        result[0] = index
                    else:
                        break
                return result

            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return result


solution = Solution()
print(solution.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4])  # [3, 4]
print(solution.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1])  # [-1, -1]
print(solution.searchRange([], 8) == [-1, -1])  # [-1, -1]
print(solution.searchRange([5, 6, 8, 9], 8) == [2, 2])  # [2, 2]
print(solution.searchRange([5, 6, 8, 8, 8, 8, 8, 10], 8) == [2, 6])  # [2, 6]
