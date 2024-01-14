# coding=utf-8
"""
77. 组合
给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
你可以按 任何顺序 返回答案。

https://leetcode-cn.com/problems/combinations/
"""

from typing import List

from leetCode.utils.util import equals_array


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def get_comb(index, temp_list):
            if n + 1 - index + len(temp_list) < k:
                return
            if len(temp_list) == k:
                answer.append(temp_list)
                return

            for i in range(index, n + 1):
                get_comb(i + 1, temp_list + [i])

        answer = []
        get_comb(1, [])
        return answer


solution = Solution()
equals_array(solution.combine(4, 2), [[2, 4], [3, 4], [2, 3], [1, 2], [1, 3], [1, 4]])
# equals_array(solution.combine(5, 3),
#              [[1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 3, 4], [1, 3, 5], [1, 4, 5], [2, 3, 4], [2, 3, 5], [2, 4, 5],
#               [3, 4, 5]])
# equals_array(solution.combine(1, 1), [[1]])
print(solution.combine(4, 2))
