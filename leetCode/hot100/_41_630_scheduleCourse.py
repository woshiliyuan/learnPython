# coding=utf-8
"""
630. 课程表 III
这里有 n 门不同的在线课程，按从 1 到 n 编号。给你一个数组 courses ，其中 courses[i] = [durationi, lastDayi] 表示第 i 门课将会 持续 上 durationi 天课，并且必须在不晚于 lastDayi 的时候完成。
你的学期从第 1 天开始。且不能同时修读两门及两门以上的课程。
返回你最多可以修读的课程数目。

https://leetcode-cn.com/problems/course-schedule-iii/
"""
from typing import List


class Solution:
    def scheduleCourse(self,courses: List[List[int]]) -> int:
        row,col = len(courses),0


s = Solution()
print(s.scheduleCourse([[100,200],[200,1300],[1000,1250],[2000,3200]]) == [1])
print(s.scheduleCourse(6,[[3,0],[3,1],[3,2],[3,4],[5,4]]) == [3,4])
