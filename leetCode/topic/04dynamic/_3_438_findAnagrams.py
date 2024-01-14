# coding=utf-8
"""
438. 找到字符串中所有字母异位词
给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。

https://leetcode.cn/problems/find-all-anagrams-in-a-string/
"""
import collections
from typing import List


class Solution:
    # 1. 暴力破解：o(n * (p_size * log(p_size)) * p_size)
    def findAnagrams1(self,s: str,p: str) -> List[int]:
        p_list = sorted(p)
        size = len(p)
        answer = []
        for i in range(len(s)):
            if sorted(s[i: size + i]) == p_list:
                answer.append(i)
        return answer

    # 2. 一旦成功就值比较单个字符，减少一些比较次数
    # 如果比较到一个相同就滑动窗口移动
    def findAnagrams2(self,s: str,p: str) -> List[int]:
        p_list = sorted(p)
        p_size,s_size = len(p),len(s)
        answer,i = [],0
        while i <= s_size - p_size:
            if sorted(s[i: i + p_size]) == p_list:
                answer.append(i)
                while i + p_size < s_size and s[i] == s[i + p_size]:
                    i += 1
                    answer.append(i)
            i += 1
        # print(answer)
        return answer

    # 3 官方题解代码比较多，但是效率会高些
    # https://leetcode.cn/problems/find-all-anagrams-in-a-string/solution/zhao-dao-zi-fu-chuan-zhong-suo-you-zi-mu-xzin/
    # 官1：比较异位词通过个数
    # 官2：通过个数数组的不同滑动窗口

    # 4. 网友答案，太秀了
    def findAnagrams(self,s: str,p: str) -> List[int]:
        """
        如果遇到没有的字符，high原地等待；
        low++遍历到这个字符后（即low比high多1后），下一次high也会消耗掉这个没有的字符
        """
        cnt = collections.defaultdict(int)
        for c in p: cnt[c] += 1

        lo,hi = 0,0
        res = []
        while hi < len(s):
            if cnt[s[hi]] > 0:
                cnt[s[hi]] -= 1
                hi += 1
                if hi - lo == len(p):
                    res.append(lo)
            else:
                cnt[s[lo]] += 1
                lo += 1
        return res


s = Solution()

# print(s.findAnagrams("cbaebabacd", "abc") == [0, 6])
# print(s.findAnagrams("abab", "ab") == [0, 1, 2])
print(s.findAnagrams("eaeabba","ab") == [3,5])
