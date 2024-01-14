# coding=utf-8
"""
240. 搜索二维矩阵 II
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
每行的元素从左到右升序排列。
每列的元素从上到下升序排列。


https://leetcode-cn.com/problems/search-a-2d-matrix-ii/
"""
import bisect
from typing import List


class Solution:
    # 1. 一行一行的二分查找
    def searchMatrix0(self,matrix: List[List[int]],target: int) -> bool:
        def binary(i,left,right):
            nonlocal flag
            # middle = left + (right - left) // 2
            middle = (right + left) // 2
            value = matrix[i][middle]
            if value == target:
                flag = True
            elif value > target and middle > left:
                binary(i,left,middle - 1)
            elif value < target and middle < right:
                binary(i,middle + 1,right)

        flag,col = False,len(matrix[0])
        for i in range(len(matrix)):
            binary(i,0,col - 1)
            if flag:
                break
        return flag

    # 优化一版本我自己的代码
    def searchMatrix1(self,matrix: List[List[int]],target: int) -> bool:
        # 迭代进行二分查找
        def binary(arr):
            # 包头不包尾
            left,right = 0,len(arr)
            while left < right:
                middle = (left + right) // 2
                if arr[middle] == target:
                    return True
                elif arr[middle] < target:
                    left = middle + 1
                else:
                    right = middle
            return False

        for arr in matrix:
            if binary(arr):
                return True
            if arr[0] > target:
                return False
        return False

    # 1.2 官方的一行行二分查找：还能这么玩？
    def searchMatrix2(self,matrix: List[List[int]],target: int) -> bool:
        for row in matrix:
            idx = bisect.bisect_left(row,target)
            if idx < len(row) and row[idx] == target:
                return True
        return False

    # 2. 澜姐的转圈圈搜索
    def searchMatrix2(self,matrix: List[List[int]],target: int) -> bool:
        def search(i,j):
            nonlocal flag
            if flag or i < 0 or j < 0 or i == row or j == col or visited[i][j] == 1:
                return

            visited[i][j] = 1
            if matrix[i][j] == target:
                flag = True
            elif matrix[i][j] < target:
                search(i,j + 1)
                search(i + 1,j)
            else:
                search(i - 1,j)
                search(i,j - 1)

        row,col = len(matrix),len(matrix[0])
        flag = False
        visited = [[0] * col for _ in range(row)]
        search(0,0)
        return flag

    # 2.2 澜姐的转圈圈搜索进阶 - 二分查找  --  To do
    def searchMatrixe3(self,matrix: List[List[int]],target: int) -> bool:
        def search(p1,p2):
            nonlocal flag
            if flag:
                return

            (i1,j1),(i2,j2) = p1,p2
            if i1 == i2:
                middle = j1 + (j2 - j1) // 2
                if matrix[i1][middle] == target:
                    flag = True

                search(i1,)

            visited[i][j] = 1
            if matrix[i][j] == target:
                flag = True
            elif matrix[i][j] < target:
                search(i,j + 1)
                search(i + 1,j)
            else:
                search(i - 1,j)
                search(i,j - 1)

        row,col = len(matrix),len(matrix[0])
        flag = False
        visited = [[0] * col for _ in range(row)]
        search((0,0),(0,col - 1))
        return flag

    # 3. 变幻矩形查找，官方的Z形查找, 太牛逼了吧
    def searchMatrix(self,matrix: List[List[int]],target: int) -> bool:
        row,col = len(matrix),len(matrix[0])
        i,j = 0,col - 1
        while i < row and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False


s = Solution()
print(s.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],5))
print(s.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],16))
print(s.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],20) is False)
print(s.searchMatrix([[-5]],-5))
