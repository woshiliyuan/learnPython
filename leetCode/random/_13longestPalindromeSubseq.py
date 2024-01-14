# 给定一个字符串s，找到其中最长的回文子序列。可以假设s的最大长度为1000。
#
# 示例 1:
# 输入: "bbbab"
# 输出: 3
# 一个可能的最长回文子序列为 "bbb"。
#
# 示例 2:
# 输入: "cbbd"
# 输出: 2
# 一个可能的最长回文子序列为 "bb"。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-palindromic-subsequence


class Solution:
    # 本来还想借第12题，偷个懒，但是却是不一样的
    def longestPalindromeSubseq1(self,s: str) -> int:
        # 1. 反转，求反转字符串reverse和原来字符串origin直接的最长公共子序列
        reverse = s[::-1]
        length = len(s)

        # 2. 一维数组就够了
        matrix = [0 for i in range(length)]
        maxLen = 0
        maxEnd = 0

        for i in range(length):
            # 3. 如果用一维度数组，此处为什么不能正序，要逆序呢，太高明了，佩服佩服
            # for j in range(length):
            for j in range(length - 1,-1,-1):
                if s[i] == reverse[j]:
                    # 防止数组越界 matrix[j - 1]
                    if i == 0 or j == 0:
                        matrix[j] = 1
                    else:
                        matrix[j] = matrix[j - 1] + 1

                    # 4. 可以取代最大值
                    if matrix[j] > maxLen:
                        # 反转前的序号
                        beforeRev = length - 1 - j
                        # 放在正序中判断是否是回文，对单个字符而言
                        if beforeRev + matrix[j] - 1 == i:  # 判断下标是否对应
                            maxLen = matrix[j]
                            maxEnd = i
                # 一维度数组此处太难发觉这个错误了，需要置为0，否则影响后面的使用；二维数组不共用其它列，初始化为0，所有不用
                else:
                    matrix[j] = 0

        # print(maxEnd, ", ", maxLen)
        return maxLen

    def longestPalindromeSubseq(self,s: str) -> int:
        n = len(s)
        dp = [0 for i in range(n)]

        for j in range(n):
            dp[j] = 1
            max = 0
            for i in range(j - 1,-1,-1):
                if s[i] == s[j]:
                    dp[i] = max + 2
                    if max < dp[i]:
                        max = dp[i]
        # for i in range(n):
        #     if dp[i] > max:
        #         max = dp[i]

        return max

    def longestPalindromeSubseq(self,s: str) -> int:
        n = len(s)
        dp = [[0 for i in range(n)] for i in range(n)]
        for i in range(n):
            dp[i][i] = 1

        # 反着遍历保证正确的状态转移
        for i in range(n - 1,-1,-1):
            for j in range(i + 1,n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    if dp[i + 1][j] >= dp[i][j - 1]:
                        dp[i][j] = dp[i + 1][j]
                    else:
                        dp[i][j] = dp[i][j - 1]

        # 整个 s 的最长回文子串长度
        return dp[0][n - 1]


solution = Solution()

result = solution.longestPalindromeSubseq("bbbab")
print(result)  # 3

result = solution.longestPalindromeSubseq("cbbd")
print(result)  # 2
