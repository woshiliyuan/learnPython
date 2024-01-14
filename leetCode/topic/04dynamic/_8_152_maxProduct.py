# coding=utf-8
"""
152. 乘积最大子数组
给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
测试用例的答案是一个 32-位 整数。
子数组 是数组的连续子序列。

https://leetcode-cn.com/problems/maximum-product-subarray/
"""
from typing import List


class Solution:
    # 做成了[数字]的连续子序列, 暴力破解, 文不对题
    def maxProduct0(self,nums: List[int]) -> int:
        max_pro,length = nums[0],len(nums)
        for i in range(length):
            temp_max = nums[i]
            for j in range(i + 1,length):
                if nums[j] == nums[j - 1] + 1:
                    temp_max *= nums[j]
                else:
                    break
            max_pro = max(max_pro,temp_max)
        print(max_pro)
        return max_pro

    # 1. 动态规划
    # 1.1 记录一个最大值，最小值；需要两个数组记录状态
    def maxProduct1(self,nums: List[int]) -> int:
        size = len(nums)
        arr_max,min_max = [nums[0]] * size,[nums[0]] * size
        for i in range(1,size):
            arr_max[i] = max(arr_max[i - 1] * nums[i],min_max[i - 1] * nums[i],nums[i])
            min_max[i] = min(arr_max[i - 1] * nums[i],min_max[i - 1] * nums[i],nums[i])
        return max(arr_max)

    # 1.2 但是这种只和前一个arr_max[i - 1]有关，和arr_max[i - 2]美观的，都可以空间节省为一个数值
    def maxProduct(self,nums: List[int]) -> int:
        answer = last_max = last_min = nums[0]
        for i in range(1,len(nums)):
            num,temp_max = nums[i],last_max
            last_max = max(num,num * last_max,num * last_min)
            last_min = min(num,num * temp_max,num * last_min)
            answer = max(last_max,answer)
        return answer

    # 神奇思想：https://leetcode-cn.com/problems/maximum-product-subarray/solution/duo-chong-si-lu-qiu-jie-by-powcai-3/
    def maxProduct2(self,nums: List[int]) -> int:
        """
        根据符号的个数 [^2]
        1. 当负数个数为偶数时候，全部相乘一定最大
        2. 当负数个数为奇数时候，取左边第一个负数右边 || 右边第一个负数的左边
        3. 当有 0 情况，重置为本身
        """
        reverse_nums = nums[::-1]
        for i in range(1,len(nums)):
            # 正序表示以i结尾的字符，最大乘积是多少
            nums[i] *= nums[i - 1] or 1
            # 逆序表示以i为开头的字符，最大乘积是多少
            reverse_nums[i] *= reverse_nums[i - 1] or 1
        return max(nums + reverse_nums)


s = Solution()
print(s.maxProduct([5,-2,0,-3,4]) == 5)
print(s.maxProduct([5,6,-3,4]) == 30)
print(s.maxProduct([5,6,-3,4,-3]) == 1080)
print(s.maxProduct([2,3,-2,4]) == 6)
print(s.maxProduct([-2,0,-1]) == 0)
print(s.maxProduct([-3,-1,-1]) == 3)
print(s.maxProduct([-4,-3,-2]) == 12)
