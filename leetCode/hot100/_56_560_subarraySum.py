# coding=utf-8
"""
560. 和为 K 的子数组
给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的连续子数组的个数 。

https://leetcode.cn/problems/subarray-sum-equals-k/
"""
import collections
from typing import List


class Solution:
    # 1. 暴力破解, o(n^2) 超时
    def subarraySum1(self,nums: List[int],k: int) -> int:
        count,length = 0,len(nums)
        for i in range(length):
            array_sum = 0
            for j in range(i,length):
                # 一定以i开头, j结尾的  [i, j]
                array_sum += nums[j]
                if array_sum == k:
                    count += 1
        return count

    # 2. 前缀和 + 哈希set优化; o(n) time, o(1) space
    # 使用set是错误的，过不了这个例子： ([1, -1, 0], 0) == 3, 因为以0结尾有两个组合是可用的：1,-1,0; 0
    # 如果题目为：是否存在连续子数组，和为k，这个解法非常合适
    def subarraySum2(self,nums: List[int],k: int) -> int:
        """
        pre[i]: nums[0:i] 包括i的前缀和
        pre[i] = pre[i - 1] + nums[i]

        pre[i] = pre[j] + k，如果本事成立，说明：[j+1, i]之和为k
        """
        exit_pre = {0}
        pre,count = 0,0
        for num in nums:
            pre += num
            # 这样其实只是在计算以i结尾，是否存在解，忽略了个数
            if (pre - k) in exit_pre:
                count += 1
            exit_pre.add(pre)
        return count

    # 使用dict
    def subarraySum(self,nums: List[int],k: int) -> int:
        exit_pre = collections.defaultdict(int)
        exit_pre[0] = 1
        pre,count = 0,0
        for num in nums:
            pre += num
            count += exit_pre[pre - k]
            exit_pre[pre] += 1
        return count

    # 3. 滑动窗口是否可行？
    def subarraySum3(self,nums: List[int],k: int) -> int:
        pass


s = Solution()
print(s.subarraySum([1,1,1],2) == 2)
print(s.subarraySum([1,2,3],3) == 2)
print(s.subarraySum([1,2,3],4) == 0)
print(s.subarraySum([1,2,4,-4],3) == 2)
print(s.subarraySum([1,-1,0],0) == 3)
