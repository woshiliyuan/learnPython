# coding=utf-8
"""
429. N 叉树的层序遍历
给定一个 N 叉树，返回其节点值的层序遍历。（即从左到右，逐层遍历）。
树的序列化输入是用层序遍历，每组子节点都由 None 值分隔（参见示例）。

https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/
"""

from typing import List

from leetCode.utils.treeNodeUtil import init_tree,Node


class Solution:
    def levelOrder0(self, root: Node) -> List[List[int]]:
        def visit(node: Node, level: int):
            if node is None:
                return

            if len(answer) - 1 < level:
                answer.append([])

            answer[level].append(node.val)
            for son_node in node.children:
                visit(son_node, level + 1)

        answer = []
        visit(root, 0)
        return answer

    # 广度遍历写一次
    def levelOrder(self, root: Node) -> List[List[int]]:
        if not root: return []
        answer, queue = [], [root]
        while queue:
            level = []
            for _ in range(len(queue)):
                root = queue.pop(0)
                level.append(root.val)
                queue.extend(root.children)
            answer.append(level)
        return answer


s = Solution()
root = init_tree([1,None,3,2,4,None,5,6])
print(s.levelOrder(root))
print(s.levelOrder(root) == [[1],[3,2,4],[5,6]])

root = init_tree([1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,14])
print(s.levelOrder(root) == [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]])

root = init_tree([1])
print(s.levelOrder(root) == [[1]])

root = init_tree([])
print(s.levelOrder(root) == [])

