# coding=utf-8
"""
139. 单词拆分
给你一个字符串 s 和一个字符串列表 wordDict 作为字典。请你判断是否可以利用字典中出现的单词拼接出 s 。
注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。

https://leetcode-cn.com/problems/word-break/
"""
from typing import List


class Solution:
    # 1. 递归，超时
    def wordBreak0(self, s: str, wordDict: List[str]) -> bool:
        def visit(rest_str: str):
            nonlocal flag
            for word in wordDict:
                if rest_str == word:
                    flag = True
                    return
                if rest_str.startswith(word):
                    visit(rest_str[len(word):])

        flag = False
        wordDict.sort(key=lambda w: len(w), reverse=True)
        print(wordDict)
        visit(s)
        return flag

    # 2. 官方题解。这种最后结果为boolean | 数值n, 难道都是动态规划？
    def wordBreak1(self, s: str, wordDict: List[str]) -> bool:
        word_set, size = set(wordDict), len(s)
        # break_flags[i]表示s[0:i-1]可拆分，截取字符串的还能这么玩，退一位？s[j:i]就表示[j, i-1]
        break_flags = [False] * (size + 1)
        break_flags[0] = True # 思维太巧妙了吧
        # 循环的灵界条件判断的真赞
        for i in range(1, size + 1):
            # 1. j只需要到i-1即可
            for j in range(i):
                # 2. s只需要截取到[j,i-1]即可
                if break_flags[j] and s[j:i] in word_set:
                    break_flags[i] = True
                    break
        return break_flags[-1]

    # 3. 边界问题再修改, 还是习惯这种
    # 1. range, s[i:j]包头不包尾巴，2: 0，end，中间各举一个例子
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set, size = set(wordDict), len(s)
        # break_flags[i]表示s[0:i]可拆分
        break_flags = [False] * size
        for i in range(size):
            # range包头，不包尾，所以i+1, 否则i=0进不来
            for j in range(i+1):
                # j==0特殊判断 & 字符串截取包头不包尾，所以i+1
                if (j == 0 or break_flags[j - 1]) and s[j: i+1] in word_set:
                    break_flags[i] = True
                    break
        return break_flags[-1]


s = Solution()
print(s.wordBreak("leetcode", ["leet", "code"]) is True)
print(s.wordBreak("l", ["leet", "code", 'l']) is True)
print(s.wordBreak("l", ["leet", "code", 'a']) is False)
print(s.wordBreak("leet", ["lee", "code", 't']) is True)
print(s.wordBreak("applepenapple", ["apple", "pen"]) is True)
print(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False)
print(s.wordBreak(
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
    ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]) is False)
