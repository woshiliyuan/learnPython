# coding=utf-8
"""
64. 最小路径和
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。

https://leetcode-cn.com/problems/minimum-path-sum/
"""
from typing import List


class Solution:
    def minPathSum0(self,grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row,col = len(grid),len(grid[0])

        for j in range(1,col):
            grid[0][j] += grid[0][j - 1]
        for i in range(1,row):
            grid[i][0] += grid[i - 1][0]

        for i in range(1,row):
            for j in range(1,col):
                grid[i][j] += min(grid[i - 1][j],grid[i][j - 1])

        return grid[-1][-1]

    def minPathSum(self,grid: List[List[int]]) -> int:
        dp = grid[0].copy()

        for j in range(1,len(dp)):
            dp[j] += dp[j - 1]

        for i in range(1,len(grid)):
            for j in range(len(dp)):
                if j == 0:
                    dp[j] += grid[i][j]
                else:
                    dp[j] = min(dp[j],dp[j - 1]) + grid[i][j]

        return dp[-1]


solution = Solution()
print(solution.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))  # 7
print(solution.minPathSum([[1,2,3],[4,5,6]]))  # 12
