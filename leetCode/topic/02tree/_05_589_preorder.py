# coding=utf-8
"""
589. N 叉树的前序遍历
给定一个 n 叉树的根节点  root ，返回 其节点值的 前序遍历 。
n 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔（请参见示例）。

https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/
"""
from typing import List

from leetCode.utils.treeNodeUtil import init_tree,Node


class Solution:
    def preorder0(self,root: 'Node') -> List[int]:
        def visit(node: Node):
            if node is None:
                return

            answer.append(node.val)
            for child in node.children:
                visit(child)

        answer = []
        visit(root)
        return answer

    def preorder1(self,root: 'Node') -> List[int]:
        answer,stack = [],[]
        while stack or root:
            stack.extend(root.children[::-1])
            answer.append(root.val)
            if stack:
                root = stack.pop()
            else:
                root = None
        return answer

    def preorder(self,root: 'Node') -> List[int]:
        if not root: return []
        answer,stack = [],[root]
        while stack:
            stack.extend(root.children[::-1])
            answer.append(root.val)
            root = stack.pop()
        return answer


s = Solution()
root = init_tree([1,None,3,2,4,None,5,6])
print(s.preorder(root))
print(s.preorder(root) == [1,3,5,6,2,4])

root = init_tree([1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,14])
print(s.preorder(root) == [1,2,3,6,7,11,14,4,8,12,5,9,13,10])

root = init_tree([])
print(s.preorder(root) == [])
