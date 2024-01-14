# coding=utf-8
"""
47. 全排列 II
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

https://leetcode-cn.com/problems/permutations-ii/
"""

from typing import List

from leetCode.utils.util import equals_array


class Solution:

    def permutation(self, s: str) -> List[str]:
        def visit_all(temp_list):
            if len(temp_list) == len(s_list):
                answer.append("".join(temp_list))
                return

            for i in range(len(s_list)):
                if i > 0 and s_list[i] == s_list[i-1] and visited[i-1] == 0:
                    continue
                if visited[i] == 1:
                    continue

                visited[i] = 1
                visit_all(temp_list + [s_list[i]])
                visited[i] = 0

        answer, visited = [], [0] * len(s)
        s_list = sorted(s)
        visit_all([])
        print(answer)
        return answer


solution = Solution()
equals_array(solution.permutation("abc"), ["abc","acb","bac","bca","cab","cba"])
equals_array(solution.permutation("abac"), ['aabc', 'aacb', 'abac', 'abca', 'acab', 'acba', 'baac', 'baca', 'bcaa', 'caab', 'caba', 'cbaa'])



