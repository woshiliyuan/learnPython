# coding=utf-8
"""
740. 删除并获得点数
给你一个整数数组 nums ，你可以对它进行一些操作。
每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除 所有 等于 nums[i] - 1 和 nums[i] + 1 的元素。
开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。

https://leetcode.cn/problems/delete-and-earn/
"""
from typing import List


class Solution:
    # 1. 动态规划 申请 [0] * (max_num + 1)的数组
    def deleteAndEarn1(self, nums: List[int]) -> int:
        max_num = max(nums)
        total = [0] * (max_num + 1)
        for n in nums:
            total[n] += 1

        for i in range(2, max_num + 1):
            total[i] = max(total[i] * i + total[i - 2], total[i - 1])
        # print(total)
        return total[-1]

    # 2. 动态规划； 排序, 连续的数组符合rob, 可以传入计算
    def deleteAndEarn(self, nums: List[int]) -> int:
        def rob(total: List[int]):
            size = len(total)
            if size >= 2: total[1] = max(total[0], total[1])
            for i in range(2, size):
                total[i] = max(total[i - 1], total[i] + total[i - 2])
            return total[-1]

        nums.sort()
        answer, total = 0, [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                total[-1] += nums[i]
            elif nums[i] == nums[i -1] + 1:
                total.append(nums[i])
            # 找到了不连续数组了
            else:
                answer += rob(total)
                total = [nums[i]]

        # 最后剩余的total也得算一次
        answer += rob(total)
        return answer


s = Solution()
print(s.deleteAndEarn([3, 4, 2]) == 6)
print(s.deleteAndEarn([2, 2, 3, 3, 3, 4]) == 9)
print(s.deleteAndEarn([2]) == 2)
print(s.deleteAndEarn([2, 10]) == 12)
print(s.deleteAndEarn([2, 4]) == 6)
print(s.deleteAndEarn([2, 2, 3]) == 4)
print(s.deleteAndEarn([2, 2, 3000]) == 3004)
