# coding=utf-8
"""
3. 无重复字符的最长子串
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
"""


class Solution:
    # 1. 暴力破解：枚举以i开头的不重复字符串
    def lengthOfLongestSubstring1(self, s: str) -> int:
        max_len, length = 0, len(s)
        for i in range(length):
            temp_set, j = {s[i]}, i + 1
            while j < length and s[j] not in temp_set:
                temp_set.add(s[j])
                j += 1
            max_len = max(max_len, len(temp_set))
        return max_len

    # 2. 滑动窗口; 实际上是对上面暴力破解的j的优化，省去了很多重复判断：s[i, j]为不重复字符串，那么s[i+1, j]必定也是
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len, length = 0, len(s)
        window_set, j = set(), 0
        for i in range(length):
            if i > 0:
                window_set.remove(s[i - 1])
            while j < length and s[j] not in window_set:
                window_set.add(s[j])
                j += 1
            max_len = max(max_len, j - i)
        # print(max_len)
        return max_len


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb") == 3)
print(s.lengthOfLongestSubstring("bbbbb") == 1)
print(s.lengthOfLongestSubstring("pwwkew") == 3)
print(s.lengthOfLongestSubstring("a") == 1)
print(s.lengthOfLongestSubstring("") == 0)

