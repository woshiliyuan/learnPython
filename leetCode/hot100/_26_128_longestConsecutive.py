# coding=utf-8
"""
128. 最长连续序列
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

https://leetcode-cn.com/problems/longest-consecutive-sequence/
"""
from typing import List


class Solution:
    # 1. 类似计数排序做法，空间换时间
    # 对于样例 [0,1,2,4,8,5,6,7,9,3,55,88,77,99,999999999]会出现 MemoryError
    # 通过 67/70
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0

        min_num, max_num = min(nums), max(nums)
        scope = [0] * (max_num - min_num + 1)
        for num in nums:
            scope[num - min_num] = 1

        # 验证
        count, temp = 0, 0
        for i in range(len(scope)):
            if scope[i]:
                temp += 1
            else:
                if temp > count:
                    count = temp
                temp = 0
        print(count)
        return max(count, temp)

    # 2. 官方题解： set中查找
    def longestConsecutive(self, nums: List[int]) -> int:
        # 1. set去重
        longest, num_set = 0, set(nums)
        for num in num_set:
            # 2. 如果num-1也在集合中，那没必要这次寻找了
            if num - 1 in num_set:
                continue
            # 3. 不断去匹配next+1是否在集合中
            current, next = 1, num + 1
            while next in num_set:
                current += 1
                next += 1
            longest = max(longest, current)
        # print(longest)
        return longest


s = Solution()

print(s.longestConsecutive([100,4,200,1,3,2]) == 4)

print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]) == 9)

print(s.longestConsecutive([]) == 0)

print(s.longestConsecutive([0,1,2,4,8,5,6,7,9,3,55,88,77,99,999999999]) == 10)

