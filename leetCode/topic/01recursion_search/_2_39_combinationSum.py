# coding=utf-8
"""
组合总和
给定一个无重复元素的正整数数组candidates和一个正整数target，找出candidates中所有可以使数字和为目标数target的唯一组合。
candidates中的数字可以无限制重复被选取。如果至少一个所选数字数量不同，则两种组合是唯一的。

链接：https://leetcode-cn.com/problems/combination-sum
"""
from typing import List


class Solution:
    def combinationSum0(self, candidates: List[int], target: int) -> List[List[int]]:
        def get_result(rest, index, temp_list: List):
            # 1. 递归终止条件。可以写在开始，也可以嵌入for循环里面判断
            if rest < 0:
                return
            if rest == 0:
                result.append(temp_list)
                return

            # 2. 遍历所有可能
            for i in range(index, len(candidates)):
                get_result(rest - candidates[i], i, temp_list + [candidates[i]])

                # 这样改变的是引用对象，递归的参数得时刻生成新对象，因为同一个for循环的下一次还是得使用原值temp_list
                # temp_list.append(candidates[i])
                # get_result(rest - candidates[i], i, temp_list)

                # 如果这个题目换一下，变成candidates中的数字只能选一次呢？ []
                # get_result(rest - candidates[i], i+1, temp_list + [candidates[i]])

        result = []
        get_result(target, 0, [])
        return result

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        队列方式应该怎么做呢？
        """
        # 1. 构建字母和下标的映射
        letter_index_map = {}
        for i in range(len(candidates)):
            letter_index_map[candidates[i]] = i

        result = []
        queue = [[]]  # 初始化队列
        while len(queue) > 0:
            tmp = queue.pop(0)
            start = 0
            if len(tmp) > 0:
                start = letter_index_map[tmp[-1]]

            for i in range(start, len(candidates)):
                temp_sum = sum(tmp) + candidates[i]
                if temp_sum < target:
                    queue.append(tmp + [candidates[i]])
                elif temp_sum == target:
                    result.append(tmp + [candidates[i]])
        return result


solution = Solution()
print(solution.combinationSum([2, 3, 6, 7], 7))  # [[7],[2,2,3]]
print(solution.combinationSum([2, 3, 5], 8))  # [[2,2,2,2],[2,3,3],[3,5]]
print(solution.combinationSum([1], 1))  # [[1]]
print(solution.combinationSum([2], 1))  # []
print(str(solution.combinationSum([1], 2)))  # [[1,1]]
