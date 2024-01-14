# coding=utf-8
"""
38. 外观数列
给定一个正整数 n ，输出外观数列的第 n 项。
「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。
你可以将其视作是由递归公式定义的数字字符串序列：
countAndSay(1) = "1"
countAndSay(n) 是对 countAndSay(n-1) 的描述，然后转换成另一个数字字符串。

链接：https://leetcode-cn.com/problems/valid-sudoku
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        # 1. 默认是1
        result = "1"

        # 2. 从n=2开始数
        for i in range(1, n):
            # 每一个临时的n对应的temp_result
            temp_result, count = "",  1
            for j in range(1, len(result)):
                # 对于这种比较前后两数关系的，可以不搞临时变量，直接j-1, 但是得从1开始
                if result[j] == result[j-1]:
                    count += 1
                else:
                    # 前一个字符遍历结束
                    temp_result += str(count) + result[j-1]
                    count = 1
            # 最后一个字符特殊处理
            temp_result += str(count) + result[-1]
            result = temp_result

        return result


solution = Solution()
print(solution.countAndSay(1)) # 1
print(solution.countAndSay(2)) # 11
print(solution.countAndSay(3)) # 21
print(solution.countAndSay(4)) # 1211
print(solution.countAndSay(5)) # 111221


