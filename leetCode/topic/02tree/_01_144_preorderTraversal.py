# coding=utf-8
"""
144. 二叉树的前序遍历
给你二叉树的根节点 root ，返回它节点值的 前序 遍历。

链接：https://leetcode-cn.com/problems/binary-tree-preorder-traversal/
"""
from typing import Optional,List

from leetCode.utils.treeNodeUtil import TreeNode,init__binary_tree


class Solution:
    # 1. 递归方式
    def preorderTraversal0(self,root: Optional[TreeNode]) -> List[int]:
        def visit(node: TreeNode):
            if node is None:
                return

            answer.append(node.val)
            visit(node.left)
            visit(node.right)

        answer = []
        visit(root)
        return answer

    # 2 迭代方式 - by myself: 感觉比官方的要简洁：栈内都是没访问过的
    def preorderTraversal1(self,root: Optional[TreeNode]) -> List[int]:
        answer,stack,node = [],[],root
        # 假设全是左孩子链路，那么stack将一直为空
        while stack or node:
            # 1. 如果node not None, 说明node.left一直存在; 当left不存在了，才从栈里面取值
            if not node:
                node = stack.pop()

            # 2. 右边的入栈保存
            if node.right:
                stack.append(node.right)

            # 3. 始终访问本身，左孩子，才是栈里面的右节点
            answer.append(node.val)
            node = node.left

        # print(answer)
        return answer

    # 简化只进栈未访问节点: 孩子节点都不访问，先减栈，等下一次访问
    def preorderTraversal(self,root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        answer,stack = [],[root]
        while stack:
            root = stack.pop()
            answer.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return answer

    # 官方题解：栈内都是访问过的
    def preorderTraversal2(self,root: TreeNode) -> List[int]:
        res,stack,node = list(),[],root

        while stack or node:
            # 1. 一直往左
            while node:
                res.append(node.val)
                # 一路往左都进栈，没必要吧？
                stack.append(node)
                node = node.left
            # 2. 弹出的node节点已经访问过的，需要去访问节点的右侧
            node = stack.pop()
            node = node.right
        return res


s = Solution()

root = init__binary_tree([1,2,3])
print(s.preorderTraversal(root) == [1,2,3])

root = init__binary_tree([1,2,3,4,None,5])
print(s.preorderTraversal(root) == [1,2,4,3,5])

root = init__binary_tree([1,2,3,4,5])
print(s.preorderTraversal(root) == [1,2,4,5,3])

root = init__binary_tree([1,None,2,3])
print(s.preorderTraversal(root) == [1,2,3])

root = init__binary_tree([])
print(s.preorderTraversal(root) == [])

root = init__binary_tree([1])
print(s.preorderTraversal(root) == [1])
