# coding=utf-8
"""
79. 单词搜索
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

https://leetcode-cn.com/problems/word-search/
"""
from typing import List


class Solution:

    def exist(self,board: List[List[str]],word: str) -> bool:
        def search(r,c,cur):  # 行号，列号，子集起始关键字
            nonlocal is_exit
            # print(r,c,cur,board[r][c],word[cur])
            if board[r][c] != word[cur] or (r,c) in visited:  # 当前不等于起始关键字，或已访问过，就跳过且改变行列号重新搜索
                return False
            if len(word) - 1 == cur:  # 说明所有的子集都匹配了
                is_exit = True
                return

            visited.append((r,c))
            directions = [(0,1),(1,0),(0,-1),(-1,0)]  # 上右下左
            for dr,dc in directions:
                newr,newc = r + dr,c + dc  # 上右下左顺序搜索
                if 0 <= newr < row and 0 <= newc < col:  # 当前行列号要大于0且小于行列号
                    search(newr,newc,cur + 1)  # 访问下一个子集

        is_exit,row,col = False,len(board),len(board[0])
        visited = []
        for r in range(row):
            for c in range(col):
                search(r,c,0)  # 永远从第一个关键字搜索
                if is_exit is True:  # 如果存在，则停止
                    return True
        return is_exit


solution = Solution()

print(solution.exist([["A","B","C","E"],
                      ["S","F","C","S"],
                      ["A","D","E","E"]],"ABC"))  # True

print(solution.exist([["A","B","C","E"],
                      ["S","F","C","S"],
                      ["A","D","E","E"]],"ABD"))  # False

print(solution.exist([["A","B","C","E"],
                      ["S","F","C","S"],
                      ["A","D","E","E"]],"ABCCEDASF"))  # True

print(solution.exist([["A","B","C","E"],
                      ["S","F","C","S"],
                      ["A","D","E","E"]],"ABCCEDASFC"))  # False
