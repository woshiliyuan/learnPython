# coding=utf-8
"""
238. 除自身以外数组的乘积
给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。
题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。
请不要使用除法，且在 O(n) 时间复杂度内完成此题。

https://leetcode-cn.com/problems/product-of-array-except-self/
"""
from typing import List


class Solution:
    # 1. 额外一个逆序乘积数组
    def productExceptSelf0(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left_prod, desc_prod = nums[0], nums.copy()
        for i in range(length - 2, 0, -1):
            desc_prod[i] *= desc_prod[i + 1]

        nums[0] = desc_prod[1]
        for i in range(1, length - 1):
            temp = nums[i]
            nums[i] = left_prod * desc_prod[i + 1]
            left_prod *= temp
        nums[-1] = left_prod
        print(nums)
        return nums

    # 官方题解，其实与我的方法一思想一样，只是题目默认输出数组重写接收结果, 这就算所谓的o(1)空间复杂度？
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left_prod, desc_prod = 1, nums.copy()
        for i in range(length - 2, 0, -1):
            desc_prod[i] *= desc_prod[i + 1]

        for i in range(0, length - 1):
            desc_prod[i] = left_prod * desc_prod[i + 1]
            left_prod *= nums[i]
        desc_prod[-1] = left_prod
        print(desc_prod)
        return desc_prod

    # 2. 递归
    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        def right_product(left_prod, i):
            temp = nums[i]
            if i == len(nums) - 1:
                nums[i] = left_prod
                return temp

            right_prod = right_product(left_prod * temp, i + 1)
            nums[i] = left_prod * right_prod
            return temp * right_prod

        right_product(1, 0)
        print(nums)
        return nums


s = Solution()
print(s.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6])
print(s.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0])
print(s.productExceptSelf([2, 3]) == [3, 2])
