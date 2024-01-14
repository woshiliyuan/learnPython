# coding=utf-8
"""
600. 不含连续1的非负整数
给定一个正整数 n ，返回范围在 [0, n] 都非负整数中，其二进制表示不包含 连续的 1 的个数。

https://leetcode.cn/problems/non-negative-integers-without-consecutive-ones/
"""


class Solution:
    # 1. 暴力破解：n * log(n)
    def findIntegers1(self,n: int) -> int:
        def serial_one(num):
            last = 0
            while num != 0:
                num,temp = num // 2,num % 2
                if temp == 1 and last == 1:
                    return True
                last = temp
            return False

        count = 0
        for i in range(n + 1):
            if not serial_one(i): count += 1
        return count

    # 2. 暴力破解：n * 2* log(n)
    def findIntegers2(self,n: int) -> int:
        count = 0
        for i in range(n + 1):
            if "11" not in bin(i): count += 1
        return count

    # ------------------   动态规划         ------------------------
    # 1. 打家劫舍的思想
    def findIntegers(self,n: int) -> int:
        # 二进制序号从0开始
        # 1. 长度为i的二进制数组[选1，不选0]能有不连续1的种类
        s = [1] * 30  # select
        d = [0] * 30  # dis select
        d[1] = 1
        for i in range(2,30):
            s[i],d[i] = d[i - 1],s[i - 1] + d[i - 1]

        answer,pre = 0,0
        # 开始从高往低位匹配二进制n的1位置
        for i in range(29,-1,-1):
            if n & (1 << i):
                answer += s[i] + d[i]
                if pre == 1:
                    return answer
                pre = 1
            else:
                pre = 0
        return answer + 1

    # 2. 字典树 || 斐波那契树 思想
    """
        官方题解真是看不懂，参考网友题解：
        1. 斐波那契：https://leetcode.cn/problems/non-negative-integers-without-consecutive-ones/solution/leetcode-ac-dong-tai-gui-hua-jie-fa-han-eqceq/
        2. 字典树：https://leetcode.cn/problems/non-negative-integers-without-consecutive-ones/solution/suan-fa-xiao-ai-wo-lai-gei-ni-jie-shi-qi-4nh4/
    """

    # 1. 先搞成二进制字符串，然后遍历一遍即可：o(2 * log(n)), 空间o(log(n))
    def findIntegers2(self,n: int) -> int:
        b = "{0:b}".format(n)
        size = len(b)
        # 当位数为i时, 能表示出没有连续1的种数为kind[i], i = 0, 1, 2, ...
        kinds = [1] * max(size,2)
        kinds[1] = 2
        for i in range(2,size):
            kinds[i] = kinds[i - 1] + kinds[i - 2]

        answer = 0
        for i in range(size):
            if b[i] == "1":
                answer += kinds[size - 1 - i]
                if i > 0 and b[i - 1] == "1":
                    return answer

        return answer + 1

    # 2. 不用字符串，改用位运算
    def findIntegers2(self,n: int) -> int:

        kinds = [1] * 30
        kinds[1] = 2
        for i in range(2,30):
            kinds[i] = kinds[i - 1] + kinds[i - 2]

        answer,pre = 0,0
        for i in range(29,-1,-1):
            # 第i位是否为1
            if n & (1 << i):
                answer += kinds[i]
                if pre == 1: return answer
                pre = 1
            else:
                pre = 0

        return answer + 1

    # 3. 使用字典树，即官方题解思维注释同样的代码
    def findIntegers2(self,n: int) -> int:
        # 预处理第 i 层满二叉树的路径数量
        dp = [0] * 31
        # 以0为根节点，树高为i，能表示出没有连续1的种数： 1, 1, 2, 3, 5, 8, 13,
        dp[0],dp[1] = 1,1
        for i in range(2,31):
            dp[i] = dp[i - 1] + dp[i - 2]

        # pre 记录上一层的根节点值，res记录最终路径数
        res,pre = 0,0
        for i in range(29,-1,-1):
            # if 语句判断 当前子树是否有右子树
            if n & (1 << i):
                # 有右子树
                res += dp[i + 1]  # 先将左子树（满二叉树）的路径加到结果中
                if pre == 1:
                    # 上一层为 1，之后要处理的右子树根节点肯定也为 1
                    # 此时连续两个 1，不满足题意，直接退出
                    return res
                pre = 1
            else:
                # 无右子树，此时不能保证左子树是否为满二叉树，所以要在下一层再继续判断
                pre = 0

        return res + 1


s = Solution()

print(s.findIntegers(1) == 2)
print(s.findIntegers(2) == 3)
print(s.findIntegers(4) == 4)
print(s.findIntegers(5) == 5)
print(s.findIntegers(6) == 5)
print(s.findIntegers(7) == 5)
print(s.findIntegers(8) == 6)
print(s.findIntegers(9) == 7)
print(s.findIntegers(10) == 8)
print(s.findIntegers(11) == 8)
print(s.findIntegers(12) == 8)
print(s.findIntegers(13) == 8)
print(s.findIntegers(14) == 8)
print(s.findIntegers(15) == 8)

print()
print("{0:b}".format(5))  # 101
print(bin(5))  # 0b101
