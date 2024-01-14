# coding=utf-8
"""
236. 二叉树的最近公共祖先
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
"""

from leetCode.utils.treeNodeUtil import TreeNode,init__binary_tree,get_node


class Solution:
    # 1. 存储父节点路径
    # 1.1 数组存储所有的路径
    def lowestCommonAncestor0(self,root: TreeNode,p: 'TreeNode',q: 'TreeNode') -> 'TreeNode':
        def postorder(node: TreeNode,path):
            if node is None or len(visited) == 2:
                return

            path = path + [node]
            # path += [node] // 错误
            if node == p or node == q:
                visited.append(path)
            postorder(node.left,path)
            postorder(node.right,path)

        visited = []
        postorder(root,[])

        size = min(len(visited[0]),len(visited[1]))
        for i in range(size - 1,-1,-1):
            if visited[0][i] == visited[1][i]:
                return visited[0][i]

        return root

    # 1.2 官方，map存储所有节点的父节点

    # 2. 递归
    # 2.1 记录左右子树节点
    def lowestCommonAncestor2(self,root: TreeNode,p: 'TreeNode',q: 'TreeNode') -> 'TreeNode':
        def find_sons(node):
            nonlocal ancestor
            if node is None or ancestor: return 0

            # 递归问题类似于动态规划，割裂到一个局部树(以node为顶点，往下到底的)中来统计找到多少个
            nums = find_sons(node.left)
            nums += find_sons(node.right)

            if ancestor: return 0

            if node == p or node == q:
                nums += 1
            # 全局变量来记录第一次出现nums=2的情况
            if nums == 2:
                ancestor = node
            return nums

        ancestor = None
        find_sons(root)
        return ancestor

    # 2.2. 官方思想：递归记录左右子树是否能找到，只要有一个就可以为true
    def lowestCommonAncestor(self,root: TreeNode,p: 'TreeNode',q: 'TreeNode') -> 'TreeNode':
        def find_son(node: TreeNode):
            nonlocal ancestor
            # ancesotr剪枝不再往下
            if not node or ancestor: return

            left = find_son(node.left)
            right = find_son(node.right)
            # 剪枝，不再往上返回; 但是这种做法这个地方不判断也可以，我数个数做法此处一定得剪枝
            # if ancestor: return
            if (left and right) or ((left or right) and (node == p or node == q)):
                ancestor = node
            return left or right or node == p or node == q

        ancestor = None
        find_son(root)
        return ancestor


s = Solution()
root = init__binary_tree([3,5,1,6,2,0,8,None,None,7,4])
print(s.lowestCommonAncestor(root,get_node(root,5),get_node(root,1)).val == 3)

root = init__binary_tree([3,5,1,6,2,0,8,None,None,7,4])
print(s.lowestCommonAncestor(root,get_node(root,5),get_node(root,4)).val == 5)

root = init__binary_tree([3,5,1,6,2,0,8,None,None,7,4])
print(s.lowestCommonAncestor(root,get_node(root,6),get_node(root,8)).val == 3)

root = init__binary_tree([1,2])
print(s.lowestCommonAncestor(root,get_node(root,1),get_node(root,2)).val == 1)


def plus():
    """
    解释上面的 path = path + [node]; path += [node]
    """
    a = 3
    b = a
    a += 2
    print(a,b)

    a = 3
    b = a
    a = a + 2
    print(a,b)

    b = [1,2]
    a = b
    b += [3]
    print(b,a)

    b = [1,2]
    a = b
    b = b + [3]
    print(b,a)

# plus()
