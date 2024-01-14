"""
9. 回文数
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
例如，121 是回文，而 123 不是。

https://leetcode-cn.com/problems/palindrome-number/
"""


class Solution:
    def isPalindrome1(self,x: int) -> bool:
        xStr = str(x)

        length = len(xStr)
        for index in range(int(length + 1 / 2)):
            if xStr[index] != xStr[length - 1 - index]:
                return False
        return True

    # 强行记忆吧：回文可以简化比较界限的： length // 2
    def isPalindrome2(self,x: int) -> bool:
        s = str(x)
        length = len(s)
        for i in range(length // 2):
            if s[i] != s[length - 1 - i]: return False
        return True

    def isPalindrome3(self,x: int) -> bool:
        x_str = str(x)
        return x_str[::-1] == x_str

    # 官方题解：反转一半数字; 时间复杂度竟然是o(log(n)): 但是仅限于数字的回文判断
    def isPalindrome(self,x: int) -> bool:
        # 特殊情况：
        # 如上所述，当 x < 0 时，x不是回文数。
        # 同样地，如果数字的最后一位是0，为了使该数字为回文，则其第一位数字也应该是0，只有0满足这一属性
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted_number = 0
        while x > reverted_number:
            reverted_number = reverted_number * 10 + x % 10
            x //= 10

        # 当数字长度为奇数时，我们可以通过 revertedNumber / 10，去除处于中位的数字。
        # 例如，当输入为12321时，在while 循环的末尾我们可以得到 x = 12，revertedNumber = 123，
        # 由于处于中位的数字不影响回文（它总是与自己相等），所以我们可以简单地将其去除。
        return x == reverted_number or x == reverted_number / 10


# 测试过程
# 1. 新建对象
solution = Solution()

# 2. 函数调用
print(solution.isPalindrome(121))
print(solution.isPalindrome(-121) is False)
print(solution.isPalindrome(120) is False)
print(solution.isPalindrome(1221))
print(solution.isPalindrome(1231) is False)
