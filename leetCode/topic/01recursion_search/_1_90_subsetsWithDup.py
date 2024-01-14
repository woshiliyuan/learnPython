# coding=utf-8
"""
90. 子集 II
给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列

https://leetcode-cn.com/problems/subsets-ii/
"""

from typing import List

from leetCode.utils.util import equals_array


class Solution:
    # 最佳方案？
    def subsetsWithDup0(self,nums: List[int]) -> List[List[int]]:
        def get_sub(index,temp_list):
            answer.append(temp_list)
            for i in range(index,len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                get_sub(i + 1,temp_list + [nums[i]])

        nums.sort()
        answer = []
        get_sub(0,[])
        return answer

    # 迭代器做法，貌似不可解
    def subsetsWithDup1(self,nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = [[]]
        for i in range(len(nums)):
            if i > 1 and nums[i] == nums[i - 1]:
                # 这样就比较难算了，需要判断第一次出现重复数字时，前面已经有几个了， 比如有n个数了
                # 那再次相同数，就只能拼接最后几个了
                # temp = [answer[-2:] + [nums[i]]]
                pass
            else:
                temp = [item + [nums[i]] for item in answer]
            answer += temp
        return answer

    def subsetsWithDup(self,nums: List[int]) -> List[List[int]]:
        def get_sub(index,temp_list):
            if index == len(nums):
                answer.append(temp_list)
                return

            if index == 0 or nums[index] != nums[index - 1] or visited[index - 1] == 1:
                visited[index] = 1
                get_sub(index + 1,temp_list + [nums[index]])
            visited[index] = 0
            get_sub(index + 1,temp_list)

        answer = []
        nums.sort()
        visited = [0] * len(nums)
        get_sub(0,[])
        return answer


solution = Solution()
# print(solution.subsetsWithDup([1,2,3]))  # [[],[1],[1,2],[1,2,2],[2],[2,2]]
# print(solution.subsetsWithDup([0,1,1]))  # [[],[1],[1,2],[1,2,2],[2],[2,2]]
# print(solution.subsetsWithDup([1,2,2]))  # [[],[1],[1,2],[1,2,2],[2],[2,2]]
# print(solution.subsetsWithDup0([1,2,2]))  # [[],[1],[1,2],[1,2,2],[2],[2,2]]
equals_array(solution.subsetsWithDup([1,2,2,2]),[[],[1],[1,2],[1,2,2],[1,2,2,2],[2],[2,2],[2,2,2]])
equals_array(solution.subsetsWithDup([1,2,2,3]),
             [[],[1],[1,2],[1,2,2],[1,2,2,3],[1,2,3],[1,3],[2],[2,2],[2,2,3],[2,3],[3]])
equals_array(solution.subsetsWithDup([0]),[[],[0]])
equals_array(solution.subsetsWithDup([4,4,4,1,4]),
             [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]])
equals_array(solution.subsetsWithDup([1,2,2,2]),[[],[1],[1,2],[1,2,2],[1,2,2,2],[2],[2,2],[2,2,2]])
