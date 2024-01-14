# coding=utf-8
"""
通配符匹配：
给定一个字符串(s) 和一个字符模式(p) ，实现一个支持'?'和'*'的通配符匹配。
'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:
s可能为空，且只包含从a-z的小写字母。
p可能为空，且只包含从a-z的小写字母，以及字符?和*。

示例1:
输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。

示例2:
输入:
s = "aa"
p = "*"
输出: true
解释:'*' 可以匹配任意字符串。

示例3:
输入:
s = "cb"
p = "?a"
输出: false
解释:'?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。

示例4:
输入:
s = "adceb"
p = "*a*b"
输出: true
解释:第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".

示例5:
输入:
s = "acdcb"
p = "a*c?b"
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/wildcard-matching
"""


class Solution0:
    """
        自己的写法，失败于："abceb", "*b"
    """

    def isMatch(self,s: str,p: str) -> bool:
        i = j = 0
        last_is_star = False
        while i < len(s):
            if j < len(p) and p[j] == "*":
                j += 1
                last_is_star = True
            elif j < len(p) and (p[j] == "?" or p[j] == s[i]):
                i,j = i + 1,j + 1
                last_is_star = False
            elif last_is_star:
                i += 1
            else:
                return False

        if i == len(s) and j == len(p):
            return True
        else:
            return False


class Solution:
    def isMatch(self,s: str,p: str) -> bool:
        i = j = 0
        star_position = -1
        # 感觉这个应该是专门为了 "azd", "*?d" 这种类型，
        match_position = 0
        while i < len(s):
            if j < len(p) and p[j] == "*":
                star_position = j
                match_position = i
                j += 1
            elif j < len(p) and (p[j] == "?" or p[j] == s[i]):
                i,j = i + 1,j + 1
            elif star_position != -1:
                # j能本来已经到末尾了 || 当前位置不匹配（start_position=0, j = 2; abc, *bb）
                # 需要重新把j拉回来
                j = star_position + 1
                match_position += 1
                i = match_position
            else:
                return False

        # 通过不了："b", "b*"
        # if i == len(s) and j == len(p):
        #     return True
        # else:
        #     return False

        # 将多余的 * 直接匹配空串
        return all("*" == x for x in p[j:])
        # return False


class Solution2:
    # 参考的网友答案
    def isMatch(self,s,p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i = 0
        j = 0
        start = -1
        match = 0
        while i < len(s):
            # 一对一匹配,匹配成功一起移
            if j < len(p) and (s[i] == p[j] or p[j] == "?"):
                i += 1
                j += 1
            # 记录p的"*"的位置,还有s的位置
            elif j < len(p) and p[j] == "*":
                start = j
                match = i
                j += 1
            # j 回到 记录的下一个位置
            # match 更新下一个位置
            # 这不代表用*匹配一个字符
            elif start != -1:
                j = start + 1
                match += 1
                i = match
            else:
                return False
        # 将多余的 * 直接匹配空串
        return all(x == "*" for x in p[j:])


solution = Solution()
print(solution.isMatch("aa","a"))  # false
print(solution.isMatch("abc","a?c"))  # true
print(solution.isMatch("aa","*"))  # true
print(solution.isMatch("cb","?a"))  # false
print(solution.isMatch("adceb","*a*b"))  # true
print(solution.isMatch("abceb","*b"))  # true
print(solution.isMatch("abceb","*b*"))  # true
print(solution.isMatch("b","b*"))  # true
print(solution.isMatch("abceb","*a*b"))  # true
print(solution.isMatch("acdcb","a*c?b"))  # false
print(solution.isMatch("azd","*?d"))  # true
