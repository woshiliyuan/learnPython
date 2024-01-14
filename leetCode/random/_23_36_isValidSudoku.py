# coding=utf-8
"""
36. 有效的数独
请你判断一个9 x 9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。
数字1-9在每一行只能出现一次。
数字1-9在每一列只能出现一次。
数字1-9在每一个以粗实线分隔的3x3宫内只能出现一次。

链接：https://leetcode-cn.com/problems/valid-sudokuXf
"""
from typing import List


class Solution:
    def isValidSudoku(self,board: List[List[str]]) -> bool:
        def is_sudo_list(one_list):
            flag = [-1] * 10
            for num in one_list:
                if num == '.':
                    continue
                num = int(num)
                if flag[num] == -1:
                    flag[num] = num
                else:
                    return False
            return True

        # 1. 每一行
        for row_list in board:
            if is_sudo_list(row_list) is False:
                return False

        # 2. 读取列
        for i in range(9):
            col = [x[i] for x in board]
            if is_sudo_list(col) is False:
                return False

        # 读取列方式二，不过引入了其它包
        # np_board = np.array(board)
        # for i in range(9):
        #     print(np_board[:,i])
        #     if is_sudo_list(np_board[:,i]) is False:
        #         return False

        # 3. 小方格读取
        for i in range(9):
            start_row,start_col = (i // 3) * 3,3 * (i % 3)
            temp_list = board[start_row][start_col:start_col + 3] \
                        + board[start_row + 1][start_col:start_col + 3] \
                        + board[start_row + 2][start_col:start_col + 3]
            # print(temp_list)
            if is_sudo_list(temp_list) is False:
                return False

        return True


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
print(solution.isValidSudoku(board))  # true

board = \
    [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
print(solution.isValidSudoku(board))  # false

board = \
    [["5","3",".",".","7",".",".",".","."]
        ,["6","8",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
print(solution.isValidSudoku(board))  # false
