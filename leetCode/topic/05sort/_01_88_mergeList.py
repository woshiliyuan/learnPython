# coding=utf-8
"""
88. 合并两个有序数组
给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。
请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。
注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。

https://leetcode-cn.com/problems/merge-sorted-array/
"""
from typing import List


class Solution:
    # 1. 双指针尾部移动法，这样不会覆盖元素
    def merge0(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, p = m - 1, n -1, m + n -1
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[p] = nums1[i]
                i -= 1
            else:
                nums1[p] = nums2[j]
                j -= 1
            p -= 1

        while j >= 0:
            nums1[p] = nums2[j]
            j -= 1
            p -= 1
        # print(nums1)

    # 2. 进化版本; 如果是类似归并排序，新增空间的，就 while l1 and l2吧，原地数组的就while l1 or l2
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, p = m - 1, n -1, m + n -1
        while i >= 0 or j >= 0:
            if j == -1:
                break
            elif i == -1 or nums1[i] < nums2[j]:
                nums1[p] = nums2[j]
                j -= 1
            else:
                nums1[p] = nums1[i]
                i -= 1
            p -= 1

        # print(nums1)


s = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
s.merge(nums1, 3, [2, 5, 6], 3)
print(nums1 == [1, 2, 2, 3, 5, 6])

nums1 = [1]
s.merge(nums1, 1, [], 0)
print(nums1 == [1])

nums1 = [0]
s.merge(nums1, 0, [1], 1)
print(nums1 == [1])
