"""
Created on 2019年12月24日

题目：https://leetcode-cn.com/problems/reverse-integer/
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例1:

输入: 123
输出: 321
示例 2:

输入: -123
输出: -321

"""


class Solution:
    def reverse(self,x: int) -> int:
        tempX = x
        if tempX < 0:
            x = -1 * x

        result = 0
        while x != 0:
            temp = x % 10
            x = int(x / 10)
            result = 10 * result + temp

        if tempX < 0:
            result = -1 * result

        if result > 2 ** 31 - 1 or result < -2 ** 31:
            return 0

        return result

    #  直接利用python自带的函数 str和int强转
    def reverse2(self,x: int) -> int:
        if x < 0:
            x = -1 * x
            x = int("-" + str(x)[::-1])
        else:
            x = int(str(x)[::-1])
        if x > 2 ** 31 - 1 or x < -2 ** 31:
            return 0
        return x


solution = Solution()

# 测试样例1
x = 123
result = solution.reverse(x)
print(result)

# 测试样例2
x = -123
result = solution.reverse(x)
print(result)

# 测试样例3
x = 120
result = solution.reverse(x)
print(result)

# 测试样例4
x = -120
result = solution.reverse(x)
print(result)

# 测试样例4
x = 1234567777776666666666666669
result = solution.reverse(x)
print(result)
