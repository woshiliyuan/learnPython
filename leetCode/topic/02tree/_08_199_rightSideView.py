# coding=utf-8
"""
199. 二叉树的右视图
给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

https://leetcode-cn.com/problems/binary-tree-right-side-view/
"""

from typing import List

from leetCode.utils.treeNodeUtil import init_tree, Node, TreeNode, init__binary_tree


class Solution:
    def rightSideView0(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        answer = []

        # s为每层结束时的分隔符
        queue, right = [root, 's'], None
        while queue:
            node = queue.pop(0)
            if node == 's':
                # 到最后了，这一把什么也没捞着
                if right is None:
                    break
                answer.append(right)
                queue.append('s')
                right = None
            else:
                right = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return answer


    def rightSideView1(self, root: TreeNode) -> List[List[int]]:
        def visit(node: TreeNode, level: int):
            if node is None:
                return

            if len(answer) - 1 < level:
                answer.append(node.val)
            else:
                answer[level] = node.val
            visit(node.left, level + 1)
            visit(node.right, level + 1)

        answer = []
        visit(root, 0)
        return answer

    # 改进上面的深度优先遍历
    def rightSideView(self, root: TreeNode) -> List[List[int]]:
        def visit(node: TreeNode, level: int):
            if node is None:
                return

            # if len(answer) - 1 < level:
            if len(answer) == level:
                answer.append(node.val)
            # 先右后左
            visit(node.right, level + 1)
            visit(node.left, level + 1)

        answer = []
        visit(root, 0)
        return answer

s = Solution()
root = init__binary_tree([1,2,3,None,5,None,4])
print(s.rightSideView(root))
print(s.rightSideView(root) == [1,3,4])

root = init__binary_tree([1,None,3])
print(s.rightSideView(root) == [1,3])

root = init__binary_tree([1])
print(s.rightSideView(root) == [1])

root = init__binary_tree([])
print(s.rightSideView(root) == [])

