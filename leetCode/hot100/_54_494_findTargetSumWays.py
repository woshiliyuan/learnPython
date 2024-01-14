# coding=utf-8
"""
494
"""
from typing import List


class Solution:
    # 1. 暴力破解：模仿子集解法 - 回溯
    def findTargetSumWays1(self,nums: List[int],target: int) -> int:
        def dfs(i):
            nonlocal temp_sum,count
            if i == len(nums):
                # 错误示范
                # if temp_sum == target:
                #     print(record)
                #     count += 1

                aa = 0
                for j in range(len(nums)):
                    aa += nums[j] * record[j]
                if aa == target:
                    print(record,temp_sum)
                    count += 1
                return

            record[i] = 1
            temp_sum += nums[i]
            dfs(i + 1)

            record[i] = -1
            temp_sum -= 2 * nums[i]
            dfs(i + 1)

        temp_sum,count = 0,0
        record = [1] * len(nums)
        dfs(0)
        print(count)
        return count

    # 1. 暴力破解，官方的递归
    def findTargetSumWays(self,nums: List[int],target: int) -> int:
        def dfs(i,temp_sum):
            nonlocal count
            if i == len(nums):
                if temp_sum == target:
                    count += 1
                return
            dfs(i + 1,temp_sum + nums[i])
            dfs(i + 1,temp_sum - nums[i])

        count = 0
        dfs(0,0)
        return count

    # 2. 暴力破解，模仿子集解法 - 迭代
    def findTargetSumWays2(self,nums: List[int],target: int) -> int:
        size,count = len(nums),0
        for mask in range(1 << size):
            temp_sum = 0
            for i in range(size):
                p = 1 << i
                if p & mask:
                    temp_sum += nums[i]
                else:
                    temp_sum -= nums[i]
            if temp_sum == target:
                count += 1
        return count

    # 3. 队列打印出所有和的可能性；不需要每次重新求和
    def findTargetSumWays3(self,nums: List[int],target: int) -> int:
        queue = [0]
        for n in nums:
            for _ in range(len(queue)):
                k = queue.pop(0)
                queue.append(k + n)
                queue.append(k - n)
        count = 0
        for n in queue:
            if n == target: count += 1
        return count

    # 4. 绝对可以用动态规划的, 网友非常好理解的解法
    # https://leetcode.cn/problems/target-sum/solution/dong-tai-gui-hua-si-kao-quan-guo-cheng-by-keepal/
    def findTargetSumWays4(self,nums: List[int],target: int) -> int:
        num_sum = sum(nums)
        if abs(target) > num_sum: return 0

        size,t = len(nums),num_sum * 2 + 1
        # 初始化dp[size+1][t]
        dp = [[0] * t for _ in range(size + 1)]
        dp[0][num_sum] = 1

        for i in range(1,size + 1):
            for j in range(t):
                # 理解一：不太理解，当越界时赋值l,r为0，是因为dp[i-1][0]始终为0吗？
                # l = j - nums[i - 1] if (j - nums[i - 1]) > 0 else 0
                # r = j + nums[i - 1] if (j + nums[i - 1]) < t else 0
                # dp[i][j] = dp[i - 1][l] + dp[i - 1][r]

                # 理解二：当左右边界存在时，表示存在这种组合，才加上计数
                l,r = j - nums[i - 1],j + nums[i - 1]
                if l >= 0: dp[i][j] = dp[i - 1][l]
                if r < t: dp[i][j] += dp[i - 1][r]

        return dp[-1][num_sum + target]

    # 5. 动态规划，模仿官方题解
    def findTargetSumWays(self,nums: List[int],target: int) -> int:
        """
        总和为sum, 所有“-”构成的和为neg( > 0), 剩下的数都是"+"了，构成的和为sum-neg
             5                    1                   5 - (1) = 4
        target = -1 + 4 = -neg + sum - neg = sum - 2 * neg
        neg = (sum - target) / 2
        """
        nums_sum = sum(nums)
        diff = nums_sum - target
        if diff < 0 or diff % 2 == 1: return 0

        neg,size = diff // 2,len(nums)
        # 问题转换为从nums中选取k个数，之和为neg
        # 二维数组开始, neg + 1, 为了取值方便;
        dp = [[0] * (neg + 1) for _ in range(size)]  # dp[size][neg+1]
        dp[0][0] = 1
        if neg >= nums[0]:
            dp[0][nums[0]] = 1
            if nums[0] == 0: dp[0][0] = 2
        # dp[i][j]: 候选集nums[0 - i], 和为neg
        # 不选nums[i] + 一定选nums[i]
        for i in range(1,size):
            for j in range(neg + 1):
                dp[i][j] = dp[i - 1][j]
                # if i == 1 && j == num[1], dp[1][j] += dp[0][0], 这个时候dp[0][0]就得为1了
                if j >= nums[i]:
                    dp[i][j] += dp[i - 1][j - nums[i]]
        # print(dp)
        return dp[-1][-1]

    # 6. 动态规划，官方题解
    def findTargetSumWays6(self,nums: List[int],target: int) -> int:
        nums_sum = sum(nums)
        diff = nums_sum - target
        if diff < 0 or diff % 2 == 1: return 0
        neg,size = diff // 2,len(nums)
        # dp[size+1][neg+1]的做法在num[0]为0的时候这么简洁
        dp = [[0] * (neg + 1) for _ in range(size + 1)]
        dp[0][0] = 1
        for i in range(1,size + 1):
            # j还是得从0开始
            for j in range(neg + 1):
                dp[i][j] = dp[i - 1][j]
                if nums[i - 1] <= j:
                    dp[i][j] += dp[i - 1][j - nums[i - 1]]
        return dp[-1][-1]

    # 7. 动态规划，官方题解  一维数组
    def findTargetSumWays7(self,nums: List[int],target: int) -> int:
        nums_sum = sum(nums)
        diff = nums_sum - target
        if diff < 0 or diff % 2 == 1: return 0
        neg,size = diff // 2,len(nums)

        dp = [1] + [0] * neg

        # for i in range(1, size + 1):
        #     for j in range(neg, nums[i - 1] - 1, -1):
        #         dp[j] += dp[j - nums[i - 1]]

        # dp序号和i无关
        for n in nums:
            for j in range(neg,n - 1,-1):
                dp[j] += dp[j - n]

        return dp[-1]


s = Solution()

print(s.findTargetSumWays([1,1,1,1,1],3) == 5)
print(s.findTargetSumWays([1],1) == 1)
print(s.findTargetSumWays([1,1],0) == 2)
print(s.findTargetSumWays([1,1,1],3) == 1)
print(s.findTargetSumWays([1,1,1],0) == 0)
print(s.findTargetSumWays([0,0,0,0,0,0,0,0,1],1) == 256)
print(s.findTargetSumWays([0,0,1],1) == 4)
print(s.findTargetSumWays([0,1],1) == 2)
print(s.findTargetSumWays([2,107,109,113,127,131,137,3,2,3,5,7,11,13,17,19,23,29,47,53],1000) == 0)
