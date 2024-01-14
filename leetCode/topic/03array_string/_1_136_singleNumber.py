# coding=utf-8
"""
136. 只出现一次的数字
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

https://leetcode-cn.com/problems/single-number/
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        for num in nums:
            answer ^= num
        return answer


s = Solution()
print(s.singleNumber([2,2,1]) == 1)
print(s.singleNumber([4,1,2,1,2]) == 4)
