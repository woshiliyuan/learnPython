# coding=utf-8
"""
老师想给孩子们分发糖果，有 N个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。
你需要按照以下要求，帮助老师给这些孩子分发糖果：
每个孩子至少分配到 1 个糖果。
评分更高的孩子必须比他两侧的邻位孩子获得更多的糖果。
那么这样下来，老师至少需要准备多少颗糖果呢？

示例1：
输入：[1,0,2]
输出：5
解释：你可以分别给这三个孩子分发 2、1、2 颗糖果。

示例2：
输入：[1,2,2]
输出：4
解释：你可以分别给这三个孩子分发 1、2、1 颗糖果。
     第三个孩子只得到 1 颗糖果，这已满足上述两个条件。

本题精髓在示例2：相等情况下是可以不多的，只有评分大于才会更多糖果。对的，就是这么不公平

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/candy
"""
from typing import List


class Solution:
    def candy1(self,ratings: List[int]) -> int:
        """
        by myself:
        从位置i开始求最长的递减序列，到位置decrease_index， 再给这个区间赋值
        复杂度：o(2n)
        :param ratings:
        :return:
        """
        # result = [1 for i in range(len(ratings))]
        result = [1] * len(ratings)
        i = 0
        while i < len(ratings):
            # 找出从位置i开始的递减序列，最后一个位置为decrease_index
            decrease_index = self.find_descrease(i,ratings)
            print("decrease_index ",decrease_index)
            # 开始对数组ressult赋值， 区间：i -> decrease_index
            for j in range(i,decrease_index):
                result[j] = decrease_index - j + 1
            # ratings虽然从i往右边到decrease_index都是最大，但是可能大于左边
            if i > 0 and ratings[i] > ratings[i - 1]:
                result[i] = max(result[i],result[i - 1] + 1)
            # 跳过区间[i -> decrease_index]
            i = decrease_index + 1
        print(result)
        return sum(result)

    def find_descrease(self,index,ratings):
        """
        找出从index位置开始的最长递减序列
        :param index:
        :param ratings:
        :return: 递减到哪个位置
        """
        while index < len(ratings) - 1 and ratings[index] > ratings[index + 1]:
            index += 1
        return index

    def candy(self,ratings: List[int]) -> int:
        """
        参考官方答案: 竟然可以如此巧妙，不过复杂度也是o(2n),
        从左往右遍历一遍，保证右边比左边+1
        从右往左遍历一遍，保证左边比右边+1
        贪心算法体现在两遍都只顾当前，不考虑全局最优解？
        :param ratings:
        :return:
        """
        length = len(ratings)
        result = [1] * length
        # 第一遍: 从左往右
        for i in range(1,length):
            if ratings[i] > ratings[i - 1]:
                result[i] = result[i - 1] + 1
        print(result)
        # 第二遍：从右往左
        for i in range(length - 2,-1,-1):
            if ratings[i] > ratings[i + 1]:
                result[i] = result[i + 1] + 1
            if i > 0 and ratings[i] > ratings[i - 1]:
                result[i] = max(result[i],result[i - 1] + 1)
        print(result)
        return sum(result)


solution = Solution()
list = [1,0,2]
print(solution.candy(list))

list = [1,2,2]
print(solution.candy(list))

list = [3,2,1]
print(solution.candy(list))

list = [1,2,3,4,3,2]
print(solution.candy(list))
