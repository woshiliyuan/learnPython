# coding=utf-8
"""
416. 分割等和子集
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

https://leetcode.cn/problems/partition-equal-subset-sum/
"""
from typing import List


class Solution:
    # 1. 递归求解：数组中是否能相加为 nums/2； o(n* 2**n)
    def canPartition1(self, nums: List[int]) -> bool:
        def find_comb(index, temp_sum):
            nonlocal flag
            if temp_sum == ans:
                flag = True
                return
            if temp_sum > ans or flag: return

            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                find_comb(i + 1, temp_sum + nums[i])

        ans = sum(nums)
        if ans % 2 == 1: return False
        ans = ans // 2

        flag = False
        nums.sort()
        find_comb(0, 0)
        return flag

    # 2. 最后结果为一个值的，必定为动态规划
    def canPartition2(self, nums: List[int]) -> bool:
        target, size = sum(nums), len(nums)
        if target % 2 == 1: return False
        target //= 2

        # 1. 初始值
        dp = [[False] * (target + 1) for _ in range(size)]
        for i in range(size): dp[i][0] = True
        if nums[0] <= target: dp[0][nums[0]] = True
        # dp[i][j]: 在候选集为 [nums[0], ..., nums[i]]的情况下，是否能够求和为j？

        # 2. 选与不选
        for i in range(1, size):
            for j in range(1, target + 1):
                # 一定不选nums[i]
                dp[i][j] = dp[i - 1][j]
                # 一定选nums[i]
                if j >= nums[i] and dp[i - 1][j - nums[i]]:
                    dp[i][j] = True

            if dp[i][-1]:
                return True

        return False

    # 3. 01背包优化成一维数组
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 == 1: return False
        target //= 2

        # 1. 初始值；以后一维数组的初始化，直接这种样式
        dp = [True] + [False] * target
        # 下面循环中不存在dp[i-1]数组越界问题了，所以不用在这儿专门初始化dp[0][num[0]]
        # if nums[0] <= target: dp[nums[0]] = True
        # dp[i][j]: 在候选集为 [nums[0], ..., nums[i]]的情况下，是否能够求和为j？

        # 2. 选与不选
        for i in range(len(nums)):
            for j in range(target, nums[i] - 1, -1):
                # 一定不选nums[i]
                # dp[j] = dp[j]
                # 一定选nums[i]
                if dp[j - nums[i]]: dp[j] = True
                # dp[j] ^= dp[j - nums[i]]

            if dp[-1]: return True

        return False

s = Solution()

print(s.canPartition([100]) is False)
print(s.canPartition([101, 1]) is False)
print(s.canPartition([2, 2]) is True)
print(s.canPartition([1, 2, 5]) is False)
print(s.canPartition([1, 5, 11, 5]))
print(s.canPartition([2, 5, 1, 8]))
print(s.canPartition([1, 6, 11, 6]))
print(s.canPartition([1, 2, 3, 5]) is False)
print(s.canPartition([1, 1, 1, 1]))
print(s.canPartition(
    [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
     100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
     100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
     100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
     100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
     100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
     100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
     100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
     100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 99, 97]) is False)
print(s.canPartition(
    [4, 4, 4, 4, 4, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 12, 12, 12, 12, 12, 12, 12, 12, 16, 16, 16, 16, 16, 16, 16, 16, 20,
     20, 20, 20, 20, 20, 20, 20, 24, 24, 24, 24, 24, 24, 24, 24, 28, 28, 28, 28, 28, 28, 28, 28, 32, 32, 32, 32, 32, 32,
     32, 32, 36, 36, 36, 36, 36, 36, 36, 36, 40, 40, 40, 40, 40, 40, 40, 40, 44, 44, 44, 44, 44, 44, 44, 44, 48, 48, 48,
     48, 48, 48, 48, 48, 52, 52, 52, 52, 52, 52, 52, 52, 56, 56, 56, 56, 56, 56, 56, 56, 60, 60, 60, 60, 60, 60, 60, 60,
     64, 64, 64, 64, 64, 64, 64, 64, 68, 68, 68, 68, 68, 68, 68, 68, 72, 72, 72, 72, 72, 72, 72, 72, 76, 76, 76, 76, 76,
     76, 76, 76, 80, 80, 80, 80, 80, 80, 80, 80, 84, 84, 84, 84, 84, 84, 84, 84, 88, 88, 88, 88, 88, 88, 88, 88, 92, 92,
     92, 92, 92, 92, 92, 92, 96, 96, 96, 96, 96, 96, 96, 96, 97, 99]) is False)
