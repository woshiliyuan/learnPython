"""
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点(i,ai) 。在坐标内画 n 条垂直线，
垂直线 i的两个端点分别为(i,ai) 和 (i, 0) 。找出其中的两条线，使得它们与x轴共同构成的容器
可以容纳最多的水。

输入：[1,8,6,2,5,4,8,3,7]
输出：49
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为49。

示例 2：
输入：height = [1,1]
输出：1

示例 3：
输入：height = [4,3,2,1,4]
输出：16

示例 4：
输入：height = [1,2,1]
输出：2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/container-with-most-water
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxArea = 0
        while left < right:
            tempArea = (right - left) * min(height[left], height[right])
            maxArea = max(maxArea, tempArea)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea


solution = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(solution.maxArea(height))

