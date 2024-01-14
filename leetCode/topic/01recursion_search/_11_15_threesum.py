# coding=utf-8
"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。

示例 1：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]

示例 2：
输入：nums = []
输出：[]

示例 3：
输入：nums = [0]
输出：[]

链接：https://leetcode-cn.com/problems/3sum
"""
from typing import List


class Solution:
    # 1. 暴力破解
    def threeSum0(self, nums: List[int]):
        result = []
        length = len(nums)
        exit_set = set()
        for i in range(length):
            for j in range(i + 1, length):
                for k in range(j + 1, length):
                    if nums[i] + nums[j] + nums[k] == 0:
                        # result.append([nums[i], nums[j], nums[k]])
                        list = [nums[i], nums[j], nums[k]]
                        list.sort()
                        if str(list) not in exit_set:
                            exit_set.add(str(list))
                            result.append(list)
        return result

    def threeSum1(self, nums: List[int]):
        """
        1. 解决重复: sort; nums[i] == nums[i-1]: continue
        2. 第二三遍转为双指针问题，一遍解决
        """
        result = []
        nums.sort()
        length = len(nums)
        for first in range(length):
            if first > 0 and nums[first] == nums[first - 1]:
                continue

            second, third = first + 1, length - 1
            while second < third:
                # [-1, -1, -1, 0, 0, 1, 2...] 这种，nums[second]=nums[first]
                if second > first + 1 and nums[second] == nums[second - 1]:
                    second += 1
                    continue
                sum = nums[first] + nums[second] + nums[third]
                if sum < 0:
                    second += 1
                elif sum > 0:
                    third -= 1
                else:
                    result.append([nums[first], nums[second], nums[third]])
                    second += 1
                    third -= 1
        return result

    # 简单递归，简单减枝
    def threeSum2(self, nums: List[int]):
        def get_result(rest, index, temp_list: List):
            # 1. 递归终止条件
            if rest < 0:
                return
            if rest == 0 and len(temp_list) == 3:
                result.append(temp_list)
                return

            # 2. 遍历所有可能
            for i in range(index, len(nums)):
                # 跳过重复值
                if i > index and nums[i] == nums[i - 1]:
                    continue
                get_result(rest - nums[i], i + 1, temp_list + [nums[i]])

        nums.sort()
        result = []
        get_result(0, 0, [])
        return result

    # 继续剪枝
    def threeSum(self, nums: List[int]):
        def get_result(rest, index, temp_list: List):
            # 剪循环节点
            for i in range(index, len(nums) - size + 1 + len(temp_list)):
                # 剪兄弟节点
                if rest < 0 or len(temp_list) >= size:
                    return
                if rest == nums[i] and len(temp_list) == size - 1:
                    result.append(temp_list + [nums[i]])
                    return

                # 跳过重复值
                if i > index and nums[i] == nums[i - 1]:
                    continue

                get_result(rest - nums[i], i + 1, temp_list + [nums[i]])

        nums.sort()
        result, target, size = [], 0, 3
        get_result(target, 0, [])
        return result


solution = Solution()
print(solution.threeSum([-1, 0, 1, 2, -1, -4]))  # [[-1, -1, 2], [-1, 0, 1]]
print(solution.threeSum([-1, -1, 2]))  # [[-1, -1, 2]]
print(solution.threeSum([]))  # []
print(solution.threeSum([0]))  # []
print(solution.threeSum([-2, 0, 0, 2, 2]))  # [[-2, 0, 2]]
print(solution.threeSum([0, 0, 0]))  # [[0, 0, 0]]
