# coding=utf-8
"""
310. 最小高度树
树是一个无向图，其中任何两个顶点只通过一条路径连接。 换句话说，一个任何没有简单环路的连通图都是一棵树。
给你一棵包含 n 个节点的树，标记为 0 到 n - 1 。给定数字 n 和一个有 n - 1 条无向边的 edges 列表（每一个边都是一对标签），其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间存在一条无向边。
可选择树中任何一个节点作为根。当选择节点 x 作为根节点时，设结果树的高度为 h 。在所有可能的树中，具有最小高度的树（即，min(h)）被称为 最小高度树 。
请你找到所有的 最小高度树 并按 任意顺序 返回它们的根节点标签列表。
树的 高度 是指根节点和叶子节点之间最长向下路径上边的数量。

https://leetcode-cn.com/problems/minimum-height-trees/
"""
import collections
from typing import List,Optional


class Solution:
    # 1. 广度遍历：遍历所有节点，超时。。。
    def findMinHeightTrees(self,n: int,edges: List[List[int]]) -> List[int]:
        # 1. 构造无向图
        graph = collections.defaultdict(list)
        for [start,end] in edges:
            graph[start].append(end)
            graph[end].append(start)

        # 2. 需要的结果
        answer,min_height = [],n

        # 3. 依次遍历所有的顶点为根
        for i in range(n):
            queue,visited,height = [i],[False] * n,0
            while queue:
                height += 1
                if height > min_height:
                    break

                for _ in range(len(queue)):
                    node = queue.pop(0)
                    visited[node] = True
                    for next_node in graph[node]:
                        if not visited[next_node]:
                            queue.append(next_node)

            # 遍历完了一个i
            if height < min_height:
                answer = [i]
                min_height = height
            elif height == min_height:
                answer.append(i)
        # print(answer)
        return answer


s = Solution()
print(s.findMinHeightTrees(4,[[1,0],[1,2],[1,3]]) == [1])
print(s.findMinHeightTrees(6,[[3,0],[3,1],[3,2],[3,4],[5,4]]) == [3,4])
