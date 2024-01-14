# coding=utf-8
"""
637. 二叉树的层平均值
给定一个非空二叉树的根节点 root , 以数组的形式返回每一层节点的平均值。与实际答案相差 10-5 以内的答案可以被接受。

https://leetcode-cn.com/problems/average-of-levels-in-binary-tree/
"""

from typing import List

from leetCode.utils.treeNodeUtil import TreeNode,init__binary_tree


class Solution:
    # 完整遍历并记录完所有节点；最后再一起计算
    def averageOfLevels0(self,root: TreeNode) -> List[List[int]]:
        def visit(node: TreeNode,level: int):
            if node is None:
                return

            if len(answer) - 1 < level:
                answer.append([])

            answer[level].append(node.val)
            visit(node.left,level + 1)
            visit(node.right,level + 1)

        answer = []
        visit(root,0)
        avgs = []
        for level_array in answer:
            avgs.append(sum(level_array) / len(level_array))
        return avgs

    # 两个数组：和 & 个数
    def averageOfLevels(self,root: TreeNode) -> List[List[int]]:
        def visit(node: TreeNode,level: int):
            if node is None:
                return

            if len(sums) - 1 < level:
                sums.append(0)
                count.append(0)

            sums[level] += node.val
            count[level] += 1

            visit(node.left,level + 1)
            visit(node.right,level + 1)

        sums,count = [],[]
        visit(root,0)
        avgs = []
        for i in range(len(sums)):
            avgs.append(sums[i] / count[i])
        return avgs


s = Solution()
root = init__binary_tree([3,9,20,None,None,15,7])
print(s.averageOfLevels(root))
print(s.averageOfLevels(root) == [3.00000,14.50000,11.00000])

root = init__binary_tree([3,9,20,15,7])
print(s.averageOfLevels(root) == [3.00000,14.50000,11.00000])

root = init__binary_tree([1])
print(s.averageOfLevels(root) == [1])

root = init__binary_tree([])
print(s.averageOfLevels(root) == [])
