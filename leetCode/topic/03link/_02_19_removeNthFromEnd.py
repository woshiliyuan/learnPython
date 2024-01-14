# coding=utf-8
"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/
"""
from leetCode.utils.listNodeUtil import ListNode, init_nodes, visit_list


class Solution:
    # 1. 暴力破解
    # 1. 先遍历获取链表长度为k, 倒数第n个, 遍历到第k-n+1停下来，删除操作

    # 2. 快慢指针两个节点
    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        # 1. 初始空节点头
        pre = ListNode(0, None)
        pre.next = head

        # 2. 先初始化p2, 空开n个距离
        p1, p2 = pre, pre
        for i in range(n):
            p2 = p2.next

        # 3. p2遍历到尾巴
        while p2.next:
            p1, p2 = p1.next, p2.next

        # 4. 删除节点
        p1.next = p1.next.next

        return pre.next

    # 这类删除链表节点的题目，没个空间点还真难搞... 应该是没法搞？
    # 1. p2一定得停在最后一个节点上，p1才能在倒数第n+1上
    # 2. p2和p1初始化在同一个位置，p2前进了n步，那么初始化一定是head前面的空间点
    # 3. head=[1] 这种，没空节点，没法 p1.next = p1.next.next
    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        p1, p2 = head, head
        for _ in range(n):
            p2 = p2.next

        while p2.next:
            p1, p2 = p1.next, p2.next

        p1.next = p1.next.next

        return head

    # 3. 栈的妙用
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pre = ListNode()
        pre.next = head
        stack, p = [], pre

        while p:
            stack.append(p)
            p = p.next

        for _ in range(n + 1):
            p = stack.pop()

        p.next = p.next.next
        return pre.next


solution = Solution()

list = [1, 2, 3, 4, 5]
head = init_nodes(list)
head = solution.removeNthFromEnd(head, 5)
print(visit_list(head) == [2, 3, 4, 5])

list = [1, 2]
head = init_nodes(list)
head = solution.removeNthFromEnd(head, 1)
print(visit_list(head) == [1])

list = [1]
head = init_nodes(list)
head = solution.removeNthFromEnd(head, 1)
print(visit_list(head) == [])
