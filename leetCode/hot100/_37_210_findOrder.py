# coding=utf-8
"""
210. 课程表 II
现在你总共有 numCourses 门课需要选，记为 0 到 numCourses - 1。给你一个数组 prerequisites ，其中 prerequisites[i] = [ai, bi] ，表示在选修课程 ai 前 必须 先选修 bi 。
例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示：[0,1] 。
返回你为了学完所有课程所安排的学习顺序。可能会有多个正确的顺序，你只要返回 任意一种 就可以了。如果不可能完成所有课程，返回 一个空数组 。

https://leetcode-cn.com/problems/course-schedule-ii/
"""
import collections
from typing import List


class Solution:
    # 队列广度优先遍历
    def findOrder1(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 有向图结构：start: [结束点1，结束点2]
        graph = collections.defaultdict(list)
        # 每个点的入度多少，下标对应顶点。这得要求所有顶点度是从0->n依次编号，不能乱哦
        entry_num = [0] * numCourses

        # 1. 初始化图和出度数组
        for [start, end] in prerequisites:
            graph[end].append(start)
            entry_num[start] += 1

        # 2. 初始化队列
        queue, visited = [], []
        for i in range(numCourses):
            if entry_num[i] == 0:
                queue.append(i)

        # 3. 直到队列为空
        while queue:
            node = queue.pop(0)
            visited.append(node)
            for end_node in graph[node]:
                entry_num[end_node] -= 1
                if entry_num[end_node] == 0:
                    queue.append(end_node)
        # print(visited)
        return visited if len(visited) == numCourses else []

    # 深度优先遍历
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 遍历 a->b-> ... -> end
        def dfs(end):
            nonlocal no_cycle
            visited[end] = 1

            for start in graph[end]:
                # 不判断visited[start]，会无限循环
                if visited[start] == 0:
                    dfs(start)
                # 存在环了
                elif visited[start] == 1:
                    no_cycle = False
                    return

            # dfs在主函数中可以调用多次，所以这儿还不能设置为1，否则会被误判为环
            visited[end] = 2
            answer.append(end)

        # 1. 初始化图；和广度遍历（graph[end].append(start)）添加顺序不一致， 此处存储的是入度
        graph = collections.defaultdict(list)
        for [start, end] in prerequisites:
            graph[start].append(end)

        answer, visited, no_cycle = [], [0]*numCourses, True
        for i in range(numCourses):
            if no_cycle and not visited[i]:
                dfs(i)
        # print(answer)
        return answer if no_cycle else []


s = Solution()

print(s.findOrder(2, [[1, 0]]) == [0, 1])
print(s.findOrder(2, [[0, 1]]) == [1, 0])
print(s.findOrder(1, []) == [0])
print(s.findOrder(2, [[1, 0], [0, 1]]) == [])

print(s.findOrder(7,
                  [[0, 2], [0, 4], [0, 5]
                      , [1, 0], [1, 2]
                      , [3, 5]
                      , [5, 4], [5, 6]
                   ]) == [2, 4, 6, 5, 0, 3, 1])
