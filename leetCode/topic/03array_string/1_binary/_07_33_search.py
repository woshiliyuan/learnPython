# coding=utf-8
"""
给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，
则返回它的下标，否则返回 -1 。

https://leetcode-cn.com/problems/search-in-rotated-sorted-array/
"""
from typing import List


class Solution:
    def search0(self,nums: List[int],target: int) -> int:
        try:
            return nums.index(target)
        except:
            return -1

    def search1(self,nums: List[int],target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1

    def search(self,nums: List[int],target: int) -> int:
        """
        对于有序数组的搜索，估计最优的就是二分查找法了
        有序数组的逆序，双指针法
        """
        left,right = 0,len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # 说明左半边都是被旋转了, 这个等号也太玄机了吧，[3, 1], 1  只能进这个循环？
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # 说明右半边都是升序的，旋转的最大值一定on左边
            else:
                if nums[mid] < target <= nums[-1]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


solution = Solution()
print(solution.search([4,5,6,7,0,1,2],0) == 4)  # 4
# print(solution.search([4, 5, 6, 7, 0, 1, 2], 3) == -1)  # -1
# print(solution.search([4, 5, 6, 7, 0, 1, 2], 4) == 0)  # 0
# print(solution.search([1], 0) == -1)  # -1
# print(solution.search([1], 1) == 0)  # 0
# print(solution.search([3, 1], 1) == 1)  # 1
# print(solution.search([3, 1], 3) == 0)  # 0
