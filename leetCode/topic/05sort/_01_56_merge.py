# coding=utf-8
"""
56. 合并区间
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。

https://leetcode-cn.com/problems/merge-intervals/
"""
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda e:e[0])
        answer = []
        for interval in intervals:
            if not answer or answer[-1][1] < interval[0]:
                answer.append(interval)
            else:
                answer[-1][1] = max(answer[-1][1], interval[1])
        return answer


solution = Solution()
print(solution.merge([[1,3],[2,6],[8,10],[15,18]])) # [[1,6],[8,10],[15,18]]
print(solution.merge([[1,4],[4,5]])) # [[1,5]]
print(solution.merge([[1,4],[4,5]])) # [[1,5]]





