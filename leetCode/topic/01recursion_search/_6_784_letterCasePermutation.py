# coding=utf-8
"""
784. 字母大小写全排列
给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。

https://leetcode-cn.com/problems/letter-case-permutation/
"""

from typing import List

from leetCode.utils.util import equals_array


class Solution:

    def letterCasePermutation(self, s: str) -> List[str]:
        def visit_all(i, temp_list):
            if i == size:
                answer.append("".join(temp_list))
                return

            if 'A' <= s[i] <= 'z':
                visit_all(i + 1, temp_list + [s[i].lower()])
                visit_all(i + 1, temp_list + [s[i].upper()])
            else:
                visit_all(i + 1, temp_list + [s[i]])

        answer, size = [], len(s)
        visit_all(0, [])
        # print(answer)
        return answer


solution = Solution()

equals_array(solution.letterCasePermutation("a1b2"), ["a1b2", "a1B2", "A1b2", "A1B2"])
equals_array(solution.letterCasePermutation("3z4"), ["3z4", "3Z4"])
equals_array(solution.letterCasePermutation("12345"), ["12345"])




