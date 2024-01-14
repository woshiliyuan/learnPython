# coding=utf-8
"""
215. 数组中的第K个最大元素
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

https://leetcode-cn.com/problems/kth-largest-element-in-an-array/
"""
import random
from typing import List


class Solution:
    # 1. 快速排序做法, 据说平均复杂度能到 o(n)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(left, right):
            # 据说加上个随机数，效率高的惊人
            r = random.randint(left, right)
            nums[left], nums[r] = nums[r], nums[left]

            key = nums[left]
            while left < right:
                while left < right and nums[right] < key:
                    right -= 1
                nums[left] = nums[right]

                while left < right and nums[left] >= key:
                    left += 1
                nums[right] = nums[left]

            nums[right] = key
            return left

        def quick_sort(left, right):
            if left < right:
                part_position = partition(left, right)
                if k < part_position + 1:
                    quick_sort(left, part_position - 1)
                elif k > part_position + 1:
                    quick_sort(part_position + 1, right)

        quick_sort(0, len(nums) - 1)
        return nums[k - 1]

    # 2. 堆排序做法 平均复杂度难道是k(logk)?: 建立大顶堆：n + logk,  交换k个数：k(logk);
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        def adjust_heap(i, tree_size):
            j = 2 * i + 1
            if j + 1 < tree_size and nums[j + 1] > nums[j]:
                j += 1
            if j < tree_size and nums[j] > nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
                adjust_heap(j, tree_size)

        length = len(nums)
        # 1. 构建个大顶堆， 如果正常排序后，会是顺序排序的
        for i in range(length // 2 - 1, -1, -1):
            adjust_heap(i, length)

        # 2. 交换顺序，不断输出顶点，换下（k-1）个大树到尾部
        for i in range(length - 1, length - k, -1):
            nums[0], nums[i] = nums[i], nums[0]
            adjust_heap(0, i)
        # print(nums)
        return nums[0]


s = Solution()
# print(s.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5)
# print(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4)
# print(s.findKthLargest([1], 1) == 1)
print(s.findKthLargest([2, 1], 2) == 1)


