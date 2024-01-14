# coding=utf-8
"""
123. 买卖股票的最佳时机 III
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/
"""
from typing import List


class Solution:
    # 1. 动态规划: 这写的是 最多可以同时持有两只股票？
    def maxProfit0(self,prices: List[int]) -> int:
        p0,p1,p2 = 0,-prices[0],-prices[0]
        for i in range(1,len(prices)):
            t0 = max(p0,p1 + prices[i])
            t1 = max(p1,p0 - prices[i],p2 + prices[i])
            t2 = max(p2,p1 - prices[i])
            p0,p1,p2 = t0,t1,t2
        print(p0)
        return p0

    # 2. 官方题解：动态规划
    def maxProfit2(self,prices: List[int]) -> int:
        """
未进行过任何操作；
buy1:   只进行过一次买操作；
sell1:  进行了一次买操作和一次卖操作，即完成了一笔交易；
buy2:   在完成了一笔交易的前提下，进行了第二次买操作；
sell2:  完成了全部两笔交易。
        """
        buy1,sell1,buy2,sell2 = -prices[0],0,-prices[0],0
        for i in range(1,len(prices)):
            # 1. 不能[在同一天买入并且卖出]
            # t1 = max(buy1, -prices[i])
            # t2 = max(sell1, buy1 + prices[i])
            # t3 = max(buy2, sell1 - prices[i])
            # t4 = max(sell2, buy2 + prices[i])
            # buy1, sell1, buy2, sell2 = t1, t2, t3, t4

            # 2. 可以[在同一天买入并且卖出], 等同于上一种情况
            # 1: buy1, sell1 = -3, n;  prices[i] = 5. 这种情况不影响; t1=max(buy1, -prices[i])=buy1
            # 2: buy1, sell1 = -3, n;  prices[i] = 2. 考虑这种情况
            buy1 = max(buy1,-prices[i])  # t1 = -2, t2 = max(n, -3+2)=n;  buy1=-2 sell1=max(n, -2+2)=n
            sell1 = max(sell1,buy1 + prices[i])  # 只要prices[i]<buy1, buy1=-prices[i]; sell1=n >=0
            buy2 = max(buy2,sell1 - prices[i])
            sell2 = max(sell2,buy2 + prices[i])

        # 不理解，为什么不用 max(sell1, sell2)  sell2 >= sell1:
        # 难道是因为sell1, sell2初始化值相同？ buy2+prices[i] < sell2, 就还是上次的sell2 ?
        return sell2

    # 3. 改版网友思想：分左右两个区间([1,n)共n-1种划分法)，分别求两个区间的最大收益，然后相加就是两次股票
    def maxProfit(self,prices: List[int]) -> int:
        length = len(prices)
        # 1. 先逆序得出dp[i]: 区间[i, length)所能获取的最大利益
        dp,max_sell = [0] * length,prices[-1]
        for i in range(length - 2,-1,-1):
            dp[i] = max(dp[i + 1],max_sell - prices[i])
            max_sell = max(max_sell,prices[i])

        # 2. 再顺序得出 [0, i]区间所能获取的最大利益
        min_buy,max_left = prices[0],0
        answer = 0
        for i in range(1,length):
            max_left = max(max_left,prices[i] - min_buy)
            min_buy = min(min_buy,prices[i])
            # [0, i] + [i, len-1)
            answer = max(answer,max_left + dp[i])
        return answer


s = Solution()
print(s.maxProfit([3,3,5,0,0,3,1,4]) == 6)
print(s.maxProfit([7,1,5,3,6,4]) == 7)
print(s.maxProfit([1,2,3,4,5]) == 4)
print(s.maxProfit([7,6,4,3,1]) == 0)


def test_swap():
    a,b,c,d = 1,2,3,4

    # a1 = a + 1
    # b1 = b + a
    # c1 = c + a
    # d1 = d + a
    # a, b, c, d = a1, b1, c1, d1

    # a, b, c, d = a + 1, b + a, c + a, d + a
    print(a,b,c,d)  # 2 3 4 5

    a = a + 1
    b = b + a
    c = c + a
    d = d + a
    print(a,b,c,d)  # 2 4 5 6
