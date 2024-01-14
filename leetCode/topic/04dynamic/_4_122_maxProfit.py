# coding=utf-8
"""
122. 买卖股票的最佳时机 II
给你一个整数数组 prices ，其中 prices[i] 表示某支股票第 i 天的价格。
在每一天，你可以决定是否购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。你也可以先购买，然后在 同一天 出售。
返回 你能获得的 最大 利润 。

https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/
"""
from typing import List


class Solution:
    # 1. 动态规划
    def maxProfit1(self, prices: List[int]) -> int:
        length = len(prices)
        # profit[i] = [第i天持有股票的最大收益，第i天没有股票的最大收益]
        profit = [[0, 0] for _ in range(length)]
        profit[0][0] = -prices[0]

        for i in range(1, length):
            profit[i][0] = max(profit[i - 1][0], profit[i - 1][1] - prices[i])
            profit[i][1] = max(profit[i - 1][0] + prices[i], profit[i - 1][1])

        return profit[-1][1]

    # 2. 动态规划，节省内存版本
    def maxProfit2(self, prices: List[int]) -> int:
        # 第i天没有股票的最大收益 第i天持有股票的最大收益
        p0, p1 = 0, -prices[0]
        for i in range(1, len(prices)):
            p0, p1 = max(p1 + prices[i], p0), max(p1, p0 - prices[i])
        return p0

    # 3. 贪心算法，这也可以？
    def maxProfit3(self, prices: List[int]) -> int:
        p = 0
        for i in range(1, len(prices)):
            p += max(0, prices[i] - prices[i - 1])
        return p

    # 4. 贪心算法，解法二
    def maxProfit4(self, prices: List[int]) -> int:
        p, buy_min = 0, prices[0]
        for i in range(1, len(prices)):
            if prices[i] < buy_min:
                buy_min = prices[i]
            else:
                p += prices[i] - buy_min
                buy_min = prices[i]
        return p

    # 5. 属于贪心算法吗？：极值低点买，极值高点卖，操作完整上升的线
    def maxProfit(self, prices: List[int]) -> int:
        p = 0

        # 特殊处理开头和结尾
        if len(prices) > 1:
            if prices[1] > prices[0]: p -= prices[0]
            if prices[-1] > prices[-2]: p += prices[-1]

        for i in range(1, len(prices) - 1):
            # 极值低点: 2,2,5
            if prices[i - 1] >= prices[i] < prices[i + 1]:
                p -= prices[i]
            # 极值高点 2 5 5
            elif prices[i - 1] < prices[i] >= prices[i + 1]:
                p += prices[i]
        return p


s = Solution()
# print(s.maxProfit([7, 1, 5, 3, 6, 4]) == 7)
# print(s.maxProfit([1, 2, 3, 4, 5]) == 4)
# print(s.maxProfit([7, 6, 4, 3, 1]) == 0)
print(s.maxProfit([2,2,5]) == 3)
