# coding=utf-8
"""
347. 前 K 个高频元素
给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。

https://leetcode-cn.com/problems/top-k-frequent-elements/
"""
import collections
from typing import List


class Solution:
    # 1. 利用字典api，sorted(dict.item(), key=lambda)
    def topKFrequent1(self,nums: List[int],k: int) -> List[int]:
        # 1. map先记录个数
        num_dict = collections.defaultdict(int)
        for n in nums:
            num_dict[n] += 1

        # 2. 字典按照个数倒序排序
        sorted_dict = sorted(num_dict.items(),key=lambda x: x[1],reverse=True)

        # 3. 记录前k的结果
        answer = []
        for i in range(k):
            answer.append(sorted_dict[i][0])
        print(answer)
        return answer

    # 2. 不调用sorted全排序，用快排取前k大
    def topKFrequent(self,nums: List[int],k: int) -> List[int]:
        def partition(left,right):
            # lucky = random.randint(left, right)
            # nums[left], nums[lucky] = nums[lucky], nums[left]

            key = item_list[left]
            while left < right:
                while left < right and item_list[right][1] < key[1]:
                    right -= 1
                item_list[left] = item_list[right]

                while left < right and item_list[left][1] >= key[1]:
                    left += 1
                item_list[right] = item_list[left]

            item_list[left] = key
            return left

        def quick_sort(left,right):
            if left < right:
                part = partition(left,right)
                if part + 1 > k:
                    quick_sort(left,part - 1)
                elif part + 1 < k:
                    quick_sort(part + 1,right)

        # 1. map先记录个数
        num_dict = collections.defaultdict(int)
        for n in nums:
            num_dict[n] += 1
        # 2. 转为items list
        item_list = list(num_dict.items())

        # 3. 排序部分
        quick_sort(0,len(item_list) - 1)

        # 4. 收集结果
        answer = []
        for i in range(k):
            answer.append(item_list[i][0])

        # print(answer)
        return answer


s = Solution()
# print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2])
# print(s.topKFrequent([1, 2, 2, 2, 3,3], 2) == [2, 3])
# print(s.topKFrequent([1], 1) == [1])
# print(s.topKFrequent([1, 2], 2) == [1, 2])
print(s.topKFrequent([4,1,-1,2,-1,2,3],2) == [-1,2])
