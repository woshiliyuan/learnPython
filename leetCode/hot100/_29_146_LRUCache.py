# coding=utf-8
"""
146. LRU 缓存
请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
实现 LRUCache 类：
LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。
如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。

https://leetcode-cn.com/problems/lru-cache/
"""
import collections


class LinkedNode:
    def __init__(self,key: int,val: int,pre=None,next=None):
        self.val = val
        self.key = key
        self.pre = pre
        self.next = next


class LRUCache(collections.OrderedDict):

    def __init__(self,capacity: int):
        # super().__init__()
        self.capacity = capacity

    def get(self,key: int) -> int:
        if key not in self:
            return -1
        # OrderedDict的get函数，不会像LinkedHashMap那样自动更新吗
        self.move_to_end(key)
        return self[key]

    def put(self,key: int,value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)


class LRUCache2:
    def __init__(self,capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.head = LinkedNode(0,0)
        self.tail = LinkedNode(0,0,self.head)
        self.head.next = self.tail

    def get(self,key: int) -> int:
        if key not in self.dict:
            return -1

        # 节点存在，更新节点到尾部
        node = self.dict[key]
        self.move_node_to_tail(node)
        return node.val

    def move_node_to_tail(self,node: LinkedNode):
        if node.next != self.tail:
            # 1. 先断开本身
            self.del_from_link(node)
            # 2. 尾部插入
            self.add_node_in_tail(node)

    # 1. 删除某个节点
    def del_from_link(self,node: LinkedNode):
        node.pre.next = node.next
        node.next.pre = node.pre

    # 2. 尾部插入
    def add_node_in_tail(self,node: LinkedNode):
        node.next = self.tail
        self.tail.pre.next = node

        node.pre = self.tail.pre
        self.tail.pre = node

    def put(self,key: int,value: int) -> None:
        # 1. key值已存在，修改值 & 更新到尾部
        if key in self.dict:
            # 不用考虑容量，必然小于capacity
            node = self.dict[key]
            node.val = value
            self.move_node_to_tail(node)
        else:
            # 2. key不存在，新建；dict & 双链表都放入
            node = LinkedNode(key,value)
            self.dict[key] = node
            self.add_node_in_tail(node)

            # 2.2 满了，删掉头部未使用的节点
            if len(self.dict) > self.capacity:
                first_node = self.head.next
                self.del_from_link(first_node)
                del self.dict[first_node.key]
        # print(self.dict)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

lRUCache = LRUCache(2)
lRUCache.put(1,1)  # 缓存是{1 = 1}
lRUCache.put(2,2)  # 缓存是{1 = 1, 2 = 2}
print(lRUCache.get(1) == 1)  # 返回 1
lRUCache.put(3,3)  # 该操作会使得关键字2作废，缓存是{1 = 1, 3 = 3}
print(lRUCache.get(2) == -1)  # 返回 - 1(未找到)
lRUCache.put(4,4)  # 该操作会使得关键字1作废，缓存是{4 = 4, 3 = 3}
print(lRUCache.get(1) == -1)  # 返回 - 1(未找到)
print(lRUCache.get(3) == 3)  # 返回3
print(lRUCache.get(4) == 4)  # 返回4
