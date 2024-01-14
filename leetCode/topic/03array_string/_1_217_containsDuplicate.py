# coding=utf-8
"""
217. 存在重复元素
给你一个整数数组 nums 。如果任一值在数组中出现 至少两次 ，返回 true ；如果数组中每个元素互不相同，返回 false 。

https://leetcode-cn.com/problems/contains-duplicate/
"""
from typing import List


class Solution:
    # 1. 排序

    # 2. set
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for num in nums:
            if num in nums_set:
                return True
            else:
                nums_set.add(num)
        return False


s = Solution()
print(s.containsDuplicate([1,2,3,1]))
print(s.containsDuplicate( [1,2,3,4]) is False)
