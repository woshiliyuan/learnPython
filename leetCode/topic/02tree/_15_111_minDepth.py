# coding=utf-8
"""
111. 二叉树的最小深度
给定一个二叉树，找出其最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/
"""

from leetCode.utils.treeNodeUtil import init__binary_tree, TreeNode


class Solution:
    def minDepth0(self, root: TreeNode) -> int:
        def visit(node: TreeNode):
            if node is None:
                return 10000
            if node.left is None and node.right is None:
                return 1

            return min(visit(node.left), visit(node.right)) + 1

        if root is None:
            return 0
        else:
            return visit(root)

    def minDepth1(self, root: TreeNode) -> int:
        def visit(node: TreeNode, level: int):
            if node is None:
                return

            nonlocal min_height
            if node.left is None and node.right is None and level < min_height:
                min_height = level
            visit(node.left, level + 1)
            visit(node.right, level + 1)

        if root is None:
            return 0
        else:
            min_height = 100000
            visit(root, 1)
            return min_height

    # 求最小高度，层次遍历，广度优先 实属最佳方案
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        depth, queue = 0, [root]
        while queue:
            depth += 1
            for _ in range(len(queue)):
                root = queue.pop(0)
                if root.left is None and root.right is None:
                    return depth

                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
        return depth


s = Solution()
root = init__binary_tree([3,9,20,None,None,15,7])
print(s.minDepth(root) == 2)

root = init__binary_tree([2,None,3,None,4,None,5,None,6])
print(s.minDepth(root) == 5)

root = init__binary_tree([1,2,3, None, 4, None, 5])
print(s.minDepth(root) == 3)

root = init__binary_tree([1,None,3])
print(s.minDepth(root) == 2)

root = init__binary_tree([1])
print(s.minDepth(root) == 1)

root = init__binary_tree([])
print(s.minDepth(root) == 0)