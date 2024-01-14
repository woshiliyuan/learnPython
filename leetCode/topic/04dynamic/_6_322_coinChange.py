# coding=utf-8
"""
322. 零钱兑换
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
你可以认为每种硬币的数量是无限的。

https://leetcode-cn.com/problems/coin-change/
"""
import functools
import sys
from typing import List


class Solution:
    # ------- 1. 动态规划 ---------
    # 1.1 超出时间限制
    def coinChange0(self,coins: List[int],amount: int) -> int:
        coins_set = set(coins)
        nums = [0] * (amount + 1)
        for i in range(1,amount + 1):
            min_num = 100
            for j in range(0,i):
                if nums[j] != -1 and (i - j) in coins_set:
                    min_num = min(min_num,nums[j])
            if min_num < 100:
                nums[i] = 1 + min_num
            else:
                nums[i] = -1
        return nums[-1]

    # 1.2 改进下，不要从 i->len； 只遍历coins数组本身
    def coinChange1(self,coins: List[int],amount: int) -> int:
        nums = [0] * (amount + 1)
        for i in range(1,amount + 1):
            min_num = 10000
            for c in coins:
                if i - c >= 0 and nums[i - c] != -1:
                    min_num = min(min_num,nums[i - c])

            nums[i] = 1 + min_num if min_num < 10000 else -1

        return nums[-1]

    # ------------------  2. 递归  ---------------
    # 澜澜老师，队列实现树的广度遍历： 求最小树高度
    def coinChange(self,coins: List[int],amount: int) -> int:
        queue,level,visited = [amount],0,set()

        while queue:
            level += 1
            # 层序遍历
            for _ in range(len(queue)):
                node = queue.pop(0)
                for c in coins:
                    rest = node - c
                    if rest == 0: return level
                    # visited去掉重复的节点
                    if rest > 0 and rest not in visited:
                        visited.add(rest)
                        queue.append(rest)

        return 0 if amount == 0 else -1

    # 直接递归
    def coinChange2(self,coins: List[int],amount: int) -> int:
        def dfs(res,count):
            if res < 0: return

            nonlocal min_count
            if res == 0:
                min_count = min(min_count,count)
                return

            # 剩下的都rest > 0
            for c in coins:
                dfs(res - c,count + 1)

        min_count = amount + 1
        dfs(amount,0)
        return min_count if min_count != (amount + 1) else -1

    # 加了缓存的递归
    def coinChange2(self,coins: List[int],amount: int) -> int:
        # 神奇的一句，可以缓存递归函数
        @functools.lru_cache(amount)
        def dfs(res):
            if res < 0: return -1
            if res == 0: return 0

            min_count = sys.maxsize
            for c in coins:
                count = dfs(res - c)
                if min_count > count >= 0:
                    min_count = count + 1
            return min_count if min_count < sys.maxsize else -1

        return dfs(amount)


s = Solution()
# print(s.coinChange([1, 2, 5], 11) == 3)
# print(s.coinChange([2], 3) == -1)
# print(s.coinChange([1], 0) == 0)
print(s.coinChange([186,419,83,408],6249) == 20)
