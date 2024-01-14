# coding=utf-8
"""
279. 完全平方数
给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。
完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。

https://leetcode-cn.com/problems/perfect-squares/
"""


class Solution:
    def __init__(self):
        self.square = [1, 4, 9, 16, 25]
        self.f = [0]

    # 暴力破解， 类似  40. 组合总和 II, 但是会超时
    # https://leetcode-cn.com/problems/combination-sum-ii/
    def numSquares0(self, n: int) -> int:
        def dfs(index, sum, count):
            nonlocal max_count
            if sum > n:
                return
            if sum == n:
                max_count = min(max_count, count)

            for i in range(index, len(self.square)):
                dfs(i, self.square[i] + sum, count + 1)

        for i in range(len(self.square), int(n ** 0.5)):
            self.square.append((i + 1) ** 2)

        max_count = n
        dfs(0, 0, 0)
        return max_count

    # 2. 动态规划: f(n): 整数n的完全平方数最小为f(n)
    def numSquares1(self, n: int) -> int:
        f = [0] * (n + 1)
        # f1, f2, ... , fn都要设置的，fn依赖于之前的所有f
        for i in range(1, n + 1):
            min_f = i
            # 假设 fn = j * j + left
            for j in range(1, int(i ** 0.5) + 1):
                min_f = min(min_f, f[i - j * j])
            # 这个1就是上面的j**2
            f[i] = 1 + min_f
        return f[n]

    # 3. 如果把f全局化，跑所有用例时会不会快？
    def numSquares(self, n: int) -> int:
        for i in range(len(self.f), n + 1):
            min_f = i
            for j in range(1, int(i ** 0.5) + 1):
                min_f = min(min_f, self.f[i - j * j])
            self.f.append(1 + min_f)
        return self.f[n]


s = Solution()
print(s.numSquares(12) == 3)
print(s.numSquares(13) == 2)

print(s.numSquares(37) == 2)
print(s.numSquares(76) == 3)



