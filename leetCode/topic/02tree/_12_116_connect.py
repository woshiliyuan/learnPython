# coding=utf-8
"""
116. 填充每个节点的下一个右侧节点指针
给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
初始状态下，所有 next 指针都被设置为 NULL。

https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/
"""

from typing import Optional

from leetCode.utils.treeNodeUtil import init__binary_tree


class Solution:
    def connect(self, root) -> 'Optional[Node]':
        def visit(node, level: int):
            if node is None:
                return

            if len(answer) - 1 < level:
                answer.append(node)
            else:
                answer[level].next = node
                answer[level] = node
            visit(node.left, level + 1)
            visit(node.right, level + 1)

        answer = []
        visit(root, 0)
        return root

    def verify(self, root):
        answer = []
        node = root
        left_node = node.left

        while left_node or node:
            if node is None:
                answer.append("#")
                node = left_node
                left_node = left_node.left
            else:
                answer.append(node.val)
                node = node.next
        answer.append("#")
        print(answer)
        return answer


s = Solution()
root = init__binary_tree([1,2,3,4,5,6,7])
print(s.connect(root))
print(s.verify(root) == [1, "#", 2, 3, "#", 4, 5, 6, 7, "#"])


