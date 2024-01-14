# coding=utf-8
"""
990. 等式方程的可满足性
给定一个由表示变量之间关系的字符串方程组成的数组，每个字符串方程 equations[i] 的长度为 4，并采用两种不同的形式之一："a==b" 或 "a!=b"。在这里，a 和 b 是小写字母（不一定不同），表示单字母变量名。
只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回 true，否则返回 false。

https://leetcode.cn/problems/satisfiability-of-equality-equations/
"""
from typing import List


class Solution:
    class UnionFind:
        def __init__(self):
            self.parent = list(range(26))

        def find(self, index):
            if index == self.parent[index]:
                return index
            # 这样是只查找，不压缩路径
            # return self.find(self.parent[index])
            # 太精妙了，一边查找，一边压缩路径
            self.parent[index] = self.find(self.parent[index])
            return self.parent[index]

        def union(self, index1, index2):
            self.parent[self.find(index1)] = self.find(index2)

    # 1. 官方题解，封装成对象了
    def equationsPossible1(self, equations: List[str]) -> bool:
        uf = Solution.UnionFind()

        # 1. 构造并查集
        for st in equations:
            if st[1] == "=":
                index1 = ord(st[0]) - ord("a")
                index2 = ord(st[3]) - ord("a")
                uf.union(index1, index2)

        for st in equations:
            if st[1] == "!":
                index1 = ord(st[0]) - ord("a")
                index2 = ord(st[3]) - ord("a")
                if uf.find(index1) == uf.find(index2):
                    return False
        return True

    # 2. 改版为：整个到一个函数内，拆掉了对象
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = list(range(26))

        def union(s1, s2):
            i1 = ord(s1) - 97
            i2 = ord(s2) - 97
            parent[find(i1)] = find(i2)

        def find(i):
            if i == parent[i]: return i
            parent[i] = find(parent[i])
            return parent[i]

        for eq in equations:
            if eq[1] == "=":
                union(eq[0], eq[3])

        for eq in equations:
            if eq[1] == "!":
                i1 = ord(eq[0]) - 97
                i2 = ord(eq[3]) - 97
                if find(i1) == find(i2): return False

        return True



s = Solution()
print(s.equationsPossible(["a==b", "b!=a"]) is False)
print(s.equationsPossible(["b==a", "a==b"]))
print(s.equationsPossible(["a==b", "b==c", "a==c"]))
print(s.equationsPossible(["a==b", "b!=c", "c==a"]) is False)
print(s.equationsPossible(["c==c", "b==d", "x!=z"]))

print(list(range(26)))
a = [i for i in range(26)]
print(a)

print(ord('a'))

