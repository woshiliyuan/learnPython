# coding=utf-8
"""
94. 二叉树的中序遍历
给定一个二叉树的根节点 root ，返回它的 中序 遍历。

https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
"""
from typing import Optional, List

from leetCode.utils.treeNodeUtil import TreeNode, init__binary_tree


class Solution:
    def inorderTraversal0(self, root: Optional[TreeNode]) -> List[int]:
        def visit(node: TreeNode):
            if node is None:
                return

            visit(node.left)
            answer.append(node.val)
            visit(node.right)

        answer = []
        visit(root)
        return answer

    # 2. 迭代做法: 我自己之前第一题那样，栈里面只存未访问的，貌似做不到？ 中间节点每次必须访问，而且得入栈暂存
    # 错误的，待调整
    def inorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        answer, stack, node = [], [], root
        while stack or node:
            if not node:
                node = stack.pop()
                answer.append(node.val)
            elif node.right:
                stack.append(node.right)
                stack.append(node)
            node = node.left
        print(answer)
        return answer

    # 迭代：栈里是未添加的，都是访问过的
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer, stack, node = [], [], root
        while stack or node:
            # 1. 都是一路网左进栈
            while node:
                stack.append(node)
                node = node.left

            # 2. 进到每次的左分支底部了，开始要弹栈访问了
            node = stack.pop()
            # 这两句真绝，想不到呀
            # 3. 最关键的一步，哪儿保存val; 前序在stack.append时候，中序在stack.pop时候
            answer.append(node.val)
            node = node.right
        return answer


s = Solution()
root = init__binary_tree([1, None, 2, 3])
print(s.inorderTraversal(root) == [1, 3, 2])

root = init__binary_tree([])
print(s.inorderTraversal(root) == [])

root = init__binary_tree([1])
print(s.inorderTraversal(root) == [1])
