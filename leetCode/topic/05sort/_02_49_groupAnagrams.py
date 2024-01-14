# coding=utf-8
"""
49. 字母异位词分组
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母通常恰好只用一次。

https://leetcode-cn.com/problems/group-anagrams/
"""
import collections
from typing import List


class Solution:
    # 我自己的做法, o(n* k*logk), k是单个字符串长度
    def groupAnagrams(self,strs: List[str]) -> List[List[str]]:
        dict = collections.defaultdict(list)
        for item in strs:
            key = "".join(sorted(item))
            dict[key].append(item)

        return list(dict.values())

    # 官方2: key值不排序，计数
    def groupAnagrams2(self,strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)
        for st in strs:
            counts = [0] * 26
            for ch in st:
                counts[ord(ch) - ord("a")] += 1
            # 需要将 list 转换成 tuple 才能进行哈希
            mp[tuple(counts)].append(st)

        return list(mp.values())


solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))  # [["bat"],["nat","tan"],["ate","eat","tea"]]
print(solution.groupAnagrams([""]))  # [[""]]
print(solution.groupAnagrams(["a"]))  # [["a"]]

print("".join(sorted("bac")))
