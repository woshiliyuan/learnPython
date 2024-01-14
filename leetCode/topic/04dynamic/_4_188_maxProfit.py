# coding=utf-8
"""
188. 买卖股票的最佳时机 IV
给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）

https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/
"""
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0 or prices == []: return 0
        # 0 1 2 3 4 5
        # 0   1   2
        size = 2 * k
        p = [0] * size

        # 1. 初始化
        for j in range(size):
            if j % 2 == 0: p[j] = -prices[0]

        for i in range(1, len(prices)):
            p[0], flag = max(p[0], -prices[i]), 1
            for j in range(1, size):
                # 一次卖，一次买，不断循环
                p[j], flag = max(p[j], p[j-1] + flag * prices[i]), -flag
        print(p)
        return p[-1]


s = Solution()
print(s.maxProfit(2, [2, 4, 1]) == 2)
print(s.maxProfit(2, [3, 2, 6, 5, 0, 3]) == 7)
# 变态的边界条件
print(s.maxProfit(2, []) == 0)
print(s.maxProfit(0, [1,3]) == 0)


