# coding=utf-8
"""
739. 每日温度
给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100

https://leetcode.cn/problems/daily-temperatures/
"""

from typing import List


class Solution:
    # 1. 暴力破解，o(n**2)
    def dailyTemperatures1(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        answer = [0] * length
        for i in range(length - 1):
            for j in range(i + 1, length):
                if temperatures[j] > temperatures[i]:
                    answer[i] = j - i
                    break
        return answer

    # 神奇的单调递减栈
    def dailyTemperatures2(self, temperatures: List[int]) -> List[int]:
        stack = []
        length = len(temperatures)
        answer = [0] * length
        for i in range(length):
            while stack and temperatures[i] > stack[-1][1]:
                top = stack.pop()
                answer[top[0]] = i - top[0]
            stack.append((i, temperatures[i]))
        return answer

    # 官方题解，栈里面只存i？ 牛呀
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        length = len(temperatures)
        answer = [0] * length
        for i in range(length):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                top = stack.pop()
                answer[top] = i - top
            stack.append(i)
        return answer






s = Solution()
print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0])
print(s.dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0])
print(s.dailyTemperatures([30, 60, 90]) == [1, 1, 0])
