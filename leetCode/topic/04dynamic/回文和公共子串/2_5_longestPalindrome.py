#
"""
5. 最长回文子串
给你一个字符串 s，找到 s 中最长的回文子串。
"""


# 示例 1：
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
#
# 示例 2：
# 输入: "cbbd"
# 输出: "bb"
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-palindromic-substring

class Solution:

    # 1. 暴力破解法
    # 遍历出所有的字符串，判断是否是回文数，并且和暂存最长长度比较： o(n**3)
    def longestPalindrome1(self,s: str) -> str:
        def is_palindrome(start,end) -> bool:
            while start < end:
                if s[start] != s[end]:
                    return False
                else:
                    start += 1
                    end -= 1
            return True

        max_len,begin,length = 1,0,len(s)
        # 这次的s[i,j]判断回文是包头包尾的
        for i in range(length - 1):  # 单个字符进不来这个循环
            for j in range(i + 1,length):
                if j - i + 1 > max_len and is_palindrome(i,j):
                    max_len = j - i + 1
                    begin = i
        # print(begin, max_len, s[begin: begin + max_len + 1])
        return s[begin: begin + max_len]

    # 动态规划也是遍历了所有的字符组合，只是对于每个字符不需要再次去遍历去判断是否为回文：o(n^2),
    # 2. 动态规划 之 01背包  二维数组存的是回文长度
    # 参考网友智慧： https://leetcode-cn.com/problems/longest-palindromic-substring/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-bao-gu/
    # 2.1 中间变量使用二维数组 flags, 好理解，但是空间复杂度为o(n^2)
    # flags[i][j]: 正逆序两个字符串(s[:i], s取反后[:j])最大能出现多长的回文
    def longestPalindrome21(self,s: str) -> str:
        reversed_s = s[::-1]
        max_len,end,length = 0,0,len(s)
        flags = [[0] * length for _ in range(length)]
        for i in range(length):
            for j in range(length):
                if s[i] == reversed_s[j]:
                    if i == 0 or j == 0:
                        flags[i][j] = 1
                    else:
                        flags[i][j] = flags[i - 1][j - 1] + 1

                    if flags[i][j] > max_len:
                        # 从倒序推出正序位置, 即回文的开头
                        original_order = length - 1 - j
                        # 回文开头 + 字符长度 == 回文结尾; 例子: aacabkacaa
                        if original_order + flags[i][j] - 1 == i:
                            max_len = flags[i][j]
                            end = i
        # print(flags)
        # print(s[end + 1 - max_len: end + 1], end, max_len)
        return s[end + 1 - max_len: end + 1]

    # 2.2 优化上面 中间变量一维数组 matrix, 不好理解，空间复杂度为o(n)； 这么精妙的算法，我表示只能记忆了
    def longestPalindrome22(self,s: str) -> str:
        reversed_s = s[::-1]
        length,max_len,end = len(s),0,0
        flags = [0] * length

        for i in range(length):
            # 不同点1：f[8] = f[7] + 1, f[9] = f[8] + 1, f[8]就被覆盖了，所以得倒序
            for j in range(length - 1,-1,-1):
                if s[i] == reversed_s[j]:
                    # python数组虽然不会越界，但是flags[-1]会取最后一个
                    if j == 0 or i == 0:
                        flags[j] = 1
                    else:
                        flags[j] = flags[j - 1] + 1

                    if flags[j] > max_len:
                        original_order = length - 1 - j
                        if original_order + flags[j] - 1 == i:
                            max_len = flags[j]
                            end = i
                else:
                    # 不同点2：二维数组不相等的地方是0，这里也得手动置为0，否则下一行使用就错了
                    flags[j] = 0
            # print(i, flags)
        # print(flags, end, max_len, s[end - max_len + 1: end + 1])
        return s[end - max_len + 1: end + 1]

    # 3. 动态规划 之 回文字符串定义本身:  s(i,j) = s(i+1,j−1) and (si ==sj)
    def longestPalindrome3(self,s: str) -> str:
        """
        1. dp: 行: 字符串正序；列：字符串逆序 -> dp[i][j]=True表示s[i:j+1]为回文, [i, j]
          d(i,j) = d(i+1,j−1) and (si ==sj)   len > 2
          d(i,j) = si ==sj  len == 2
          d(i,j) = True     len == 1
        2. 遍历了半个三角 n**2 / 2：
           因为那个len>2的状态方程，所以遍历顺序：从上到下，从左到右
        """
        max_len,begin,length = 1,0,len(s)
        dp = [[False] * length for _ in range(length)]
        for i in range(length):
            dp[i][i] = True

        # 遍历上三角形，上三角形；s[i:j], 下三角(i > j)重复了，再遍历就没有什么意义了
        for j in range(1,length):
            for i in range(j):
                # 所以遍历顺序为：列，行
                dp[i][j] = s[i] == s[j] and (j == i + 1 or dp[i + 1][j - 1])

                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
        return s[begin: begin + max_len]

    # 4. 中心扩散法, 也是o(n**2), 但是速度快乐很多, 这个应该得看用例的实际情况吧？
    # aaaaa
    # 以某个字符串为中心的，可以考虑动态规划 or 中心扩散
    def longestPalindrome(self,s: str) -> str:
        def spread(left,right):
            while left >= 0 and right < length and s[left] == s[right]:
                left,right = left - 1,right + 1
            return right - left - 1

        max_len,begin,length = 1,0,len(s)
        for i in range(1,length):
            odd_len = spread(i,i)
            even_len = spread(i - 1,i)
            temp_len = max(odd_len,even_len)

            if temp_len > max_len:
                max_len = temp_len
                begin = i - temp_len // 2
        # print(begin, max_len, s[begin: begin + max_len])
        return s[begin: begin + max_len]

    # 5. 马拉车算法, 待续...


solution = Solution()

print(solution.longestPalindrome("a") == "a")
print(solution.longestPalindrome("aa") == "aa")
print(solution.longestPalindrome("abba") == "abba")
print(solution.longestPalindrome("babad") == "bab")  # bab aba
print(solution.longestPalindrome("cbbd") == "bb")
print(solution.longestPalindrome("babaddaad") == "adda")
print(solution.longestPalindrome("aaca") == "aca")
print(solution.longestPalindrome("aacabkacaa") == "aca")
