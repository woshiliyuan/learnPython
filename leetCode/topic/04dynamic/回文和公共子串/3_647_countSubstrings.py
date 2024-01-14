# coding=utf-8
"""
647. 回文子串
给你一个字符串 s ，请你统计并返回这个字符串中 回文子串 的数目。
回文字符串 是正着读和倒过来读一样的字符串。
子字符串 是字符串中的由连续字符组成的一个序列。
具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。
https://leetcode.cn/problems/palindromic-substrings/
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        # i从左扩散，j从右扩散
        def spread_count(i, j):
            count = 0
            while i >= 0 and j < len(s) and s[i] == s[j]:
                count += 1
                i, j = i - 1, j + 1
            return count

        count = 0
        for i in range(len(s)):
            # 以center为中心，奇数长度的回文个数
            count += spread_count(i - 1, i + 1)
            # 以center为中心，偶数长度的回文个数：为了不重复，i只做左边的中心
            count += spread_count(i, i + 1)
        return count + len(s)


s = Solution()
print(s.countSubstrings("abc") == 3)
print(s.countSubstrings("aaa") == 6)
print(s.countSubstrings("fdsklf") == 6)

