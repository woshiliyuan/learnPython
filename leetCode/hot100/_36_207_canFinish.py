# coding=utf-8
"""
207. 课程表
你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。
在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。
例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false

https://leetcode-cn.com/problems/course-schedule/
"""
import collections
from typing import List


class Solution:
    # 队列广度优先遍历
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 有向图结构：start: [结束点]
        graph = collections.defaultdict(list)
        # 每个点的入度多少，下标对应顶点。这得要求所有顶点度是从0->n依次编号，不能乱哦
        entry_num = [0] * numCourses

        # 1. 初始化图和出度数组
        # 因为只是判断有无环型，所以 start->end; end->start都无所谓，只要统一就好
        for [start, end] in prerequisites:
            graph[start].append(end)
            entry_num[end] += 1

        # 2. 初始化队列
        queue, visited_num = [], 0
        for i in range(numCourses):
            if entry_num[i] == 0:
                queue.append(i)

        # 官方等价写法
        # q = collections.deque([u for u in range(numCourses) if entry_num[u] == 0])

        # 3. 直到队列为空
        while queue:
            start = queue.pop(0)
            visited_num += 1
            for end in graph[start]:
                entry_num[end] -= 1
                if entry_num[end] == 0:
                    queue.append(end)
        # print(visited_num)
        return visited_num == numCourses

    # 深度优先遍历
    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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

        # 1. 初始化图；和广度遍历（graph[start].append(end)）添加顺序不一致
        graph = collections.defaultdict(list)
        for [start, end] in prerequisites:
            graph[end].append(start)

        answer, visited, no_cycle = [], [0]*numCourses, True
        for i in range(numCourses):
            if no_cycle and not visited[i]:
                dfs(i)
        # print(answer)
        return no_cycle


s = Solution()

print(s.canFinish(2, [[1,0]]) is True)
print(s.canFinish(2, [[0,1]]) is True)
print(s.canFinish(1, []) is True)
print(s.canFinish(2, [[1,0],[0,1]]) is False)

print(s.canFinish(7,
                  [[0,2],[0,4],[0,5]
                   ,[1,0],[1,2]
                   ,[3,5]
                   ,[5,4],[5,6]
                  ]) is True)
