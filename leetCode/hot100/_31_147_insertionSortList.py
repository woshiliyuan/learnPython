# coding=utf-8
"""
147. 对链表进行插入排序
给定单个链表的头 head ，使用 插入排序 对链表进行排序，并返回 排序后链表的头 。

插入排序 算法的步骤:
1. 插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
2. 每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
3. 重复直到所有输入数据插入完为止。

下面是插入排序算法的一个图形示例。部分排序的列表(黑色)最初只包含列表中的第一个元素。每次迭代时，
从输入数据中删除一个元素(红色)，并就地插入已排序的列表中。


https://leetcode-cn.com/problems/insertion-sort-list/
"""

from leetCode.utils.listNodeUtil import ListNode, init_nodes, visit_list


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # 新建一个空节点，对于链表的有序插入、删除非常有用
        new_head = ListNode(0)

        # 1. 遍历旧链表，p1操作，head指向下一个头
        while head:
            p1 = head
            head = head.next

            # 2. 链表这东西都需要两个指针，除非头不用保存起来的；比如说访问链表
            p2 = new_head
            # 2.1 访问链表一般 while p: 因为这样可以判空 & 需要记录头节点p.value；
            # 但是插入操作例外，需要操作p.next, 因为需要操作p
            while p2.next:
                # 2.2 寻找到p2了，
                if p2.next.val > p1.val:
                    break
                p2 = p2.next

            # 3. 记录应该插在p2前面，同时不用特别处理新链表为空时情况(new_head初始化一个没用的节点这招太强了)
            p1.next = p2.next
            p2.next = p1

        return new_head.next


s = Solution()
head = init_nodes([4,2,1,3])
head = s.insertionSortList(head)
print(visit_list(head) == [1,2,3,4])

head = init_nodes([-1,5,3,4,0])
head = s.insertionSortList(head)
print(visit_list(head) == [-1,0,3,4,5])

head = init_nodes([])
head = s.insertionSortList(head)
print(visit_list(head) == [])

head = init_nodes([1])
head = s.insertionSortList(head)
print(visit_list(head) == [1])