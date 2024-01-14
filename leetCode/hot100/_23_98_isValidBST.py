# coding=utf-8
"""
98. 验证二叉搜索树
给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

有效 二叉搜索树定义如下：
节点的左子树只包含 小于 当前节点的数。
节点的右子树只包含 大于 当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

https://leetcode-cn.com/problems/validate-binary-search-tree/
"""
import sys
from leetCode.utils.treeNodeUtil import TreeNode, init__binary_tree


class Solution:
    # 1. 中序遍历
    def isValidBST(self, root: TreeNode) -> bool:
        def visit(root: TreeNode):
            nonlocal flag, last_value
            if flag is False:
                return

            if root is None:
                return

            visit(root.left)

            if root.val <= last_value:
                flag = False
            last_value = root.val

            visit(root.right)

        flag, last_value = True, -sys.maxsize -1
        visit(root)
        return flag


s = Solution()
root = init__binary_tree([2,1,3])
print(s.isValidBST(root) is True)

root = init__binary_tree([5, 1, 4, None, None, 3, 6])
print(s.isValidBST(root) is False)

root = init__binary_tree([2, 2, 2])
print(s.isValidBST(root) is False)

# 有意思吗，咋又这样的用例
root = init__binary_tree([-2147483648])
print(s.isValidBST(root) is True)

