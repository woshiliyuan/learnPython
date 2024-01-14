# coding=utf-8
"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。

示例 2：
输入：height = [4,2,0,3,2,5]
输出：9

链接：https://leetcode-cn.com/problems/trapping-rain-water
"""
from typing import List


class Solution:
    def trap0(self,height: List[int]) -> int:
        """
        还有问题，如果最右边没有比当前更高的了 4 2 3
        o(n)
        """
        area = 0
        i = 0
        while i < len(height):
            for j in range(i + 1,len(height)):
                if height[j] >= height[i]:
                    temp_area = (j - i) * height[i] - sum(height[i:j])
                    area += temp_area
                    i = j - 1
                    break
            i += 1
        return area

    def trap0_1(self,height: List[int]) -> int:
        """
            对上一个方法修正了有边界的判断，待完善...
        """
        area = 0
        i = 0
        while i < len(height):
            for j in range(i + 1,len(height)):
                if i == len(height) - 1 or (height[j] > height[j - 1] and height[j] < height[j + 1]):
                    temp_area = (j - i - 1) * min(height[i],height[j]) - sum(height[i + 1:j])
                    area += temp_area
                    i = j
                    break
            i += 1
        return area

    def trap0_2(self,height: List[int]) -> int:
        """
        1. 暴力破解法
        """
        area = 0
        for i in range(0,len(height)):
            max_left = max(height[:i + 1])
            max_right = max(height[i:])
            area += min(max_left,max_right) - height[i]
        return area

    def trap(self,height: List[int]) -> int:
        """
        动态规划解法
        """
        length = len(height)
        max_left,max_right = [0] * length,[0] * length
        max_left[0],max_right[-1] = height[0],height[-1]

        for i in range(1,length):
            # 1. 往左看，最大左边界
            max_left[i] = max(height[i],max_left[i - 1])

            # 2. 往右看，最大右边界
            j = length - 1 - i
            max_right[j] = max(height[j],max_right[j + 1])

        # 这两种方式有差别的吗？ 这个是 o(2n)
        # for i in range(1, length):
        #     max_left[i] = max(height[i], max_left[i-1])
        # for i in range(length-2, -1, -1):
        #     max_right[i] = max(height[i], max_right[i+1])

        # print("max_left", max_left)
        # print("max_right", max_right)

        # 3. 开始计算区域面积
        area = 0
        for i in range(length):
            area += min(max_left[i],max_right[i]) - height[i]
        return area

    def trap3(self,height: List[int]) -> int:
        """
        双指针
        """
        left,right = 0,len(height) - 1
        maxLeft,maxRight = 0,0
        area = 0
        while left < right:
            if height[left] < height[right]:
                # 有没有这么一种可能：[..., 6, 2, 3, ...] 比较2和3, maxLeft=6, 但是不能用6-2，实际应该是 3-2
                # 不可能的，maxLeft < height[right]的
                maxLeft = max(maxLeft,height[left])
                area += maxLeft - height[left]
                left += 1
            else:
                # 同理，这里的maxRight<height[left]的
                maxRight = max(maxRight,height[right])
                area += maxRight - height[right]
                right -= 1
        return area

    def trap4(self,height: List[int]) -> int:
        """
        4. 单调递减栈, 待续。。。
        """
        pass


solution = Solution()
print(solution.trap([4,2,3]) == 1)  # 1
print(solution.trap([4,2,0,3,2,5]) == 9)  # 9
print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6)  # 6
