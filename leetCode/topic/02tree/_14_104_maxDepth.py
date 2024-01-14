# coding=utf-8
"""
104. 二叉树的最大深度
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
"""

from typing import Optional

from leetCode.utils.treeNodeUtil import init__binary_tree,TreeNode


class Solution:
    def maxDepth0(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def maxDepth1(self, root: Optional[TreeNode]) -> int:
        def visit(node: TreeNode, level: int):
            if node is None:
                return
            nonlocal height
            if level > height:
                height = level
            visit(node.left, level + 1)
            visit(node.right, level + 1)

        height = 0
        visit(root, 1)
        return height

    # 也可以用广度遍历来完成，层序遍历数，遍历了多少层便是多高
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        depth, queue = 0, [root]
        while queue:
            for _ in range(len(queue)):
                root = queue.pop(0)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            depth += 1
        return depth


s = Solution()
root = init__binary_tree([3,9,20,None,None,15,7])
print(s.maxDepth(root) == 3)

root = init__binary_tree([1,2,3,4,5,None,7])
print(s.maxDepth(root) == 3)

root = init__binary_tree([1,2,3, None, 4, None, 5])
print(s.maxDepth(root) == 3)

root = init__binary_tree([1,None,3])
print(s.maxDepth(root) == 2)

root = init__binary_tree([1])
print(s.maxDepth(root) == 1)

root = init__binary_tree([])
print(s.maxDepth(root) == 0)