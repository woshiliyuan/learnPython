# coding=utf-8
"""
给定一个仅包含数字2-9的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例 1：
输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]

示例 2：
输入：digits = ""
输出：[]

示例 3：
输入：digits = "2"
输出：["a","b","c"]

链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
"""
from typing import List


class Solution:
    def letterCombinations(self,digits: str) -> List[str]:
        """
        递归，深度搜索法，回溯法
        :param digits:
        :return:
        """
        result = []
        phone_map = {
            "2": "abc","3": "def",
            "4": "ghi","5": "jkl","6": "mno",
            "7": "pqrs","8": "tuv","9": "wxyz"
        }

        # 也可以这么定义， phones[int(digital[i])]  phones[ord(digital[i]) - 48]
        # phones = ['', '', 'abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']

        def dfs(i,comb):
            if i == len(digits):
                result.append(comb)
                return

            for letter in phone_map[digits[i]]:
                dfs(i + 1,comb + letter)

        # 专门为了 "" -> []
        if digits != "": dfs(0,"")
        return result

    def letterCombinations1(self,digits: str) -> List[str]:
        """
        广度遍历，采用队列, 写法太精妙了
        作者：z1m
        链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/solution/hui-su-dui-lie-tu-jie-by-ml-zimingmeng/
        :param digits:
        :return:
        """
        if not digits: return []
        phone = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        queue = ['']  # 初始化队列， 这个也太太太巧妙了吧
        for digit in digits:
            # 有树的层序遍历的感觉
            for _ in range(len(queue)):
                tmp = queue.pop(0)
                for letter in phone[ord(digit) - 50]:  # 这里我们不使用 int() 转换字符串，使用ASCII码
                    queue.append(tmp + letter)
        return queue


solution = Solution()
# print(solution.letterCombinations("23") == ["ad","ae","af","bd","be","bf","cd","ce","cf"])
# print(solution.letterCombinations("2") == ["a","b","c"])
# print(solution.letterCombinations("234"))
print(solution.letterCombinations("") == [])  # 需要 [], 而不是 [""]
# print(solution.letterCombinations("233"))
# print(solution.letterCombinations("2345"))
