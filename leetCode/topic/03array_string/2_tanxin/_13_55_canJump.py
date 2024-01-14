# coding=utf-8
"""
55. 跳跃游戏
给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个下标。
https://leetcode-cn.com/problems/jump-game/
"""
from typing import List


class Solution:
    # 不遍历所有可能，只取当前值的, 即每次都跳跃最大长度
    def canJump0(self, nums: List[int]) -> bool:
        index, last_index = 0, len(nums) - 1
        while index < last_index:
            if nums[index] == 0:
                return False
            index += nums[index]
        return index == last_index

    # 错误示范：python range中的i是不变的
    def canJump1(self, nums: List[int]) -> bool:
        for i in range(0, len(nums) - 1):
            print("i0", i)
            i += nums[i]  # 这么修改根本动不了range中的i
            print("i1", i)
        print("last i", i)
        return i == len(nums) - 1

    # 递归会超时...
    def canJump2(self, nums: List[int]) -> bool:
        def visit_all(index):
            nonlocal flag, last_index
            if index > last_index or flag is True:
                return
            if index == last_index:
                flag = True
                return

            # 如果nums[index]==0, 那么这个for循环就不会继续了，即不会生产新的递归，本次函数只想自然也就结束了
            # for step in range(1, nums[index]+1):
            for step in range(nums[index], 0, -1):
                visit_all(index + step)

        flag, last_index = False, len(nums) - 1
        visit_all(0)
        return flag

    # 既然会超时，那就用来打印所有步骤吧
    def canJump3(self, nums: List[int]) -> bool:
        def visit_all(index, steps: List[int]):
            nonlocal flag, last_index

            # if index > last_index or flag is True: # 只打印一种解
            if index > last_index:  # 打印所有可能
                return
            if index == last_index:
                flag = True
                all_path.append(steps)
                return

            for step in range(nums[index], 0, -1):
                visit_all(index + step, steps + [index])

        flag, last_index, all_path = False, len(nums) - 1, []
        visit_all(0, [])
        print("all_path", all_path)
        return flag

    # 能跳跃到的最远位置
    def canJump4(self, nums: List[int]) -> bool:
        reach_max, last_index = 0, len(nums) - 1
        for i in range(last_index):
            # [0,2,3] [1,0,0,0,4,3] 首先每一步应该保证位置i能够到达
            if i > reach_max:
                return False
            reach_max = max(reach_max, i + nums[i])

            # 进行优化
            if reach_max >= last_index:
                return True
        return reach_max >= last_index

    # 官方代码：跳跃最远位置
    def canJump6(self, nums: List[int]) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True
        return False


solution = Solution()
print(solution.canJump([2, 3, 1, 1, 4]) is True)  # True
# print(solution.canJump([3, 2, 1, 0, 4]) is False)  # False
# print(solution.canJump([3, 2, 1, 0, 4, 3]) is False)  # False
# print(solution.canJump([1,0,4]) is False) # False
# print(solution.canJump([1,0]) is True) # True
# print(solution.canJump([2,0,1,0,4]) is False) # False
# print(solution.canJump([2]) is True) # True
# print(solution.canJump([3, 1, 0]) is True) # True
# print(solution.canJump([2, 0, 0]) is True) # True
# print(solution.canJump([0, 2, 3]) is False)  # False
