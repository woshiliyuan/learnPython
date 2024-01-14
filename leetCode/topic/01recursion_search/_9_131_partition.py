# coding=utf-8
"""
131. 分割回文串
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
回文串 是正着读和反着读都一样的字符串。

https://leetcode-cn.com/problems/palindrome-partitioning/
"""

from typing import List

from leetCode.utils.util import equals_array


class Solution:
    # for 回溯写法
    def partition(self, s: str) -> List[List[str]]:
        def visit_all0(index, temp_list):
            if index >= len(s):
                answer.append(temp_list)
                return

            # 可以不剪枝，range中不关联index; 但是拿到结果后得return, 否则会死循环
            # 取数组a[i]: range(len(a)); 如果是截取字符串，则是：s[i, len(a)+1)]
            # 而且会添加进去重复字符串："aa" -> [['a', 'a'], ['a', 'a'], ['aa']]
            for step in range(1, len(s) + 1):
                temp_s = s[index: index + step]
                visit_all(index + step, temp_list + [temp_s])

        def visit_all(index, temp_list):
            if index == len(s):
                answer.append(temp_list)

            for step in range(1, len(s) - index + 1):
                temp_s = s[index: index + step]
                if is_huiwen(temp_s):
                    visit_all(index + step, temp_list + [temp_s])

        def is_huiwen(son_str: str):
            length = len(son_str)
            for i in range(len(son_str)//2):
                if son_str[i] != son_str[length-1-i]:
                    return False
            return True

        answer = []
        visit_all(0, [])
        # print(answer)
        return answer

    # visited 回溯写法？ 写不来... 没法列举所有steps
    # 难道visited只能适合0，1两种情况的?
    def partition1(self, s: str) -> List[List[str]]:
        def visit_all(index, temp_list):
            if index >= len(s):
                answer.append(temp_list)

            step = 1
            temp_s = s[index: index + step]
            visit_all(index + step, temp_list + [temp_s])

        def is_huiwen(son_str: str):
            length = len(son_str)
            for i in range(len(son_str)//2):
                if son_str[i] != son_str[length-1-i]:
                    return False
            return True

        answer = []
        visit_all(0, [])
        # print(answer)
        return answer


solution = Solution()

# solution.partition("aab")
equals_array(solution.partition("aab"), [["a","a","b"],["aa","b"]])
equals_array(solution.partition("aabab"), [["a","a","b","a","b"],["a","a","bab"],["a","aba","b"],["aa","b","a","b"],["aa","bab"]])
equals_array(solution.partition("a"), [["a"]])
equals_array(solution.partition("aa"), [['a', 'a'], ['aa']])



