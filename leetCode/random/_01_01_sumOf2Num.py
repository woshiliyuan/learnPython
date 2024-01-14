"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

https://leetcode-cn.com/problems/two-sum/comments/
"""


class Solution:
    def twoSum(self,nums,target):
        for i in range(len(nums) - 1):
            for j in range(i + 1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return None

    #     别人优秀答案， o(n)复杂度，利用hashmap建立 num->index的快速索引
    def twoSum2(self,nums,target):
        hashmap = {}
        for index,num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num],index]
            hashmap[num] = index
        return None

    def twoSum3(self,nums,target):
        """
        这个题目对于双指针做不了，返回的是index，如果是返回数值本身那就可以 o(n*logn) + o(n)
        """
        nums.sort()  # index会变乱的
        left,right = 0,len(nums) - 1
        while left < right:
            sum = nums[left] + nums[right]
            if sum == target:
                return [left,right]
            elif sum < target:
                left += 1
            else:
                right -= 1
        return None


# 测试过程
solution = Solution()
print(solution.twoSum3([2,7,11,15],9))  # [0, 1]
print(solution.twoSum3([2,7,11,15],17))  # [0, 3]
print(solution.twoSum3([2,7,11,15],26))  # [2, 3]
print(solution.twoSum3([3,2,4],6))  # [1, 2]
