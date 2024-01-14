# coding=utf-8
"""
399. 除法求值
给你一个变量对数组 equations 和一个实数值数组 values 作为已知条件，其中 equations[i] = [Ai, Bi] 和 values[i] 共同表示等式 Ai / Bi = values[i] 。每个 Ai 或 Bi 是一个表示单个变量的字符串。
另有一些以数组 queries 表示的问题，其中 queries[j] = [Cj, Dj] 表示第 j 个问题，请你根据已知条件找出 Cj / Dj = ? 的结果作为答案。
返回 所有问题的答案 。如果存在某个无法确定的答案，则用 -1.0 替代这个答案。如果问题中出现了给定的已知条件中没有出现的字符串，也需要用 -1.0 替代这个答案。
注意：输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。

https://leetcode.cn/problems/evaluate-division/
"""
import collections
from typing import List


class Solution:
    # 尝试其它方法：1. 都转成以字典序小的为映射； 2. 无向图
    def calcEquation1(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        condition, node = collections.defaultdict(list)
        for i in equations:
            big, small = equations[i]
            if big < small:
                big, small = small, big
                big = 1 / values

    # 2. 并查集
    def calcEquation2(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        parent, weight = {}, {}

        # 1. 查操作。一边查找，一边压缩路径
        def find(node):
            if parent[node] != node:
                p = find(parent[node])
                weight[node] *= weight[parent[node]]
                parent[node] = p
            return parent[node]

        def init(node):
            if node not in parent:
                parent[node] = node
                weight[node] = 1

        # 2. 并操作。
        def union(n1, n2, product):
            init(n1)
            init(n2)

            p1, p2 = find(n1), find(n2)
            if p1 == p2: return

            parent[p1] = p2
            weight[p1] = product * weight[n2] / weight[n1]

        for i in range(len(equations)):
            union(equations[i][0], equations[i][1], values[i])

        answer = []
        for x, y in queries:
            if x not in parent or y not in parent:
                answer.append(-1)
                continue

            px, py = find(x), find(y)
            if px == py:
                answer.append(weight[x] / weight[y])
            else:
                answer.append(-1)
        return answer

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        uf = UF(equations)
        for eq, cnt in zip(equations, values):
            uf.union(eq[0], eq[1], cnt)

        ans = []
        for elem in queries:
            if elem[0] in uf.graph and elem[1] in uf.graph:
                div = uf.find(elem[0])
                bei_div = uf.find(elem[1])
                if div == bei_div:
                    ans.append(uf.weight[elem[1]] / uf.weight[elem[0]])
                else:
                    ans.append(-1)
            else:
                ans.append(-1)
        return ans


# 网友答案
class UF:
    def __init__(self, raw):
        self.graph = {}
        self.weight = {}
        for elem in raw:
            if elem[0] not in self.graph:
                self.weight[elem[0]] = 1
                self.graph[elem[0]] = elem[0]
            if elem[1] not in self.graph:
                self.weight[elem[1]] = 1
                self.graph[elem[1]] = elem[1]

    # int
    # origin = parent[x];
    # parent[x] = find(parent[x]);
    # weight[x] *= weight[origin];
    def find(self, target):
        if target != self.graph[target]:
            tmp = self.graph[target]
            self.graph[target] = self.find(self.graph[target])
            self.weight[target] = self.weight[target] * self.weight[tmp]
        return self.graph[target]

    def union(self, a, b, value):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_b == root_a:
            return False
        self.graph[root_b] = root_a
        self.weight[root_b] = self.weight[a] * value / self.weight[b]
        return True


s = Solution()
print(s.calcEquation([["a", "b"], ["b", "c"]], [2.0, 3.0], [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]])
      == [6.00000, 0.50000, -1.00000, 1.00000, -1.00000])
print(s.calcEquation([["a", "b"], ["b", "c"], ["bc", "cd"]], [1.5, 2.5, 5.0],
                     [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]])
      == [3.75000, 0.40000, 5.00000, 0.20000])
print(s.calcEquation([["a", "b"]], [0.5], [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]])
      == [0.50000, 2.00000, -1.00000, -1.00000])

