# coding=utf-8
"""
75. 颜色分类
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

https://leetcode-cn.com/problems/sort-colors/
"""
from typing import List


class Solution:
    # 计数排序
    def sortColors0(self,nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n0,n1 = 0,0

        for num in nums:
            if num == 0:
                n0 += 1
            elif num == 1:
                n1 += 1

        for i in range(len(nums)):
            if i < n0:
                nums[i] = 0
            elif i < n0 + n1:
                nums[i] = 1
            else:
                nums[i] = 2

        return nums

    def sortColors(self,nums):
        """
            i < p0: 0
            p0 <= i <= p2: 1
            p2 < i: 2
        """
        i,p0,p2 = 0,0,len(nums) - 1
        while i <= p2:
            if nums[i] == 2:
                nums[i],nums[p2] = nums[p2],nums[i]
                p2 -= 1
            else:
                if nums[i] == 0:
                    nums[i],nums[p0] = nums[p0],nums[i]
                    p0 += 1
                i += 1

        return nums

    # 双指针，左右：官方代码
    def sortColors2(self,nums: List[int]) -> None:
        n = len(nums)
        p0,p2 = 0,n - 1
        i = 0
        while i <= p2:
            while i <= p2 and nums[i] == 2:
                nums[i],nums[p2] = nums[p2],nums[i]
                p2 -= 1
            if nums[i] == 0:
                nums[i],nums[p0] = nums[p0],nums[i]
                p0 += 1
            i += 1


solution = Solution()
print(solution.sortColors([2,0,2,1,1,0]))  # [0,0,1,1,2,2]
print(solution.sortColors([2,0,1]))  # [0,1,2]
print(solution.sortColors([0]))  # [0]
print(solution.sortColors([1]))  # [1]
