# coding=utf-8
"""
557. 反转字符串中的单词 III
给定一个字符串 s ，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/
"""


class Solution:
    # 1. 哈哈：在所有 Python3 提交中击败了6.30% 140ms
    # 1. 转换成s_list = list(s)
    def reverseWords0(self,s: str) -> str:
        def reverse(i,j):
            while i < j:
                s_list[i],s_list[j] = s_list[j],s_list[i]
                i,j = i + 1,j - 1

        i,j,length = 0,0,len(s)
        s_list = list(s)
        for j in range(length):
            if (j < length - 1 and s[j + 1] == " ") or j == length - 1:
                reverse(i,j)
                i = j + 2
        return "".join(s_list)

    # 2. 速度依旧很慢，不过是参考官方题解，到着添加进去
    def reverseWords1(self,s: str) -> str:
        i = 0
        answer,length = [],len(s)
        for j in range(length):
            if (j < length - 1 and s[j + 1] == " ") or j == length - 1:
                for p in range(j,i - 1,-1):
                    answer.append(s[p])
                i = j + 2
            elif s[j] == " ":
                answer.append(" ")
        return "".join(answer)

    # 3. 看来leetcode, 如果没说不用api，那就用api吧
    def reverseWords(self,s: str) -> str:
        tem = []
        for each in s.split():
            tem.append(each[::-1])
        return ' '.join(tem)

    # 恐怖如斯，这种 abc for _ in range(n) if b > 2 这种语法需要学吗？
    def reverseWords4(self,s: str) -> str:
        # print(i[::-1] for i in s.split())
        # a = [i[::-1] for i in s.split()]
        # print(a)
        return ' '.join(i[::-1] for i in s.split())


s = Solution()
print(s.reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc")
print(s.reverseWords("God Ding") == "doG gniD")

a = list("Godabc")
# a[: 3]是一个新空间
a[:3].reverse()
print(a)
print("Let's take LeetCode contest".split(" "))
