# coding=utf-8
"""
142. 环形链表 II
给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
不允许修改 链表。

https://leetcode-cn.com/problems/linked-list-cycle-ii/
"""

from leetCode.utils.listNodeUtil import ListNode,init_cycle_nodes


class Solution:
    def detectCycle0(self,head: ListNode) -> ListNode:
        node_set = set()
        while head:
            if head in node_set:
                return head
            node_set.add(head)
            head = head.next
        return None

    def detectCycle(self,head: ListNode) -> ListNode:
        slow = fast = head
        # 如果有环，slow，fast能相遇
        while fast:
            slow,fast = slow.next,fast.next
            if fast:
                fast = fast.next
            if slow == fast and slow is not None:
                break

        if fast:
            p = head
            while slow != p:
                slow,p = slow.next,p.next
            return p

        return None


s = Solution()
head = init_cycle_nodes([3,2,0,-4],1)
print(s.detectCycle(head).val == 2)

head = init_cycle_nodes([3,2,0,-4],-1)
print(s.detectCycle(head) is None)

head = init_cycle_nodes([1,2],0)
print(s.detectCycle(head).val == 1)

head = init_cycle_nodes([1],-1)
print(s.detectCycle(head) is None)

head = init_cycle_nodes([1],0)
print(s.detectCycle(head).val == 1)

head = init_cycle_nodes([],-1)
print(s.detectCycle(head) is None)
