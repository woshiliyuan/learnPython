# coding=utf-8
"""
590. N 叉树的后序遍历
给定一个 n 叉树的根节点 root ，返回 其节点值的 后序遍历 。
n 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 None 分隔（请参见示例）。

https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/
"""
from typing import List

from leetCode.utils.treeNodeUtil import init_tree,Node


class Solution:
    def postorder0(self,root: 'Node') -> List[int]:
        def visit(node: Node):
            if node is None:
                return
            for child in node.children:
                visit(child)
            answer.append(node.val)

        answer = []
        visit(root)
        return answer

    # 这也太优雅了吧
    def postorder(self,root: 'Node') -> List[int]:
        if not root: return None
        answer,stack = [],[root]
        while stack:
            root = stack.pop()
            answer.append(root.val)
            stack.extend(root.children)

        # answer.reverse()
        # return answer
        return answer[::-1]


s = Solution()
root = init_tree([1,None,3,2,4,None,5,6])
print(s.postorder(root) == [5,6,3,2,4,1])

root = init_tree([1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,14])
print(s.postorder(root) == [2,6,14,11,7,3,12,8,4,13,9,10,5,1])
