# coding=utf-8
"""
105. 从前序与中序遍历序列构造二叉树
给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。

https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""
from typing import List

from leetCode.utils.treeNodeUtil import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        i = inorder.index(preorder[0])
        if i > 0:
            root.left = self.buildTree(preorder[1: 1+i], inorder[:i])
        if i + 1 < len(preorder):
            root.right = self.buildTree(preorder[i+1:], inorder[i+1:])

        return root

    # 非叶子节点，层次遍历打印出None
    def verify(self, root: TreeNode) -> bool:
        answer, queue = [], [root]
        while queue:
            root = queue.pop(0)
            if root is None:
                answer.append(None)
            else:
                answer.append(root.val)
                # a.只要当前节点不会空，管它下级是否有值，都塞入队列
                queue.append(root.left)
                queue.append(root.right)

        # 因为在步骤a中我没法判断是否为叶子节点了，即无法判断是否为最深层了，所以全部塞进去了，得去掉尾巴的None
        while answer[-1] is None:
            answer.pop()

        print(answer)
        return answer


s = Solution()
root = s.buildTree([3,9,20,15,7], [9,3,15,20,7])
print(s.verify(root) == [3,9,20,None,None,15,7])

root = s.buildTree([-1], [-1])
print(s.verify(root) == [-1])

root = s.buildTree([1, 2, 4, 7, 3, 5, 6], [4, 7, 2, 1, 5, 3, 6])
print(s.verify(root) == [1, 2, 3, 4, None, 5, 6, None, 7])