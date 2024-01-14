# https://leetcode-cn.com/problems/search-insert-position/
# Question: 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 你可以假设数组中无重复元素。

# 示例 1:
# 输入: [1,3,5,6], 5
# 输出: 2

# 示例2:
# 输入: [1,3,5,6], 2
# 输出: 1

# 示例 3:
# 输入: [1,3,5,6], 7
# 输出: 4

# 示例 4:
# 输入: [1,3,5,6], 0
# 输出: 0


class Solution:
    def searchInsert0(self,nums: [int],target: int) -> int:
        for index in range(len(nums)):
            if nums[index] >= target:
                return index
        return len(nums)

    def searchInsert(self,nums: [int],target: int) -> int:
        i,j = 0,len(nums)
        while i < j:
            p = (i + j) // 2
            if nums[p] == target:
                return p
            elif nums[p] < target:
                i = p + 1
            else:
                j = p
        return i


solution = Solution()

# print(solution.searchInsert([1,3,5,6], 5) == 2)
print(solution.searchInsert([1,3,5,6,7,8,9,10],7) == 4)

# print(solution.searchInsert([1,3,5,6], 2) == 1)
#
# print(solution.searchInsert([1,3,5,6], 7) == 4)
#
# print(solution.searchInsert([1,3,5,6], 0) == 0)
