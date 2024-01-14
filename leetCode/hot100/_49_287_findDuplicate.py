# coding=utf-8
"""
287. 寻找重复数
给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。
假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。
你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。

https://leetcode-cn.com/problems/find-the-duplicate-number/
"""
from typing import List


class Solution:
    # 1. set，空间复杂度o(n)
    def findDuplicate1(self,nums: List[int]) -> int:
        nums_set = set()
        for n in nums:
            if n in nums_set:
                return n
            else:
                nums_set.add(n)

    # 2. 新建一个数组 visited = [False] * (n + 1)，空间复杂度为o(n)
    def findDuplicate2(self,nums: List[int]) -> int:
        pass

    # 3. 空间复杂度为o(1), 修改原数组
    def findDuplicate3(self,nums: List[int]) -> int:
        length = len(nums)
        for num in nums:
            i = (num - 1) % length
            if nums[i] > length:
                return i + 1
            else:
                nums[i] += length

    # --------------   以上都不符合题目要求  -----------------
    # 4. 暴力破解：每个数依次往右去遍历，是否存在相等数字

    # 4. 第一个cnt > i的数字: o(n**2)  超出时间限制
    def findDuplicate4(self,nums: List[int]) -> int:
        length = len(nums)
        for i in range(1,length):
            cnt = 0
            for num in nums:
                if num <= i:
                    cnt += 1
            if cnt > i:
                return i

    # 5. 二分查找 第一个cnt > i的数字
    def findDuplicate5(self,nums: List[int]) -> int:
        length = len(nums)
        l,r = 0,length - 1
        ans = -1
        while l <= r:
            # 1. 遍历数组nums，找到 num <= mid的个数
            mid = (l + r) // 2
            cnt = 0
            for i in range(length):
                if nums[i] <= mid:
                    cnt += 1

            if cnt <= mid:
                l = mid + 1
            else:
                r = mid - 1
                ans = mid
        print(ans)
        return ans

    # 6. 神奇的快慢指针
    # https://leetcode-cn.com/problems/find-the-duplicate-number/solution/287xun-zhao-zhong-fu-shu-by-kirsche/
    def findDuplicate(self,nums: List[int]) -> int:
        slow,fast = 0,0

        # python的do while 替代写法
        # while True:
        #     # 数组不会越界, 1 <= nums[i] <= n; len(nums) == n + 1
        #     slow, fast = nums[slow], nums[nums[fast]]
        #     if slow == fast:
        #         break

        # 1 <= nums[i] <= n, slow不可能再次为0
        while slow != fast or slow == 0:
            slow,fast = nums[slow],nums[nums[fast]]

        slow = 0
        while slow != fast:
            slow,fast = nums[slow],nums[fast]

        return slow


s = Solution()
print(s.findDuplicate([1,3,4,2,2]) == 2)
print(s.findDuplicate([2,2,4,1,3]) == 2)
print(s.findDuplicate([3,1,3,4,2]) == 3)
print(s.findDuplicate([1,1]) == 1)
print(s.findDuplicate([2,2,2]) == 2)
