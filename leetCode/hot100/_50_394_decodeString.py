# coding=utf-8
"""
394. 字符串解码
给定一个经过编码的字符串，返回它解码后的字符串。
编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

https://leetcode-cn.com/problems/decode-string/
"""
import re


class Solution:
    # 1. 正则表达式: o((2n+单个[]的长度) * []组合的个数]
    def decodeString1(self,s: str) -> str:
        while True:
            search = re.search(r'(\d+)\[([a-z]+)\]',s)
            if not search:
                break
            count,str = search.group(1),search.group(2)
            temp_str = int(count) * str
            s = s.replace(search.group(),temp_str)

        return s

    # 2. 栈的使用
    def decodeString2(self,s: str) -> str:
        # 最后结果就存在栈里面了, 是扫描字符串，没有"]"自然就完结了
        stack,i = [],0
        while i < len(s):
            # 1. 数字进栈
            if '0' <= s[i] <= '9':
                j = i + 1
                # 判断下一个是某个字符作为结束的，一般情况下迭代搞不定
                # 1. 用 s[i+1] vs s[i]更佳； 2. do...while...
                while '0' <= s[j] <= '9':
                    j += 1
                stack.append(int(s[i:j]))
                i = j
            # 2. [ 也先进栈，作为标记；不进栈也可以，但是出栈时得判断是否为数字
            elif 'a' <= s[i] <= 'z' or s[i] == '[':
                stack.append(s[i])
                i += 1
            # 3. 只能是']'了
            else:
                # 3.1 一直出栈到数字停下来
                temp_list = []
                while True:
                    temp = stack.pop()
                    if temp == "[": break
                    temp_list.append(temp)
                temp_list.reverse()
                # 此处出战的一定是数字了
                count = stack.pop()

                # 3.2 反转并拼接为解码字符; 最后结果保存在stack && 可能还没算完，so再进栈
                stack.append(count * "".join(temp_list))
                i += 1

        return "".join(stack)

    # 官方那种解法：栈里面存了所有 num[abc..., 碰到“]”之后，出栈消掉[
    # 网友的答案，碰到[, 栈里面成对存 [当前左括号与上一轮左括号之间的字符串last_s, multi_num], 碰到“】”, 出栈结算
    # 最终
    def decodeString2(self,s: str) -> str:
        stack,multi_num,multi_s = [],0,""
        for c in s:
            if '0' <= c <= '9':
                multi_num = 10 * multi_num + int(c)
            elif c == '[':
                # 2[a2[bc]d], 现在如果为第二个"[", 则存入[a, 2]
                last_s = multi_s
                stack.append([last_s,multi_num])
                multi_s,multi_num = "",0
            elif c == ']':
                last_s,multi_num = stack.pop()
                # 这里是关键，赋值给multi_s，因为如果当前栈中还有[num, last_s], 则后续还能走到现在这个分支
                multi_s = last_s + multi_num * multi_s
                multi_num = 0
            else:
                multi_s += c

        return multi_s

    # 3. 递归为子问题。
    # 递归还能这么写？i不通过函数传参，使用的是全局变量
    def decodeString(self,s: str) -> str:
        # 找到成对匹配的"]" || 字符串结尾，
        def son_str():
            nonlocal i
            # 0 停止符
            if i == len(s) or s[i] == ']': return ""

            # 1. 字母，拼上
            if 'a' <= s[i] <= 'z':
                i += 1
                return s[i - 1] + son_str()
            # 2. 数字，解码成字母再拼上
            elif '0' <= s[i] <= '9':
                # 获取到数字
                j = i + 1
                while '0' <= s[j] <= '9': j += 1
                multi_num = int(s[i:j])
                # 左括号跳过
                i = j + 1

                # 这里真是太精髓了：匹配到和当前左括号匹配的那个']'才会结束：
                # 1. 如果没有嵌套，那就开始下一轮；3[a]2[bc], 匹配出来的是 aaa
                # 2. 如果有嵌套 2[a2[bc]d]abc，此处匹配出来的是 abcbcd
                multi_s = son_str()
                # 过滤右括号
                i += 1
                return multi_num * multi_s + son_str()

        i = 0
        return son_str()


s = Solution()
print(s.decodeString("3[a]2[bc]") == "aaabcbc")
print(s.decodeString("2[a2[bc]d]") == "abcbcdabcbcd")
print(s.decodeString("3[a2[c]]") == "accaccacc")
print(s.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef")
print(s.decodeString("abc3[cd]xyz") == "abccdcdcdxyz")
