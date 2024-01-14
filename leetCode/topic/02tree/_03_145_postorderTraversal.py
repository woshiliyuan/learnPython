# coding=utf-8
"""
145. 二叉树的后序遍历
给你一棵二叉树的根节点 root ，返回其节点值的 后序遍历 。

https://leetcode-cn.com/problems/binary-tree-postorder-traversal/
"""
from typing import Optional,List

from leetCode.utils.treeNodeUtil import TreeNode,init__binary_tree


class Solution:
    def postorderTraversal0(self,root: Optional[TreeNode]) -> List[int]:
        def visit(node: TreeNode):
            if node is None:
                return

            visit(node.left)
            visit(node.right)
            answer.append(node.val)

        answer = []
        visit(root)
        return answer

    def postorderTraversal(self,root: Optional[TreeNode]) -> List[int]:
        answer,stack,node,pre = [],[],root,None
        while stack or node:
            # 1. 都是一路网左进栈
            while node:
                stack.append(node)
                node = node.left

            # 2. 进到每次的左分支底部了，开始要弹栈访问了
            node = stack.pop()

            # 3. 在哪儿保存val
            # 此处根节点的处理特殊些，取出来了还可能再塞回栈里面
            # pre记录根节点从哪儿来的，如果是从右边来的，那么这次应该append到结果中
            if not node.right or node.right == pre:
                answer.append(node.val)
                pre = node
                node = None
            else:
                stack.append(node)
                pre = node
                node = node.right

        print(answer)
        return answer


s = Solution()
root = init__binary_tree([1,2,3])
print(s.postorderTraversal(root) == [2,3,1])

root = init__binary_tree([1,2,3,4,5,6,None,None,None,7,8])
print(s.postorderTraversal(root) == [4,7,8,5,2,6,3,1])

root = init__binary_tree([1,None,2,3])
print(s.postorderTraversal(root) == [3,2,1])

root = init__binary_tree([])
print(s.postorderTraversal(root) == [])

root = init__binary_tree([1])
print(s.postorderTraversal(root) == [1])
