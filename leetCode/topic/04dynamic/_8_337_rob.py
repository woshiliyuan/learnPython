# coding=utf-8
"""
337. 打家劫舍 III
小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为 root 。
除了 root 之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果 两个直接相连的房子在同一天晚上被打劫 ，房屋将自动报警。
给定二叉树的 root 。返回 在不触动警报的情况下 ，小偷能够盗取的最高金额

https://leetcode-cn.com/problems/house-robber-iii/
"""
import collections

from leetCode.utils.treeNodeUtil import TreeNode,init__binary_tree


class Solution:
    # 1. 暴力破解，遍历貌似不可行
    def rob1(self,root: TreeNode) -> int:
        def visit(node: TreeNode,rob_current: bool):
            nonlocal max_sum
            if node is None:
                return

            if rob_current:
                max_sum += node.val
                visit(node.left,False)
                visit(node.right,False)
            else:
                # visit(node.left, False)
                # visit(node.right, False)
                visit(node.left,True)
                visit(node.right,True)

        max_sum = 0
        visit(root,True)
        # visit(root, False, 0)
        print(max_sum)
        return max_sum

    # 2. 官方题解改编：time, o(n); space, o(n)
    def rob2(self,root: TreeNode) -> int:
        def visit(node: TreeNode):
            if node is None: return

            visit(node.left)
            visit(node.right)

            # 当前节点选：那么左右孩子一定不能选
            choose[node] = node.val + not_choose[node.left] + not_choose[node.right]
            # 当前节点不选：左右孩子完全自由，可选可不选
            not_choose[node] = max(choose[node.left],not_choose[node.left]) + max(choose[node.right],
                                                                                  not_choose[node.right])

        choose = collections.defaultdict(int)
        not_choose = collections.defaultdict(int)
        visit(root)
        return max(choose[root],not_choose[root])

    # 3. 节省空间复杂度
    def rob(self,root: TreeNode) -> int:
        def visit(node: TreeNode):
            if node is None: return 0,0

            choose_left,not_choose_left = visit(node.left)
            choose_right,not_choose_right = visit(node.right)

            # 当前节点选：那么左右孩子一定不能选
            choose = node.val + not_choose_left + not_choose_right
            # 当前节点不选：左右孩子完全自由，可选可不选
            not_choose = max(choose_left,not_choose_left) + max(choose_right,not_choose_right)
            return choose,not_choose

        return max(visit(root))


s = Solution()
root = init__binary_tree([3,4,5,1,3,None,1])
print(s.rob(root) == 9)

root = init__binary_tree([3,2,3,None,3,None,1])
print(s.rob(root) == 7)

# 不懂这是为何了
a = collections.defaultdict(int)
# print(a["x"], a.get("x"), a[None]) # 0, 0
# print(a.get("x"), a["x"]) # None, 0
