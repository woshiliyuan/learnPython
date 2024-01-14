# coding=utf-8
"""
581. 最短无序连续子数组
给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
请你找出符合题意的 最短 子数组，并输出它的长度。

https://leetcode.cn/problems/shortest-unsorted-continuous-subarray/
"""

from typing import List


class Solution:
    # 1. 自己想到的，先排序，挨个比较，o(nlogn) + 2n
    def findUnsortedSubarray1(self,nums: List[int]) -> int:
        origin = nums.copy()
        nums.sort()
        length = len(nums)
        i,j = 0,length - 1
        while i <= j and origin[i] == nums[i]:
            i += 1
        while i <= j and origin[j] == nums[j]:
            j -= 1
        return j - i + 1

    # 2. 参考网友思路：
    # https://leetcode.cn/problems/shortest-unsorted-continuous-subarray/solution/si-lu-qing-xi-ming-liao-kan-bu-dong-bu-cun-zai-de-/
    def findUnsortedSubarray(self,nums: List[int]) -> int:
        begin,end = 0,-1
        # 这么赋值，为什么不可以呢？
        # min, max = nums[0], nums[0]
        min,max = nums[-1],nums[0]
        length = len(nums)

        for i in range(length):
            # 从左到右维持最大值，寻找右边界end
            if nums[i] < max:
                end = i
            else:
                max = nums[i]

            # 从左到右寻找左边界? 为什么是错误❌
            # begin不单单要大于min，还要尽量出现在最左边；所以是从右到左扫描
            # if nums[i] > min:
            #     begin = i
            # else:
            #     min = nums[i]

            # 从右到左维持最小值，寻找左边界begin
            if nums[length - 1 - i] > min:
                begin = length - 1 - i
            else:
                min = nums[length - 1 - i]
        print("begin-end",begin,end)
        print("min-max",min,max)
        return end - begin + 1

    # 3. 有误，待续。。。
    def findUnsortedSubarray3(self,nums: List[int]) -> int:
        min_num,max_num = min(nums),max(nums)
        length = len(nums)
        begin,end = 0,-1

        # 1. 从左到右寻找end，最后一个<max的数
        for i in range(length):
            if nums[i] < max_num:
                end = i

        # 2. 从右往左寻找begin，最后一个大于min的数
        for i in range(length - 1,-1,-1):
            if nums[i] > min_num:
                begin = i

        print(begin,end)
        return end - begin + 1


s = Solution()
# print(s.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]) == 5)
print(s.findUnsortedSubarray([1,2,3,4]) == 0)
# print(s.findUnsortedSubarray([1]) == 0)
# print(s.findUnsortedSubarray([2,1]) == 2)
# print(s.findUnsortedSubarray([3, 2, 1]) == 3)
# print(s.findUnsortedSubarray([1,3,2,4,5]) == 2)
# print(s.findUnsortedSubarray([1,3,2,2,2]) == 4)
