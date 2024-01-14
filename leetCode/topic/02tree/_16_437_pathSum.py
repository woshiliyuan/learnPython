# coding=utf-8
"""
437. 路径总和 III
给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。
路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

https://leetcode.cn/problems/path-sum-iii/
"""
import collections

from leetCode.utils.treeNodeUtil import init__binary_tree,TreeNode


class Solution:
    # 1. 官方题解一：o(n^2)复杂度
    def pathSum1(self, root: TreeNode, targetSum: int) -> int:
        # 以节点root为顶点，一直往左或者一直往右能求和为targetSum的个数
        def rootSum(root, targetSum):
            if root is None:
                return 0

            ret = 0
            if root.val == targetSum:
                ret += 1

            ret += rootSum(root.left, targetSum - root.val)
            ret += rootSum(root.right, targetSum - root.val)
            return ret

        if root is None:
            return 0

        ret = rootSum(root, targetSum)
        # 这个狠呀，递归遍历所有节点了
        ret += self.pathSum(root.left, targetSum)
        ret += self.pathSum(root.right, targetSum)
        return ret

    # 2. 官方题解二：前缀和 递归返回结果
    def pathSum2(self, root: TreeNode, targetSum: int) -> int:
        # key是前缀和, value是大小为key的前缀和出现的次数
        prefix = collections.defaultdict(int)
        # 前缀和为0的一条路径
        prefix[0] = 1

        def dfs(root, curr):
            """"
            curr: 由根结点到当前结点的路径上所有节点的和
            return: 以root为顶点，往下能又多少路径
            """
            if not root:
                return 0

            ret = 0
            curr += root.val

            # ---核心代码
            # 看看root到当前节点这条路上是否存在节点前缀和加target为currSum的路径
            # 当前节点->root节点反推，有且仅有一条路径，如果此前有和为currSum - target, 而当前的和又为currSum, 两者的差就肯定为target了
            # currSum - target相当于找路径的起点，起点的sum + target = currSum，当前点到起点的距离就是target
            ret += prefix[curr - targetSum]
            # 更新路径上当前节点前缀和的个数
            prefix[curr] += 1

            ret += dfs(root.left, curr)
            ret += dfs(root.right, curr)

            prefix[curr] -= 1

            return ret

        return dfs(root, 0)

    # 3. 前缀和：递归不返回结果，全局变量保存
    def pathSum3(self, root: TreeNode, targetSum: int) -> int:
        def dfs(node: TreeNode, curr):
            if not node: return
            nonlocal path_sum

            curr += node.val

            path_sum += prefix[curr - targetSum]
            prefix[curr] += 1

            dfs(node.left, curr)
            dfs(node.right, curr)

            prefix[curr] -= 1

        prefix, path_sum = collections.defaultdict(int), 0
        # 初始化一种情况，从根节点开始一路下来能找到的
        prefix[0] = 1
        dfs(root, 0)
        return path_sum

    # 3. 前缀和：递归参数传递prefix
    # 内存消耗较大：看来对于数组不应该复制一份传递
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def dfs(node: TreeNode, curr, prefix):
            if not node: return

            nonlocal path_sum
            curr += node.val

            path_sum += prefix[curr - targetSum]
            prefix[curr] += 1

            dfs(node.left, curr, prefix.copy())
            dfs(node.right, curr, prefix.copy())

        prefix, path_sum = collections.defaultdict(int), 0
        # 初始化一种情况，从根节点开始一路下来能找到的
        prefix[0] = 1
        dfs(root, 0, prefix)
        return path_sum


s = Solution()

root = init__binary_tree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
print(s.pathSum(root, 8) == 3)

root = init__binary_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
print(s.pathSum(root, 22) == 3)

root = init__binary_tree([1, -2, -3])
print(s.pathSum(root, -1) == 1)

root = init__binary_tree([1, 1, 3])
print(s.pathSum(root, 2) == 1)