# coding=utf-8
"""
不使用任何内建的哈希表库设计一个哈希映射（HashMap）。
实现 MyHashMap 类：
MyHashMap() 用空映射初始化对象
void put(int key, int value) 向 HashMap 插入一个键值对 (key, value) 。如果 key 已经存在于映射中，则更新其对应的值 value 。
int get(int key) 返回特定的 key 所映射的 value ；如果映射中不包含 key 的映射，返回 -1 。
void remove(key) 如果映射中存在 key 的映射，则移除 key 和它所对应的 value 。

示例：
输入：
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
输出：
[null, null, null, 1, -1, null, 1, null, -1]

解释：
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // myHashMap 现在为 [[1,1]]
myHashMap.put(2, 2); // myHashMap 现在为 [[1,1], [2,2]]
myHashMap.get(1);    // 返回 1 ，myHashMap 现在为 [[1,1], [2,2]]
myHashMap.get(3);    // 返回 -1（未找到），myHashMap 现在为 [[1,1], [2,2]]
myHashMap.put(2, 1); // myHashMap 现在为 [[1,1], [2,1]]（更新已有的值）
myHashMap.get(2);    // 返回 1 ，myHashMap 现在为 [[1,1], [2,1]]
myHashMap.remove(2); // 删除键为 2 的数据，myHashMap 现在为 [[1,1]]
myHashMap.get(2);    // 返回 -1（未找到），myHashMap 现在为 [[1,1]]

提示：
0 <= key, value <= 10^6
最多调用 104 次 put、get 和 remove 方法

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/design-hashmap
"""


class MyHashMap1:
    """
    方式一：简单粗暴，就用数组吧，而且不考虑扩容
    """
    def __init__(self):
        self.map = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        return self.map[key]

    def remove(self, key: int) -> None:
        self.map[key] = -1


class MyHashMap:
    """
    方式二：采用拉链法，哈希进行散列，
    解决哈希冲突的方式：数组(本例子)，链表
    不太理解这段话，但是确实奏效了：248ms -> 180ms
    分桶数一般取质数，这是因为经验上来说，质数个的分桶能让数据更加分散到各个桶中。
    下面的代码中可以 self.barrel_size = 1009，是因为 1009 是大于 1000 的第一个质数。
    """
    def __init__(self):
        # 不考虑自动扩容，默认大小
        self.barrel_size = 1000
        self.map = [[] for i in range(self.barrel_size)]

    def put(self, key: int, value: int) -> None:
        temp_list = self.get_hash_list(key)
        # 可能要解决hash冲突; temp_list: [[1, 2], [11, 3], [21, 22] ... ]
        for temp in temp_list:
            if temp[0] == key:
                temp[1] = value
                return
        # 能到这儿，说明是新的key值
        temp_list.append([key, value])

    def get(self, key: int) -> int:
        temp_list = self.get_hash_list(key)
        for temp in temp_list:
            if temp[0] == key:
                return temp[1]
        return -1

    def remove(self, key: int) -> None:
        temp_list = self.get_hash_list(key)
        for temp in temp_list:
            if temp[0] == key:
                temp_list.remove(temp)
                return

    def get_hash_list(self, key):
        hash_key = key % self.barrel_size
        return self.map[hash_key]


obj = MyHashMap()
obj.put(1, 1)
param_2 = obj.get(1)
obj.put(2, 2)
param_2 = obj.get(2)
# print(obj.map)
print("1 ", param_2)
obj.put(1, 2)
param_2 = obj.get(1)
print("2 ", param_2)

obj.remove(1)
# print(obj.map)
param_2 = obj.get(1)
print("3 ", param_2)