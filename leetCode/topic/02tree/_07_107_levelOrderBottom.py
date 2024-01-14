# coding=utf-8
"""
107. 二叉树的层序遍历 II
给你二叉树的根节点 root ，返回其节点值 自底向上的层序遍历 。
（即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/
"""

from typing import List

from leetCode.utils.treeNodeUtil import TreeNode,init__binary_tree


class Solution:
    def levelOrderBottom0(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        answer = []

        # s为每层结束时的分隔符
        queue, level = [root, 's'], []
        while queue:
            node = queue.pop(0)
            if node == 's':
                # 到最后了，这一把什么也没捞着
                if not level:
                    break
                # answer.append(level)
                answer.insert(0, level)
                queue.append('s')
                level = []
            else:
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return answer

    # leetcode官方思路一: 太巧妙简洁了，
    def levelOrderBottom1(self, root: TreeNode) -> List[List[int]]:
        def visit(node: TreeNode, level: int):
            if node is None:
                return

            if len(answer) - 1 < level:
                answer.insert(0, [])
            answer[len(answer) - 1 - level].append(node.val)
            visit(node.left, level+1)
            visit(node.right, level+1)

        answer = []
        visit(root, 0)
        return answer

    # 每次插入头节点太慢了，数组要移动；还是从顶层到底层，再逆序比较好
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        def visit(node: TreeNode, level: int):
            if node is None:
                return

            if len(answer) - 1 < level:
                answer.append([])
            answer[level].append(node.val)
            visit(node.left, level+1)
            visit(node.right, level+1)

        answer = []
        visit(root, 0)
        return answer[::-1]


s = Solution()
root = init__binary_tree([3, 9, 20, None, None, 15, 7])
print(s.levelOrderBottom(root))
print(s.levelOrderBottom(root) == [[15, 7], [9, 20], [3]])

root = init__binary_tree([1])
print(s.levelOrderBottom(root) == [[1]])

root = init__binary_tree([])
print(s.levelOrderBottom(root) == [])

