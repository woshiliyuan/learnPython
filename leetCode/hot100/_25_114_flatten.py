# coding=utf-8
"""
114. 二叉树展开为链表
给你二叉树的根结点 root ，请你将它展开为一个单链表：

展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
展开后的单链表应该与二叉树 先序遍历 顺序相同。
https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/
"""

from leetCode.utils.treeNodeUtil import TreeNode,init__binary_tree


class Solution:
    # 0. 我就要复制新节点
    def flatten0(self,root: TreeNode) -> None:
        def visit(root: TreeNode):
            if not root:
                return

            nonlocal new_root,pre
            temp = TreeNode(root.val)
            if not new_root:
                new_root = pre = temp
            else:
                pre.right = temp
                pre = temp

            visit(root.left)
            visit(root.right)

        if not root: return []

        new_root = pre = None
        visit(root)

        # 得改掉root本身，否则提交时验证通不过
        root.right = new_root.right
        root.left = None

    # 改递归呢？ 待续...
    def flatten(self,root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def visit(root: TreeNode) -> TreeNode:
            if root is None:
                return

            node = root.val

            visit(root.left)
            visit(root.right)

            return node

        return visit(root)

    # 2. 迭代做法，栈存下右节点
    def flatten2(self,root: TreeNode) -> None:
        if not root: return []
        stack,pre = [root],None
        while stack:
            root = stack.pop()

            # 精髓在于pre，而不是直接root.right = root.left; 因为如果root.left没有会非常麻烦
            # if not pre:
            #     pre = root
            # else:
            #     pre.left = None
            #     pre.right = root
            #     pre = root

            # 上面等价于
            if pre:
                pre.left = None
                pre.right = root
            pre = root

            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)

    # 3. 官方题解
    def flatten3(self,root: TreeNode) -> None:
        cur = root
        while cur:
            # 则在其左子树中找到最右边的节点，作为前驱节点pre, 不用去找前序遍历中cur的前一个
            pre = cur.left
            if cur.left:
                while pre.right:
                    pre = pre.right
                pre.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right

    def verify(self,root: TreeNode) -> bool:
        answer,queue = [],[root]
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
        while answer and answer[-1] is None:
            answer.pop()

        print(answer)
        return answer


s = Solution()
root = init__binary_tree([1,2,5])
s.flatten(root)
print(s.verify(root) == [1,None,2,None,5])

root = init__binary_tree([1,2,5,3,None,None,None,None,4])
s.flatten(root)
print(s.verify(root) == [1,None,2,None,3,None,4,None,5])

root = init__binary_tree([1,2,5,3,4])
s.flatten(root)
print(s.verify(root) == [1,None,2,None,3,None,4,None,5])

root = init__binary_tree([1,2,5,3,4,None,6])
s.flatten(root)
print(s.verify(root) == [1,None,2,None,3,None,4,None,5,None,6])

root = init__binary_tree([])
s.flatten(root)
print(s.verify(root) == [])

root = init__binary_tree([0])
s.flatten(root)
print(s.verify(root) == [0])
