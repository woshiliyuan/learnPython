# coding=utf-8
"""
给你两个非空 的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
链接：https://leetcode-cn.com/problems/add-two-numbers
"""
from leetCode.utils.listNodeUtil import ListNode,init_nodes,visit_list


class Solution:
    def addTwoNumbers0(self,l1: ListNode,l2: ListNode) -> ListNode:
        """
        尝试不新建新的链表，失败告终；
        链表结果需要存储在长的那个链表里面，但是一开始根本不知道哪个链表是长的
        :return:
        """
        head = l1

        # 1. 同时移动l1,l2, 相加完成相同的位数
        sum = 0
        while l1 and l2:
            sum += l1.val + l2.val
            l1.val = sum % 10
            l1,l2,sum = l1.next,l2.next,sum // 10

        # 2. 处理剩余位数
        while l1:
            sum += l1.val
            l1.val,sum = sum % 10,sum // 10
            if l1.next:
                l1 = l1.next
            else:
                if sum == 1:
                    l1.next,l1 = ListNode(1,None),None

        while l2:
            sum += l2.val
            # 接下来太复杂了，l1.next = l2

        return head

    # 1. 链表合并操作一般都新建一个节点
    def addTwoNumbers1(self,l1: ListNode,l2: ListNode) -> ListNode:
        head = p = ListNode()
        carry = 0

        # 1. 先遍历完一样的长度
        while l1 and l2:
            sum = carry + l1.val + l2.val

            # 这一行为什么会报错呢？
            # p.next, p = ListNode(sum % 10), p.next
            p.next = ListNode(sum % 10)
            p = p.next

            l1,l2,carry = l1.next,l2.next,sum // 10

        # 2. 指向那个长的指针
        l3 = l1 if l1 else l2

        # 3. 把长的尾部遍历完
        while l3:
            sum = carry + l3.val
            p.next = ListNode(sum % 10)
            p,carry = p.next,sum // 10
            l3 = l3.next

        # 4. 如果尾部有进位，得+1
        if carry == 1:
            p.next = ListNode(1)

        return head.next

    def addTwoNumbers(self,l1: ListNode,l2: ListNode) -> ListNode:
        head = p = ListNode()
        carry = 0

        # 1. 先遍历完一样的长度
        while l1 or l2:
            sum = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)

            p.next = ListNode(sum % 10)
            p = p.next
            carry = sum // 10

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # 2. 如果尾部有进位，得+1
        if carry == 1:
            p.next = ListNode(1)

        return head.next


solution = Solution()
l1 = init_nodes([2,4,3])
l2 = init_nodes([5,6,4])
r = solution.addTwoNumbers(l1,l2)
print(visit_list(r) == [7,0,8])  # 342 + 465 = 807

l1 = init_nodes([0])
l2 = init_nodes([0])
r = solution.addTwoNumbers(l1,l2)
print(visit_list(r) == [0])

l1 = init_nodes([9,9,9,9,9,9,9])
l2 = init_nodes([9,9,9,9])
r = solution.addTwoNumbers(l1,l2)
print(visit_list(r) == [8,9,9,9,0,0,0,1])

l2 = init_nodes([9,9,9,9,9,9,9])
l1 = init_nodes([9,9,9,9])
r = solution.addTwoNumbers(l1,l2)
print(visit_list(r) == [8,9,9,9,0,0,0,1])

l1 = init_nodes([9])
l2 = init_nodes([9])
r = solution.addTwoNumbers(l1,l2)
print(visit_list(r) == [8,1])
