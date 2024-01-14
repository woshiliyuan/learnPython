# coding=utf-8
"""
70. 爬楼梯
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

https://leetcode-cn.com/problems/climbing-stairs/
"""


class Solution:
    # 0. 递归，这种求数值，不要详细的，一般不要递归，递归会超时: 只适合打印出所有跨法记录
    def climbStairs0(self,n: int) -> int:
        def visit_all(index):
            if index == n or index == n - 1:
                nonlocal count
                count += 1
                return

            visit_all(index + 1)
            visit_all(index + 2)

        count = 0
        visit_all(0)
        return count

    # 1. 递归只记录个数；类似于fibnacci了; 然而还是会超时
    def climbStairs1(self,n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    # 2. 动态规划
    def climbStairs(self,n: int) -> int:
        step1,step2 = 1,1
        for i in range(1,n):
            step1,step2 = step2,step1 + step2
        return step2


solution = Solution()
print(solution.climbStairs(2) == 2)
print(solution.climbStairs(3) == 3)
# print(solution.climbStairs(38) == 63245986)
