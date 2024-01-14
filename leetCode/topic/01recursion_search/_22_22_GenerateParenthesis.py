# coding=utf-8
"""
22. 括号生成
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例 1：
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]

示例 2：
输入：n = 1
输出：["()"]

提示：
1 <= n <= 8
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generate-parentheses
"""
from typing import List


class Solution:
    def generateParenthesis0(self, n: int) -> List[str]:
        result = []

        def generate(left, right, temp_str):
            # 1. 条件终止
            if left == 0 and right == 0:
                result.append(temp_str)
                return
            # 2. 原来遍历所有可能，得使用递归，soga；同样的动作
            if left > 0:
                generate(left - 1, right, temp_str + "(")
            if right > left:
                generate(left, right - 1, temp_str + ")")

        generate(n, n, "")
        return result

    def generateParenthesis(self, n: int) -> List[str]:
        """
        这可不简单，不看答案，一下还想不到，我自己就会这么写，这是在求全排列A(n)

        """
        result = []

        def generate(temp_str):
            # 1. 条件终止, 这样是错误的，递归没法终止
            # if len(temp_str) == 2 * n and valid(temp_str):
            #     result.append(temp_str)
            #     return

            if len(temp_str) == 2 * n:
                if valid(temp_str):
                    result.append(temp_str)
                return

            # 2. 原来遍历所有可能; 不管这样枚举，还是for循环枚举，"(",")"不分先后顺序，就是全排列
            generate(temp_str + "(")
            generate(temp_str + ")")

        # 这个判断方法借鉴的官方，写的真好
        def valid(A):
            bal = 0
            for c in A:
                if c == '(':
                    bal += 1
                else:
                    bal -= 1
                if bal < 0: return False
            return bal == 0

        generate("")
        return result


solution = Solution()
print(solution.generateParenthesis(3))
print(solution.generateParenthesis(1))
print(solution.generateParenthesis(2))
print(solution.generateParenthesis(4))
print(solution.generateParenthesis(5))
