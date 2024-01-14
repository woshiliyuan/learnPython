# coding=utf-8
"""
515. 在每个树行中找最大值
给定一棵二叉树的根节点 root ，请找出该二叉树中每一层的最大值。

https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/
"""

from typing import List,Optional

from leetCode.utils.treeNodeUtil import TreeNode,init__binary_tree


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        def visit(node: TreeNode, level: int):
            if node is None:
                return

            if len(answer) - 1 < level:
                answer.append(node.val)
            elif node.val > answer[level]:
                answer[level] = node.val
            visit(node.left, level + 1)
            visit(node.right, level + 1)

        answer = []
        visit(root, 0)
        return answer


s = Solution()
root = init__binary_tree([1,3,2,5,3,None,9])
print(s.largestValues(root))
print(s.largestValues(root) == [1,3,9])

root = init__binary_tree([1, 2, 3])
print(s.largestValues(root) == [1, 3])

root = init__binary_tree([1])
print(s.largestValues(root) == [1])

root = init__binary_tree([])
print(s.largestValues(root) == [])

