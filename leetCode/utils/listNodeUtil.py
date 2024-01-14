# coding=utf-8
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def init_nodes(values):
    # 澜澜老师教的技能，链表头新增一个空节点，方便链表删除，新增等操作
    pre = p = ListNode(0)
    for item in values:
        p.next = ListNode(item)
        p = p.next
    return pre.next


def init_cycle_nodes(values, pos=-1):
    cycle_node = None
    pre = p = ListNode(0, None)
    for i in range(len(values)):
        temp = ListNode(values[i])
        p.next = temp
        p = p.next
        if i == pos:
            cycle_node = temp
    p.next = cycle_node
    return pre.next


def init_nodes0(values):
    head = p = None
    for item in values:
        # 头节点判空放里面
        if head is None:
            head = p = ListNode(item)
        else:
            p.next = ListNode(item)
            p = p.next
    return head


def visit_list(head: ListNode):
    answer = []
    while head:
        answer.append(head.val)
        head = head.next
    # print(answer)
    return answer
