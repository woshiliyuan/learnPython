# coding=utf-8
"""
538. 把二叉搜索树转换为累加树
给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。
提醒一下，二叉搜索树满足下列约束条件：
节点的左子树仅包含键 小于 节点键的节点。
节点的右子树仅包含键 大于 节点键的节点。
左右子树也必须是二叉搜索树。
注意：本题和 1038: https://leetcode-cn.com/problems/binary-search-tree-to-greater-sum-tree/ 相同

https://leetcode.cn/problems/convert-bst-to-greater-tree/
"""
from typing import Optional

from leetCode.utils.treeNodeUtil import TreeNode,init__binary_tree,levelOrder


class Solution:
    # 1. 自己写的
    def convertBST1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: TreeNode, current):
            if node is None: return 0

            # 1. 取右子树递归回来的值, 没有右子树的，例如图中的5，则直接取函数传递进来的current
            if node.right:
                current = dfs(node.right, current)

            # 2. 更新当前val
            node.val += current
            current = node.val

            # 3. 取左子树返回值，否则直接返回current
            if node.left:
                current = dfs(node.left, current)
            return current

        dfs(root, 0)
        return root

    # 2. 官方写的，返回值不写在递归里，抽出来当全局变量，差不多
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: TreeNode):
            nonlocal total
            if node:
                dfs(node.right)
                node.val += total
                total = node.val
                dfs(node.left)

        total = 0
        dfs(root)
        return root


s = Solution()

root = init__binary_tree([4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8])
root = s.convertBST(root)
print(levelOrder(root))
print(levelOrder(root) == [30, 36, 21, 36, 35, 26, 15, None, None, None, 33, None, None, None, 8])

root = init__binary_tree([0, None, 1])
print(levelOrder(s.convertBST(root)) == [1, None, 1])

root = init__binary_tree([1, 0, 2])
print(levelOrder(s.convertBST(root)) == [3, 3, 2])

root = init__binary_tree([3, 2, 4, 1])
print(levelOrder(s.convertBST(root)) == [7, 9, 4, 10])

root = init__binary_tree([-3,-4,0,None,None,-2,1])
print(levelOrder(s.convertBST(root)) == [-4,-8,1,None,None,-1,1])


