# coding=utf-8
"""
62. 不同路径
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
问总共有多少条不同的路径？

https://leetcode-cn.com/problems/unique-paths/
"""


class Solution:
    # 新增一空列，一空行
    def uniquePaths1(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 1. 新增一列，一行
        array = [[0] * (n + 1) for _ in range(m + 1)]
        array[1][0] = 1
        # 2. 循环时(i, j)不用边界处理，但是从[1, m+1)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                array[i][j] = array[i - 1][j] + array[i][j - 1]
        return array[i][j]

    # 不新增列，循环时候得判断
    def uniquePaths(self, m: int, n: int) -> int:
        array = [[1] * n for _ in range(m)]
        # 官方这么初始化的，但是貌似没必要，因为 top + left >= 1
        # f = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]

        for i in range(1, m):
            for j in range(1, n):
                array[i][j] = array[i - 1][j] + array[i][j - 1]
        return array[-1][-1]


solution = Solution()
print(solution.uniquePaths(3, 7) == 28)
print(solution.uniquePaths(3, 2) == 3)
print(solution.uniquePaths(1, 2) == 1)
print(solution.uniquePaths(7, 2) == 7)
print(solution.uniquePaths(7, 3) == 28)
print(solution.uniquePaths(3, 3) == 6)
