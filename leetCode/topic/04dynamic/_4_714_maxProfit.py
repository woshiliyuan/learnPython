# coding=utf-8
"""
714. 买卖股票的最佳时机含手续费
给定一个整数数组 prices，其中 prices[i]表示第 i 天的股票价格 ；整数 fee 代表了交易股票的手续费用。
你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
返回获得利润的最大值。
注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。

https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
"""
from typing import List


class Solution:
    # 1. 动态规划
    def maxProfit0(self,prices: List[int],fee: int) -> int:
        # 手头没有股票的收益，拥有股票的收益
        p0,p1 = 0,-prices[0] - fee
        for i in range(1,len(prices)):
            p0,p1 = max(p0,p1 + prices[i]),max(p1,p0 - prices[i] - fee)
        return p0

    # 2. 贪心算法 改版122题：这样的贪心是错的，每次向上的线都买了&付了手续费
    def maxProfit2(self,prices: List[int],fee: int) -> int:
        p,length = 0,len(prices)

        for i in range(1,length):
            if prices[i] > prices[i - 1]:
                p += prices[i] - prices[i - 1]
                if i == length - 1 or (i < length - 1 and prices[i + 1] < prices[i]):
                    p -= fee
        print(p)
        return p

    # 3. 贪心算法
    def maxProfit(self,prices: List[int],fee: int) -> int:
        # 拥有一只股票，买入的最低价格
        p,buy_min = 0,prices[0] + fee
        for i in range(1,len(prices)):
            if prices[i] + fee < buy_min:
                buy_min = prices[i] + fee
            elif prices[i] > buy_min:
                p += prices[i] - buy_min
                buy_min = prices[i]
        return p


s = Solution()
print(s.maxProfit([1,3,2,8,4,9],2) == 8)
print(s.maxProfit([1,3,7,5,10,3],3) == 6)
