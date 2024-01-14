# coding=utf-8
"""
48. 旋转图像
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
https://leetcode-cn.com/problems/rotate-image/
"""
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        for i in range(length // 2):
            for j in range(i, length-1-i):
                print(i, j, matrix[i][j])

                # temp = matrix[i][j]
                # matrix[i][j] = matrix[length-1-j][i]
                # matrix[length-1-j][i] = matrix[length-1-i][length-1-j]
                # matrix[length-1-i][length-1-j] = matrix[j][length-1-i]
                # matrix[j][length - 1 - i] = temp

                # temp = matrix[i][j]
                # for _ in range(3):
                #     matrix[i][j] = matrix[length - 1 - j][i]
                #     i, j = length - 1 - j, i
                # matrix[i][j] = temp

                x, y, temp = i, j, matrix[i][j]
                for _ in range(3):
                    matrix[x][y] = matrix[length - 1 - y][x]
                    x, y = length - 1 - y, x
                matrix[x][y] = temp


solution = Solution()

matrix = [[1,2,3],[4,5,6],[7,8,9]]
solution.rotate(matrix)
print(matrix) # [[7,4,1],[8,5,2],[9,6,3]]

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
solution.rotate(matrix)
print(matrix) # [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

# matrix = [[1]]
# solution.rotate(matrix)
# print(matrix)


