# coding=utf-8
"""
46. 全排列
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
"""
from typing import List

from leetCode.utils.util import equals_array


class Solution:
    def permute1(self, nums: List[int]) -> List[List[int]]:
        def visit(nums, temp_list):
            if len(nums) == 0:
                result.append(temp_list)
                return
            for i in range(len(nums)):
                temp_nums = nums.copy()
                temp_nums.pop(i)
                visit(temp_nums, temp_list + [nums[i]])

        result = []
        visit(nums, [])
        return result

    def permute2(self, nums: List[int]) -> List[List[int]]:
        def visit(temp_list):
            if len(temp_list) == len(nums):
                result.append(temp_list)
                return

            for i in range(len(nums)):
                if visited[i] == 1:
                    continue

                visited[i] = 1
                visit(temp_list + [nums[i]])
                visited[i] = 0

        result, visited = [], [0] * len(nums)
        visit([])
        return result

    # 2022-06-25的错误示范
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(index, temp_list):
            if len(temp_list) == len(nums):
                answer.append(temp_list)
                return

            # for i in range(0, len(nums)):
            # 如果i>=index, [1, 3, 2]只会出现顺序[1, 3, 2], 往后的顺序，当第一个是3时，不可能还往前遍历出现3，1，2
            for i in range(index, len(nums)):
                if visited[i]: continue
                visited[i] = 1
                dfs(i + 1, temp_list + [nums[i]])
                visited[i] = 0

        answer, visited = [], [0] * len(nums)
        dfs(0, [])
        return answer


s = Solution()
print(s.permute([1, 2, 3]))
print(s.permute([1, 3, 2]))
equals_array(s.permute([1, 2, 3]), [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])
equals_array(s.permute([0, 1]), [[0, 1], [1, 0]])
equals_array(s.permute([1]), [[1]])
equals_array(s.permute([1, 2, 3, 5]), [[1, 2, 3, 5], [1, 2, 5, 3], [1, 3, 2, 5], [1, 3, 5, 2], [1, 5, 2, 3], [1, 5, 3, 2], [2, 1, 3, 5], [2, 1, 5, 3], [2, 3, 1, 5], [2, 3, 5, 1], [2, 5, 1, 3], [2, 5, 3, 1], [3, 1, 2, 5], [3, 1, 5, 2], [3, 2, 1, 5], [3, 2, 5, 1], [3, 5, 1, 2], [3, 5, 2, 1], [5, 1, 2, 3], [5, 1, 3, 2], [5, 2, 1, 3], [5, 2, 3, 1], [5, 3, 1, 2], [5, 3, 2, 1]])