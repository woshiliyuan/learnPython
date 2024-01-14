# coding=utf-8
"""
40. 组合总和 II
给你一个由候选元素组成的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个元素在每个组合中只能使用 一次 。
注意：解集不能包含重复的组合。

https://leetcode-cn.com/problems/combination-sum-ii/
"""

from typing import List

from leetCode.utils.util import equals_array


class Solution:

    def combinationSum20(self, candidates: List[int], target: int) -> List[List[int]]:
        def get_comb(index, temp_list, sum):
            if sum > target:
                return
            if sum == target:
                # 通过判断去重
                if temp_list not in answer:
                    answer.append(temp_list)

            for i in range(index, len(candidates)):
                get_comb(i + 1, temp_list + [candidates[i]], sum + candidates[i])

        answer = []
        candidates.sort()
        get_comb(0, [], 0)
        print(answer)
        return answer

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def get_comb(index, temp_list, sum):
            if sum > target:
                return
            if sum == target:
                answer.append(temp_list)

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                get_comb(i + 1, temp_list + [candidates[i]], sum + candidates[i])

        answer = []
        candidates.sort()
        get_comb(0, [], 0)
        print(answer)
        return answer


solution = Solution()
equals_array(solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8), [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]])
equals_array(solution.combinationSum2([2, 5, 2, 1, 2], 5), [[1, 2, 2], [5]])
equals_array(solution.combinationSum2([1, 1, 1, 2], 3), [[1, 1, 1], [1, 2]])
