# coding=utf-8
"""
面试题 08.12. 八皇后
设计一种算法，打印 N 皇后在 N × N 棋盘上的各种摆法，其中每个皇后都不同行、不同列，也不在对角线上。这里的“对角线”指的是所有的对角线，不只是平分整个棋盘的那两条对角线

https://leetcode-cn.com/problems/eight-queens-lcci/
"""

from typing import List

from leetCode.utils.util import equals_array


class Solution:

    def solveNQueens(self, n: int) -> List[List[str]]:
        def visit_all(row):
            if row == n:
                temp_list = []
                for i in range(n):
                    temp_list.append("".join(board[i]))
                answer.append(temp_list)
                return

            # for i in range(row, n):
            for j in range(n):
                # 分别检测：| ↘ ↙
                if col_flag[j] == 1 or left_right[row - j + n] == 1 or right_left[row + j] == 1:
                    continue

                board[row][j] = 'Q'
                col_flag[j] = 1
                left_right[row -j + n] = 1
                right_left[row + j] = 1

                visit_all(row + 1)

                board[row][j] = '.'
                col_flag[j] = 0
                left_right[row - j + n] = 0
                right_left[row + j] = 0

        answer = []
        board = [['.'] * n for _ in range(n)]
        # 标记位置是否被访问过了: 垂直, 从左上到右下，从右上到左下
        col_flag, left_right, right_left = [0] * n, [0] * 2 * n, [0] * 2 * n
        visit_all(0)
        # print(len(answer), answer)
        return answer


solution = Solution()

equals_array(solution.solveNQueens(4), [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]])
equals_array(solution.solveNQueens(3), [])
equals_array(solution.solveNQueens(2), [])
equals_array(solution.solveNQueens(8), [])




