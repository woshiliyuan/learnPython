# 为了解决“_13longestPalindromeSubseq”： 最长回文子序列，而特别篇
# 最长子序列

# 题目：两个字符串 "12345" && “145”，求最长公共子序列

class Solution:
    def longestSubseq(self,s1: str,s2: str):
        subSeq = ''

        # 1. 初始化二维数组记录所有情况: len(s1)+1 * len(s2)+1
        # 这里的行列很容易写错
        matrix = [[0 for i in range(len(s2) + 1)] for i in range(len(s1) + 1)]
        # 为了防止matrix[i-1][j-1]数组越界，index从1开始
        for i in range(1,len(s1) + 1):
            for j in range(1,len(s2) + 1):
                # 2.1 若字符相等，则记录长度+1
                if s1[i - 1] == s2[j - 1]:
                    matrix[i][j] = matrix[i - 1][j - 1] + 1
                    subSeq += s1[i - 1]
                # 2.2 不相等则取相邻最大的那个
                else:
                    if matrix[i][j - 1] > matrix[i - 1][j]:
                        matrix[i][j] = matrix[i][j - 1]
                    else:
                        matrix[i][j] = matrix[i - 1][j]

        print("max common sequence lenth: ",matrix[i][j])
        return subSeq


solution = Solution()
print(solution.longestSubseq("12345","145"))
print(solution.longestSubseq("12345","165"))
