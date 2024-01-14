# coding=utf-8
"""
300. 最长递增子序列
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。
例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

https://leetcode-cn.com/problems/longest-increasing-subsequence/
"""
from typing import List


class Solution:
    # 1. 动态规划
    def lengthOfLIS0(self,nums: List[int]) -> int:
        length = len(nums)
        # max_end[5] = 3：以nums[5]结尾构成最长递增序列长度为3
        max_end,max_size = [1] * length,1
        for i in range(length):
            for j in range(i):
                if nums[i] > nums[j]:
                    max_end[i] = max(max_end[j] + 1,max_end[i])
            max_size = max(max_size,max_end[i])
        return max_size

    # 这种暴力破解是不对的，算不到递增
    def lengthOfLIS1(self,nums: List[int]) -> int:
        max_size,length = 1,len(nums)
        for i in range(length):
            size = 1
            for j in range(i + 1,length):
                if nums[j] > nums[i]:
                    size += 1
            print(nums[i],size)
            max_size = max(size,max_size)
        print("max_size",max_size)
        return max_size

    # 3. 贪心 + 二分查找
    # 并不理解：https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-by-leetcode-soluti/
    def lengthOfLIS(self,nums: List[int]) -> int:
        d = []
        for n in nums:
            if not d or n > d[-1]:
                d.append(n)
            else:
                # 这个二分查找有点变幻：找到第一个大于n的数
                l,r = 0,len(d) - 1
                loc = r
                while l <= r:
                    mid = (l + r) // 2
                    if d[mid] == n:
                        loc = mid
                        break
                    if d[mid] > n:
                        loc = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                d[loc] = n
        return len(d)


s = Solution()
print(s.lengthOfLIS([0,8,4,12,2]) == 3)
print(s.lengthOfLIS([10,9,2,5,3,7,101,18]) == 4)
print(s.lengthOfLIS([0,1,0,3,2,3]) == 4)
print(s.lengthOfLIS([0,1,-1,3,2,3]) == 4)
print(s.lengthOfLIS([7,7,7,7,7,7,7]) == 1)
