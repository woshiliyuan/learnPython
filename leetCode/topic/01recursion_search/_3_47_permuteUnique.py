# coding=utf-8
"""
47. 全排列 II
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

https://leetcode-cn.com/problems/permutations-ii/
"""

from typing import List


class Solution:

    def permuteUnique1(self,nums: List[int]) -> List[List[int]]:
        def get_permute(temp_list):
            if len(temp_list) == len(nums):
                answer.append(temp_list)
                return

            for i in range(len(nums)):
                # if i > index and nums[i] == nums[i-1]:
                #     return
                if i > 0 and nums[i] == nums[i - 1] and visited[i - 1] == 0:
                    continue
                if visited[i] == 1:
                    continue
                visited[i] = 1
                get_permute(temp_list + [nums[i]])
                visited[i] = 0

        answer,visited = [],[0] * len(nums)
        nums.sort()
        get_permute([])
        print(answer)
        return answer

    def permuteUnique(self,nums: List[int]) -> List[List[int]]:
        def dfs(temp_list):
            if len(temp_list) == size:
                answer.append(temp_list)
                return

            for i in range(size):
                if visited[i]: continue
                # 只记录顺序，不记录倒序的
                # [..., 1(1), 1(2), 2];  如果是[..., 1(2), 1(1), 2], 此时1(2)开头，1(1)必定未访问，即visited[i-1] == 0, 舍去
                if i > 0 and nums[i] == nums[i - 1] and visited[i - 1] == 0: continue

                visited[i] = 1
                dfs(temp_list + [nums[i]])
                visited[i] = 0

        size = len(nums)
        answer,visited = [],[0] * size
        nums.sort()
        dfs([])
        return answer


s = Solution()
print(s.permuteUnique([1,1,2]))
# equals_array(s.permuteUnique([1,1,2]), [[1,1,2], [1,2,1], [2,1,1]])
# equals_array(s.permuteUnique([1,2,3]), [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])
