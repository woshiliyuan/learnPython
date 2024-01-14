# coding=utf-8
"""
121. 买卖股票的最佳时机
给定一个数组 prices ，它的第i 个元素prices[i] 表示一支给定股票第 i 天的价格。
你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

示例 1：
输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。

示例 2：
输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
"""
from typing import List


class Solution:
    def maxProfit0(self,prices: List[int]) -> int:
        """
        方法一：暴力破解: 遍历所有的，时间复杂度 o(n^2), 简洁好理解

        """
        result = 0
        for i in range(1,len(prices)):
            # 假设一定从i位置买入, 未来的某天卖出
            min_buy = min(prices[:i])
            result = max(result,prices[i] - min_buy)
        return result

    # 动态规划：第i天一定卖出
    def maxProfit2(self,prices: List[int]) -> int:
        """
        时间复杂度o(n)
        1. result: 最大收益，最后的return值
        2. max(前i天的return值, 第i天一定卖出的return值) =
        max(前i天的最大收益，第i天-前i天的最小值)
        [7,6,4,3,1]

        """
        result,buy_min = 0,prices[0]
        for i in range(1,len(prices)):  # 最0天卖出肯定收益为0
            result = max(result,prices[i] - buy_min)
            buy_min = min(prices[i],buy_min)
        return result

    # 非要强行套动态规划公式
    def maxProfit2(self,prices: List[int]) -> int:
        # 1. dp[i]: [0, 1]所能获取的最大收益
        dp,buy_min = [0] * len(prices),prices[0]
        for i in range(1,len(prices)):  # 最0天卖出肯定收益为0
            dp[i] = max(dp[i - 1],prices[i] - buy_min)
            buy_min = min(prices[i],buy_min)
        return dp[-1]

    def maxProfit(self,prices: List[int]) -> int:
        # 1. dp[i]: i一定卖出获取的最大收益
        dp,buy_min = [0] * len(prices),prices[0]
        for i in range(1,len(prices)):  # 最0天卖出肯定收益为0
            dp[i] = prices[i] - buy_min
            buy_min = min(prices[i],buy_min)
        return max(dp)

    # 公司需要leetcode竞赛，重写做一遍这题：
    def maxProfit3(self,prices: List[int]) -> int:
        right_max,length = prices.copy(),len(prices)
        # 1. 储存右边最大值: 能以哪个最大值卖掉
        for i in range(length - 2,-1,-1):
            right_max[i] = max(right_max[i],right_max[i + 1])

        max_profit = 0
        for i in range(length):
            max_profit = max(max_profit,right_max[i] - prices[i])
        return max_profit

    # 简化上面的，right_max只用一个值就好
    # 动态规划：第i天一定买入
    def maxProfit4(self,prices: List[int]) -> int:
        # 这种记录当前最大值的，一般一个值卖出时的最大值：right_max就可以，无需数组
        max_sell,max_profit = 0,0
        for i in range(len(prices) - 2,-1,-1):  # 最后一天买入肯定收益为0
            max_sell = max(max_sell,prices[i])
            max_profit = max(max_profit,max_sell - prices[i])
        return max_profit


s = Solution()
print(s.maxProfit([7,1,5,3,6,4]) == 5)

print(s.maxProfit([7,6,4,3,1]) == 0)

print(s.maxProfit([7,2,5,1,2]) == 3)
