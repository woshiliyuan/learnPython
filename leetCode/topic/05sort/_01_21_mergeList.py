# coding=utf-8
"""
21. 合并两个有序链表
https://leetcode-cn.com/problems/merge-two-sorted-lists/
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

这个题目有问题，输入示例给的是数组，实际运行时确实List
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
from leetCode.utils.listNodeUtil import ListNode, init_nodes, visit_list


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        node = result = ListNode()
        while l1 and l2:
            if l1.val <= l2.val:
                node.next, l1 = l1, l1.next
            else:
                node.next, l2 = l2, l2.next
            # 比数组要多上移动指针这一步
            node = node.next
        # 说明最终是l1没走完，还剩下了
        # if l1:
        #     node.next = l1
        # else:
        #     node.next = l2

        # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
        node.next = l1 if l1 else l2

        return result.next


solution = Solution()

l1 = init_nodes([1,2,4])
l2 = init_nodes([1,3,4])
result = solution.mergeTwoLists(l1, l2)
print(visit_list(result) == [1,1,2,3,4,4])

l1 = init_nodes([])
l2 = init_nodes([])
result = solution.mergeTwoLists(l1, l2)
print(visit_list(result) == [])

l1 = init_nodes([])
l2 = init_nodes([0])
result = solution.mergeTwoLists(l1, l2)
print(visit_list(result) == [0])


