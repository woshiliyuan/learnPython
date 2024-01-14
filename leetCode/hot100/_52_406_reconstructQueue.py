# coding=utf-8
"""
406. 根据身高重建队列
假设有打乱顺序的一群人站成一个队列，数组 people 表示队列中一些人的属性（不一定按顺序）。每个 people[i] = [hi, ki] 表示第 i 个人的身高为 hi ，前面 正好 有 ki 个身高大于或等于 hi 的人。
请你重新构造并返回输入数组 people 所表示的队列。返回的队列应该格式化为数组 queue ，其中 queue[j] = [hj, kj] 是队列中第 j 个人的属性（queue[0] 是排在队列前面的人）。


https://leetcode.cn/problems/queue-reconstruction-by-height/
"""
from typing import List


class Solution:
    # 1. 不排序，直接插入
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """
        如果不排，样例：[[7, 0], [7, 1], [4, 2], [6, 1]] --> [[7, 0], [6, 1], [4, 2], [7, 1]]
        [3,2], [7, 0] ,[7, 1], [6,3]333,

        [7, 0] , [7, 1], [4, 2];    [6, 1]
              [6, 1]
         [7, 0] , [6, 1], [7, 1], [4, 2],
        当遍历到[4, 2], 不能确定最后的正常位置，必定为变成：[7, 0], [7, 1], [4, 2]; 放到[7, 1]后面了，
        最后 [[7, 0], [6, 1], [7, 1], [4, 2]]
        """

        # 0. 全部逆序 [[7, 1], [7, 0], [4, 2], [4, 1]] -- > [[7, 0], [4, 1], [4, 2], [7, 1]]
        # 结果却会成为：[[7, 0], [4, 1], [7, 1], [4, 2]]： 当遍历到[4, 2]，-> [[7, 0], [7, 1], [4, 2]]
        # h逆序，k正序：[[7, 0], [7, 1], [4, 1], [4, 2]], 才能得到最后结果：
        # people.sort(reverse=True)
        people.sort(key=lambda x: (-x[0], x[1]))
        # print(people)

        res = []
        for p in people:
            h, k = p
            # 从res中找到k个身高 >= k 的位置
            i = 0
            while i < len(res):
                if res[i][0] >= h:
                    if k == 0:
                        break
                    else:
                        k -= 1
                i += 1

            res.insert(i, p)
        return res

    # 2. 优化上面一版本，不用每次去重新查找位置
    # https://leetcode.cn/problems/queue-reconstruction-by-height/solution/xian-pai-xu-zai-cha-dui-dong-hua-yan-shi-suan-fa-g/
    def reconstructQueue2(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        res = []
        for p in people:
            res.insert(p[1], p)

        # 官方的这是什么python语法？
        # for p in people:
        #     res[p[1]:p[1]] = [p]

        return res

    # 3. 原地修改数组  [[7, 0], [7, 1], [4, 1], [4, 2]] -> [[7, 0], [4, 1], [4, 2], [7, 1]]
    def reconstructQueue3(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        i = 0
        while i < len(people):
            if i > people[i][1]:
                # 前移动第i个位置到people[i][1]
                people.insert(people[i][1], people[i])
                people.pop(i + 1)
            i += 1
        return people


s = Solution()
print(s.reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]) == [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]])
print(s.reconstructQueue([[7, 0], [4, 1], [7, 1]]) == [[7, 0], [4, 1], [7, 1]])
print(s.reconstructQueue([[7, 0], [4, 1], [7, 1]]) == [[7, 0], [4, 1], [7, 1]])
print(s.reconstructQueue([[7, 0], [7, 1], [4, 2], [6, 1]]) == [[7, 0], [6, 1], [4, 2], [7, 1]])
print(s.reconstructQueue([[7, 0], [7, 1], [4, 2], [4, 1]]) == [[7, 0], [4, 1], [4, 2], [7, 1]])
print(s.reconstructQueue([[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]) == [[4, 0], [5, 0], [2, 2], [3, 2], [1, 4], [6, 0]])
