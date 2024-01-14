# coding=utf-8
"""
200. 岛屿数量
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。

https://leetcode-cn.com/problems/number-of-islands/
类似 79题目: https://leetcode-cn.com/problems/word-search/
"""
from typing import List


class Solution:
    def numIslands(self,grid: List[List[str]]) -> int:
        def visit_island(i,j):
            if j >= col or j < 0 or i < 0 or i >= row or grid[i][j] == "0":
                return

            grid[i][j] = "0"
            # 左，右，下，上
            for x,y in [(0,-1),(0,1),(1,0),(-1,0)]:
                visit_island(i + x,j + y)

        count = 0
        row,col = len(grid),len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    count += 1
                    visit_island(i,j)
        print(count,grid)
        return count


s = Solution()

print(s.numIslands([
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]) == 1)

print(s.numIslands([
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]) == 3)

# 这个样例太强了，还能往左
print(s.numIslands([
    ["1","1","1"],
    ["0","1","0"],
    ["1","1","1"]
]) == 1)

# 还能往上
print(s.numIslands([
    ["1","0","1","1","1"],
    ["1","0","1","0","1"],
    ["1","1","1","0","1"]
]) == 1)
