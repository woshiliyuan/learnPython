# coding=utf-8
"""
309. 最佳买卖股票时机含冷冻期
给定一个整数数组prices，其中第  prices[i] 表示第 i 天的股票价格 。
设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/submissions/
"""
from typing import List


class Solution:
    # 动态规划
    def maxProfit0(self, prices: List[int]) -> int:
        length = len(prices)

        p = [[0] * 3 for _ in range(length)]
        p[0][0] = - prices[0]

        # f = [[-prices[0], 0, 0]] + [[0] * 3 for _ in range(length - 1)]

        for i in range(1, length):
            p[i][0] = max(p[i - 1][0], p[i - 1][2] - prices[i])
            p[i][1] = p[i - 1][0] + prices[i]
            p[i][2] = max(p[i - 1][1], p[i - 1][2])

        return max(p[-1][1], p[-1][2])

    # 2. 动态规划貌似都可以节省空间
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        p = [[-prices[0], 0, 0], [0, 0,  0]]

        for i in range(1, length):
            p[1][0] = max(p[0][0], p[0][2] - prices[i])
            p[1][1] = p[0][0] + prices[i]
            p[1][2] = max(p[0][1], p[0][2])

            p[0] = p[1].copy()

        return max(p[1][1], p[1][2])




s = Solution()
print(s.maxProfit([1, 2, 3, 0, 2]) == 3)
print(s.maxProfit([1, 4]) == 3)
print(s.maxProfit([4]) == 0)
