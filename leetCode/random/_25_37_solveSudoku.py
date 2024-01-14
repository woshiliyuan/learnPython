# coding=utf-8
"""
37. 解数独
编写一个程序，通过填充空格来解决数独问题
数独的解法需 遵循如下规则：
数字1-9在每一行只能出现一次。
数字1-9在每一列只能出现一次。
数字1-9在每一个以粗实线分隔的3x3宫内只能出现一次。（请参考示例图）
数独部分空格内已填入了数字，空白格用'.'表示。

链接：https://leetcode-cn.com/problems/sudoku-solver
"""
from typing import List

from leetCode.utils.util import equals_array


class Solution:
    def solveSudoku0(self,board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def remove_repeat(i,j):
            left,top = (i // 3) * 3,(j // 3) * 3
            little_borad = board[left][top:top + 3] + board[left + 1][top:top + 3] + board[left + 2][top:top + 3]
            temp_list = board[i] + [x[j] for x in board] + little_borad

            candition_list = candition_map[f"{i}_{j}"]
            for num in candition_list:
                if num in temp_list:
                    candition_list.remove(num)

        candition_map = {}
        first_time = True
        time = 0
        while first_time or len(candition_map) > 0:
            time += 1
            if time > 500:
                break
            print(time)
            first_time = False
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        key = f"{i}_{j}"
                        if key not in candition_map:
                            candition_map[key] = [str(x + 1) for x in range(9)]

                        remove_repeat(i,j)
                        # 找到当前位置的解了，很开心
                        if len(candition_map[key]) == 1:
                            board[i][j] = candition_map[key][0]
                            del candition_map[key]
                            print(key,board[i][j])
        print(candition_map,len(candition_map))

    def solveSudoku0(self,board: List[List[str]]) -> None:
        def dfs(pos: int):
            nonlocal valid
            if pos == len(spaces):
                valid = True
                return

            i,j = spaces[pos]
            for digit in range(9):
                if line[i][digit] == column[j][digit] == block[i // 3][j // 3][digit] == False:
                    line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = True
                    board[i][j] = str(digit + 1)
                    dfs(pos + 1)
                    # 回溯退回
                    line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = False
                if valid:
                    return

        line = [[False] * 9 for _ in range(9)]
        column = [[False] * 9 for _ in range(9)]
        block = [[[False] * 9 for _a in range(3)] for _b in range(3)]
        valid = False

        spaces = list()  # []
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    spaces.append((i,j))
                else:
                    digit = int(board[i][j]) - 1
                    line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = True
        print(spaces)
        dfs(0)

    def solveSudoku(self,board: List[List[str]]) -> None:
        def game_over():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        return False
            return True

        def find_next_empty(row):
            for i in range(row,9):
                for j in range(9):
                    if board[i][j] == '.':
                        return (i,j)
            return (8,8)

        def visit_all(row2):
            nonlocal fill_all
            fill_all = game_over()
            if fill_all is True:
                # print("ok", board)
                return

            (row,j) = find_next_empty(row2)
            # print("row, j", row, j)

            # 每一个空的单元格尝试1-9的选择 (0, 2)
            for index in range(9):  # 0 -8
                if row_list[row][index] == 0 and col_list[j][index] == 0 and box_list[row // 3][j // 3][index] == 0:
                    board[row][j] = str(index + 1)  # 1 - 9
                    row_list[row][index] = col_list[j][index] = box_list[row // 3][j // 3][index] = 1

                    visit_all(row)
                    if fill_all is True:
                        # print("222", board)
                        return

                    board[row][j] = "."
                    row_list[row][index] = col_list[j][index] = box_list[row // 3][j // 3][index] = 0
                # if fill_all is True:
                #     print("222", board)
                #
                #     return

            # print("row, j", row, j)
            # print(666, board)

        row_list,col_list = [[0] * 9 for _ in range(9)],[[0] * 9 for _ in range(9)]
        box_list = [[[0] * 9 for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    index = int(board[i][j]) - 1
                    row_list[i][index] = col_list[j][index] = box_list[i // 3][j // 3][index] = 1

        fill_all = False
        visit_all(0)
        return board


solution = Solution()
board = \
    [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
solution.solveSudoku(board)

b = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],
     ["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],
     ["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]

equals_array(board,b)
