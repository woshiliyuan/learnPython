# coding=utf-8
"""
95. 不同的二叉搜索树 II
给你一个整数 n ，请你生成并返回所有由 n 个节点组成且节点值从 1 到 n 互不相同的不同 二叉搜索树 。可以按 任意顺序 返回答案。

https://leetcode-cn.com/problems/unique-binary-search-trees-ii/
"""
from typing import List

from leetCode.utils.treeNodeUtil import TreeNode


class Solution:
    def generateTrees(self,n: int) -> List[TreeNode]:
        def generate(start,end):
            if start > end: return [None]

            answer = []
            for i in range(start,end + 1):
                left_trees = generate(start,i - 1)
                right_trees = generate(i + 1,end)
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        answer.append(root)
            return answer

        return generate(1,n) if n else []

    def verify(self,roots: List[TreeNode]):
        answer = []
        for root in roots:
            temp,queue = [],[root]
            while queue:
                node = queue.pop(0)
                if node:
                    temp.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    temp.append(None)

            while temp[-1] is None:
                temp.pop()

            answer.append(temp)
        print(answer)
        return answer


s = Solution()
answer = s.generateTrees(3)
print(s.verify(answer) == [[1,None,2,None,3],[1,None,3,2],[2,1,3],[3,1,None,None,2],[3,2,None,1]])

answer = s.generateTrees(0)
print(answer)

answer = s.generateTrees(1)
print(s.verify(answer) == [[1]])
