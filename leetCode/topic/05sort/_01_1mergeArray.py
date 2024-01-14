# coding=utf-8
"""
https://leetcode-cn.com/problems/merge-two-sorted-lists/
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
示例：
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]

示例 2：
输入：l1 = [], l2 = []
输出：[]

示例 3：
输入：l1 = [], l2 = [0]
输出：[0]
"""

# 这次合并数组
from typing import List


class Solution:
    def mergeTwoLists(self, l1: List[int], l2: List[int]) -> List[int]:
        result = []
        i, j = 0, 0
        while i < len(l1) and j < len(l2):
            if l1[i] <= l2[j]:
                result.append(l1[i])
                i = i + 1
            else:
                result.append(l2[j])
                j = j + 1
        # 说明最终是l1没走完，还剩下了
        result.extend(l1[i:] if i < len(l1) else l2[j:])
        return result


solution = Solution()

l1 = [1, 2, 4, 5, 6]
l2 = [1, 3, 4]
result = solution.mergeTwoLists(l1, l2)
print(result == [1, 1, 2, 3, 4, 4, 5, 6])

l1 = []
l2 = []
result = solution.mergeTwoLists(l1, l2)
print(result == [])

l1 = []
l2 = [0]
result = solution.mergeTwoLists(l1, l2)
print(result == [0])
