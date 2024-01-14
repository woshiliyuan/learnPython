# coding=utf-8
"""
148. 排序链表
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

https://leetcode-cn.com/problems/sort-list/
"""
from typing import Optional

from leetCode.utils.listNodeUtil import ListNode,init_nodes,visit_list


class Solution:
    # 1. 递归：归并排序，自顶向下
    def sortList0(self,head: Optional[ListNode]) -> Optional[ListNode]:
        # 又是包头不包尾
        def sort_dui(head: ListNode,tail: ListNode) -> ListNode:
            # 0. 递归得有个结束条件吧？
            if not head:
                return None
            # 0.1 分割到单个节点了
            if head.next == tail:
                # 因为最后要merge_sorted_list(left, right), 所以得head.next=None, 否则真是：剪不断，理还乱
                head.next = None
                return head

            # 1. 寻找中间节点进行分割
            slow = fast = head
            while fast != tail:
                slow,fast = slow.next,fast.next
                if fast != tail:
                    fast = fast.next
            # 中间点 = 中间靠右那个 奇数[-1,5,3,4,0] -> 4；偶数[4,2,1,3]->1
            # 因为得带上None [-1,5,3,4,0,None] [4,2,1,3,None]
            middle = slow

            # 2. 分治法排序左边、右边，再merge
            left = sort_dui(head,middle)
            right = sort_dui(middle,tail)
            return self.merge_sorted_list(left,right)

        return sort_dui(head,None)

    # 2. 迭代：归并排序，自底向上； 题解比官方题解更好懂
    # https://leetcode-cn.com/problems/sort-list/solution/sort-list-gui-bing-pai-xu-lian-biao-by-jyd/
    def sortList1(self,head: Optional[ListNode]) -> Optional[ListNode]:
        # if not head:
        #     return None

        # 获取链表长度
        length,node = 0,head
        while node:
            length += 1
            node = node.next

        # 新建一个空节点，
        dummyHead = ListNode(0,head)
        subLength = 1  # 从长度1，2，4，8开始迭代
        while subLength < length:
            prev,curr = dummyHead,dummyHead.next
            while curr:
                # 一轮迭代中，找出分割点：head1，head2
                head1 = curr
                # 往后挪动(subLength-1)步骤
                for i in range(1,subLength):
                    if curr.next:
                        curr = curr.next
                    else:
                        break
                head2 = curr.next
                curr.next = None  # 这一步非常关键，最后要merge

                curr = head2
                for i in range(1,subLength):
                    if curr and curr.next:
                        curr = curr.next
                    else:
                        break

                # 当前长度subLength内的下一轮遍历
                succ = None
                if curr:
                    succ = curr.next
                    curr.next = None

                merged = self.merge_sorted_list(head1,head2)
                prev.next = merged
                while prev.next:
                    prev = prev.next
                curr = succ

            subLength <<= 1

        return dummyHead.next

    def sortList(self,head: Optional[ListNode]) -> Optional[ListNode]:
        h1,length = head,0
        while h1:
            h1 = h1.next
            length += 1

        intv = 1
        new_head = ListNode(0)
        while intv < length:
            p = new_head

            while head:
                h1 = head

                # 1. 找到h2并且断开了h1的尾巴
                i = 1
                while head.next and i < intv:
                    # head, i = head.next, i + 1
                    head = head.next
                    i = i + 1
                h2 = head.next
                head.next = None

                # 2. 找到h2并且断开了h1的尾巴
                successor = None
                head = h2
                i = 1
                while head.next and i < intv:
                    head,i = head.next,i + 1
                successor = head.next
                head.next = None

                p.next = self.merge_sorted_list(h1,h2)

                head = successor

            intv *= 2
        return new_head.next

    # 3. by myself
    def sortList(self,head: Optional[ListNode]) -> Optional[ListNode]:
        # 0. 先遍历出链表长度
        h1,length = head,0
        while h1:
            length += 1
            h1 = h1.next

        new_head,intv = ListNode(0,head),1
        # 循环终止：当间隔达到了数组长度时候
        while intv < length:
            # print("intv", intv)
            p,head = new_head,new_head.next
            while head:
                h1 = head

                # 1. h1尾部断链 & 寻找h2
                h2 = self.find_next_and_disconnect(head,intv)

                # 2. h2尾部断链 & 寻找下一轮循环的successor
                if h2 is None:
                    successor = None
                else:
                    head = h2
                    successor = self.find_next_and_disconnect(head,intv)

                # 3. 连起来 & 准备下一轮
                p.next = self.merge_sorted_list(h1,h2)
                # 方便下一组合并，p挪到最后
                while p.next:
                    p = p.next
                head = successor

            intv <<= 1
        return new_head.next

    def find_next_and_disconnect(self,head,intv):
        i = 1
        while head.next and i < intv:
            head,i = head.next,i + 1
        next = head.next
        head.next = None
        return next

    # 第21题：https://leetcode-cn.com/problems/merge-two-sorted-lists/
    def merge_sorted_list(self,l1: ListNode,l2: ListNode):
        node = head = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                node.next,l1 = l1,l1.next
            else:
                node.next,l2 = l2,l2.next
            node = node.next
        node.next = l1 if l1 else l2
        return head.next


s = Solution()
head = init_nodes([4,3,2,6,5,7,1])
head = s.sortList(head)
print(visit_list(head) == [1,2,3,4,5,6,7])

head = init_nodes([2,1])
head = s.sortList(head)
print(visit_list(head) == [1,2])

head = init_nodes([4,2,1,3])
head = s.sortList(head)
print(visit_list(head) == [1,2,3,4])

head = init_nodes([-1,5,3,4,0])
head = s.sortList(head)
print(visit_list(head) == [-1,0,3,4,5])

head = init_nodes([])
head = s.sortList(head)
print(visit_list(head) == [])
