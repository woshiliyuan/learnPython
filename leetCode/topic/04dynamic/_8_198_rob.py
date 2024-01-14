# coding=utf-8
"""
198. 打家劫舍
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

https://leetcode-cn.com/problems/house-robber/
"""
import functools
from typing import List


class Solution:
    # 1. 递归
    # 1.1 向前遍历：暴力破击
    def rob0(self,nums: List[int]) -> int:
        def visit(index,temp_sum):
            nonlocal max_sum
            if index >= length:
                max_sum = max(max_sum,temp_sum)
                return

            for i in range(index,length):
                visit(i + 2,temp_sum + nums[i])

        max_sum,length = 0,len(nums)
        visit(0,0)
        return max_sum

    # 1.2 从后往前递归
    @functools.lru_cache()  # TypeError: unhashable type: 'list'
    def rob1(self,nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]

        # 因为数组取了nums[-2], 所以在特殊判断(len==0 || len==1)
        return max(self.rob(nums[:-2]) + nums[-1],self.rob(nums[:-3]) + nums[-2])

    def rob1(self,nums: List[int]) -> int:
        @functools.lru_cache(len(nums))
        def rob_end(i):
            if i < 1: return 0
            if i == 1: return nums[0]
            return max(nums[i - 1] + rob_end(i - 2),nums[i - 2] + rob_end(i - 3))

        return rob_end(len(nums))

    # 2. 动态规划
    # 2.1. o(n^2)。 nums[i]: 抢到第i家结尾最大金额是多少。第i家一定抢了的
    def rob2(self,nums: List[int]) -> int:
        for i in range(2,len(nums)):
            nums[i] = nums[i] + max(nums[:i - 1])
        return max(nums[-2:])

    # 2.1 o(n). 澜澜老师的想法； 同上一个方法; nums[i]都表示i一定选了, 以i结尾的
    def rob2(self,nums: List[int]) -> int:
        a,b = 0,nums[0]
        for i in range(2,len(nums)):
            # max(nums[:i - 1])只能出现在倒数两个：nums[i-2], nums[i-3]; nums[i-2] > nums[i-4]
            nums[i] = nums[i] + max(a,b)
            a,b = nums[i - 2],nums[i - 1]
        return max(b,nums[-1])

    # 2.1 还是同上一个做法:
    # max(nums[:i - 1])只能出现在倒数两个：nums[i-2], nums[i-3]; nums[i-2] > nums[i-4]
    def rob2(self,nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        if len(nums) >= 3: nums[2] += nums[0]

        for i in range(3,len(nums)):
            nums[i] = nums[i] + max(nums[i - 2],nums[i - 3])

        return max(nums[-2],nums[-1])

    # 2.2. o(n). nums[i]: [0-i]家店铺选择，能抢到的最多，i可选可不选
    def rob3(self,nums: List[int]) -> int:
        if len(nums) > 1:
            nums[1] = max(nums[1],nums[0])
        for i in range(2,len(nums)):
            nums[i] = max(nums[i] + nums[i - 2],nums[i - 1])
        return nums[-1]


s = Solution()
print(s.rob([2]) == 2)
print(s.rob([2,1]) == 2)
print(s.rob([2,3,2]) == 4)
print(s.rob([2,1,1,2]) == 4)
print(s.rob([1,2,3,1]) == 4)
print(s.rob([2,7,9,3,1]) == 12)
print(s.rob([2,7,1,9,3,1,4]) == 20)
