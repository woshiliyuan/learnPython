# coding=utf-8
"""
78. 子集
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

https://leetcode-cn.com/problems/subsets/
"""
from typing import List


class Solution:
    def subsets0(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def get_sub(index, temp_list):
            answer.append(temp_list)
            # 这一句可以省略，下面的for循环有做index限制 & 这是再遍历所有数据
            # if index == len(nums):
            #     return

            for i in range(index, len(nums)):
                get_sub(i + 1, temp_list + [nums[i]])

        answer = []
        get_sub(0, [])
        return answer

    # 01记录回溯结果
    def subsets1(self, nums):
        def get_sub(index):
            if index == size:
                temp_list = []
                for i in range(size):
                    if record[i] == 1:
                        temp_list.append(nums[i])
                answer.append(temp_list)
                return

            record[index] = 1
            get_sub(index + 1)
            record[index] = 0
            get_sub(index + 1)

        size = len(nums)
        answer, record = [], [0] * size
        get_sub(0)
        return answer

    # 回溯算法，对结果保存的优化版本
    def subsets2(self, nums):
        def get_sub(index):
            if index == len(nums):
                answer.append(temp_list + [])
                return

            temp_list.append(nums[index])
            get_sub(index + 1)
            temp_list.pop()
            get_sub(index + 1)

        answer, temp_list = [], []
        get_sub(0)
        return answer

    # https://leetcode-cn.com/problems/subsets/solution/hui-su-suan-fa-by-powcai-5/
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            print([num + [i] for num in res])
            res += [num + [i] for num in res]
        return res


solution = Solution()
print(solution.subsets0([1, 2, 3]))  # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
print(solution.subsets([0]))  # [[],[0]]


# 按位与操作
def move_left():
    n = 3
    for mask in range(1 << n):
        print(mask)
        for i in range(n):
            b = 1 << i
            print(" ", b, mask & b)
# move_left()
