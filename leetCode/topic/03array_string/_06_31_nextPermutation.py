# coding=utf-8
"""
实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列
（即，组合出下一个更大的整数）。
如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
必须 原地 修改，只允许使用额外常数空间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-permutation
"""
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        我这个写法有bug：
        [1,3,2] -> [3, 1, 2], 1不应该和3交换的，而是应该和2交换的
        12354321 -> 12534321, 3也不应该和5进行交换，而是和4进行交换 12453321
        """
        desc = True
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
                desc = False
                break
        if desc:
            nums.sort()

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        参考题解
        """
        # 0. 判断特殊情况
        if len(nums) < 2:
            return

        # 1. 找到a[i]: 从右往左，第一个开始降序的位置
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:  # 得特别注意=的判断
            i -= 1

        # 如果是 3，2，1；走完第一步，i = -1；nums[-1]就取错了
        if i >= 0:
            # 2. 找到了i后, 从右往左，找a[j]: 第一个比a[i]大的数
            for j in range(len(nums) - 1, i, -1):
                if nums[j] > nums[i]:
                    nums[j], nums[i] = nums[i], nums[j]
                    break

        # 3. 这一步很容易漏掉呀，得排序nums[j:], 而且不能再第二步的for内，因为321进不去第二步
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left + 1, right - 1


solution = Solution()

list = [5, 1, 1]
solution.nextPermutation(list)
print(list)  # [1, 1, 5]

list = [1, 2, 3]
solution.nextPermutation(list)
print(list)  # [1, 3, 2]

list = [3, 2, 1]
solution.nextPermutation(list)
print(list)  # [1,2,3]

list = [1, 1, 5]
solution.nextPermutation(list)
print(list)  # [1, 5, 1]

list = [1]
solution.nextPermutation(list)
print(list)  # [1]

list = [1, 3, 2]
solution.nextPermutation(list)
print(list)  # [2,1,3]

list = [1, 3, 5, 4, 2, 1]
solution.nextPermutation(list)
print(list)  # [1,4,1, 2, 3, 5]
