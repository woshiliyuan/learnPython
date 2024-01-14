# coding=utf-8
"""
621. 任务调度器
给你一个用字符数组 tasks 表示的 CPU 需要执行的任务列表。其中每个字母表示一种不同种类的任务。
任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。
在任何一个单位时间，CPU 可以完成一个任务，或者处于待命状态。

然而，两个 相同种类 的任务之间必须有长度为整数 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。
你需要计算完成所有任务所需要的 最短时间 。

https://leetcode.cn/problems/task-scheduler/

这题目题意看的很费解呀，看这个好懂一些：
https://leetcode.cn/problems/task-scheduler/solution/jian-ming-yi-dong-de-javajie-da-by-lan-s-jfl9/
"""

import collections
from typing import List


class Solution:
    def leastInterval(self,tasks: List[str],n: int) -> int:
        """
        (maxExec−1)(n+1)+maxCount 和 ∣task∣ 中的较大值
        """
        task_dict = collections.defaultdict(int)
        for t in tasks:
            task_dict[t] += 1

        # 执行的最多次数
        max_exec = max(task_dict.values())
        # 有多少个任务执行次数为 max_exec
        max_count = 0
        for v in task_dict.values():
            if v == max_exec:
                max_count += 1

        greed = (max_exec - 1) * (n + 1) + max_count
        return max(greed,len(tasks))

    # 官方题解
    def leastInterval2(self,tasks: List[str],n: int) -> int:
        freq = collections.Counter(tasks)
        print(freq)
        # 最多的执行次数
        maxExec = max(freq.values())
        # 具有最多执行次数的任务数量
        maxCount = sum(1 for v in freq.values() if v == maxExec)
        print(maxExec,maxCount)

        return max((maxExec - 1) * (n + 1) + maxCount,len(tasks))


s = Solution()
print(s.leastInterval(["A","A","A","B","B","B"],2) == 8)
print(s.leastInterval(["A","A","A","B","B","B"],0) == 6)
print(s.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"],2) == 16)
