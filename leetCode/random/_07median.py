# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
# 你可以假设 nums1 和 nums2 不会同时为空。
# 示例 1:
# nums1 = [1, 3]
# nums2 = [2]
#
# 则中位数是 2.0
# 示例 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# 则中位数是 (2 + 3)/2 = 2.5
#
# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self,nums1,nums2) -> float:
        # 1. 重组一个新的数组
        nums = []
        i = 0
        j = 0

        # 1.1 同时往右比较
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                nums.append(nums1[i])
                i = i + 1
            else:
                nums.append(nums2[j])
                j = j + 1

        # 1.2 看哪个数组比较完了
        if i == len(nums1):
            for index in range(j,len(nums2)):
                nums.append(nums2[index])
        if j == len(nums2):
            for index in range(i,len(nums1)):
                nums.append(nums1[index])

        # 2. 新数组求中位数
        # 偶数个数组，中位数有两个
        median = 0
        middle = int(len(nums) / 2)
        if len(nums) % 2 == 0:
            median = (nums[middle] + nums[middle - 1]) / 2
        # 奇数个数组，中位数只有一个
        else:
            median = nums[middle]
        return median


# 开始测试
solution = Solution()

nums1 = [1,2]
nums2 = [3,4]
result = solution.findMedianSortedArrays(nums1,nums2)
print(result)

nums1 = [1,3]
nums2 = [2]
result = solution.findMedianSortedArrays(nums1,nums2)
print(result)

nums1 = [1,3]
nums2 = []
result = solution.findMedianSortedArrays(nums1,nums2)
print(result)

nums1 = [3,5]
nums2 = [1,2]
result = solution.findMedianSortedArrays(nums1,nums2)
print(result)
