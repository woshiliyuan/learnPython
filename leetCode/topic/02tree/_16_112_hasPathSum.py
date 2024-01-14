# coding=utf-8
"""
112. 路径总和
给你二叉树的根节点 root 和一个表示目标和的整数 targetSum 。判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。如果存在，返回 true ；否则，返回 false 。
叶子节点 是指没有子节点的节点。

https://leetcode.cn/problems/path-sum/
"""

from typing import Optional

from leetCode.utils.treeNodeUtil import init__binary_tree,TreeNode


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def visit(node: TreeNode, answer):
            nonlocal flag
            if flag or not node: return

            answer += node.val
            if not node.left and not node.right and answer == targetSum:
                flag = True
                return

            visit(node.left, answer)
            visit(node.right, answer)

        # if not root: return False
        flag = False
        visit(root, 0)
        return flag

    # 2. 官方题解递归；
    # 递归本身具有返回值
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return sum == root.val
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)


s = Solution()

root = init__binary_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
print(s.hasPathSum(root, 22))

root = init__binary_tree([1, 2, 3])
print(s.hasPathSum(root, 5) is False)

root = init__binary_tree([])
print(s.hasPathSum(root, 0) is False)

root = init__binary_tree([1,2])
print(s.hasPathSum(root, 1) is False)

root = init__binary_tree([-2,None,-3])
print(s.hasPathSum(root, -5))
