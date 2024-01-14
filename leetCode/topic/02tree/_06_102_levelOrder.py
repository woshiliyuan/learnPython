# coding=utf-8
"""
102. 二叉树的层序遍历
给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。

https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
"""
from typing import List

from leetCode.utils.treeNodeUtil import TreeNode,init__binary_tree


class Solution:
    # 自己实现的，竟然还通过了
    def levelOrder0(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        answer = []

        # s为每层结束时的分隔符
        queue, level = [root, 's'], []
        while queue:
            node = queue.pop(0)
            if node == 's':
                # 到最后了，这一把什么也没捞着
                if not level:
                    break
                answer.append(level)
                queue.append('s')
                level = []
            else:
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return answer

    # 不二维数组装了，直接一维数组装起来
    def levelOrder1(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        answer = []

        queue, level = [root], []
        while queue:
            node = queue.pop(0)
            answer.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return answer

    # leetcode官方思路一: 太巧妙简洁了，
    def levelOrder2(self, root: TreeNode) -> List[List[int]]:
        def visit(node: TreeNode, level: int):
            if node is None:
                return

            if len(answer) - 1 < level:
                answer.append([])
            # 管你先序后续中序，只要遍历完就好，都能在本题中push进去; 如果不是这种二维数组承接，反而是不能用递归了吧
            answer[level].append(node.val)

            visit(node.left, level+1)
            visit(node.right, level+1)

        answer = []
        visit(root, 0)
        return answer

    # 管你先序后续中序，只要遍历完就好，都能在本题中push进去; 如果不是这种二维数组承接，反而是不能用递归了吧
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        def visit(node: TreeNode, level: int):
            if node is None:
                return

            visit(node.left, level + 1)
            visit(node.right, level + 1)

            if len(answer) - 1 < level:
                # 非前序，answer可能为[], 但是level第一次确实7这样，为了不错位，得提前插入好空[]
                for _ in range(level - len(answer) + 1):
                    answer.append([])
            answer[level].append(node.val)

        answer = []
        visit(root, 0)
        return answer

    def levelOrder3(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        answer, queue = [], [root]
        while queue:
            level = []
            for i in range(len(queue)):
                root = queue.pop(0)
                level.append(root.val)

                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            answer.append(level)
        return answer


s = Solution()
root = init__binary_tree([3, 9, 20, None, None, 15, 7])
print(s.levelOrder(root))
print(s.levelOrder(root) == [[3],[9,20],[15,7]])

root = init__binary_tree([1])
print(s.levelOrder(root) == [[1]])

root = init__binary_tree([])
print(s.levelOrder(root) == [])



