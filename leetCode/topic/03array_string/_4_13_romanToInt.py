# 罗马数字包含以下七种字符:I，V，X，L，C，D和M。
#
# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 例如， 罗马数字 2 写做II，即为两个并列的 1。12 写做XII，即为X+II。 27 写做XXVII, 即为XX+V+II。
#
# 通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做IIII，而是IV。数字 1 在数字 5 的左边，
# 所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为IX。这个特殊的规则只适用于以下六种情况：
#
# I可以放在V(5) 和X(10) 的左边，来表示 4 和 9。 IV, IX
# X可以放在L(50) 和C(100) 的左边，来表示 40 和90。XL, XC
# C可以放在D(500) 和M(1000) 的左边，来表示400 和900。CD, CM
# 给定一个罗马数字，将其转换成整数。输入确保在 1到 3999 的范围内。
#
# 示例1:
# 输入:"III"
# 输出: 3

# 示例2:
# 输入:"IV"
# 输出: 4

# 示例3:
# 输入:"IX"
# 输出: 9

# 示例4:
# 输入:"LVIII"
# 输出: 58
# 解释: L = 50, V= 5, III = 3.

# 示例5:
# 输入:"MCMXCIV"
# 输出: 1994
# 解释: M = 1000, CM = 900, XC = 90, IV = 4.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/roman-to-integer

class Solution:
    def romanToInt1(self,s: str) -> int:
        # 1. 定义字典
        dict = {"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000,
                "IV": 4,"IX": 9,"XL": 40,"XC": 90,"CD": 400,"CM": 900}
        result = 0
        i = 0
        while i < len(s):
            temp = s[i]

            # 2. 判断六种特殊情况是否存在 4，9， 40，90，400，900
            if i + 1 < len(s) and (temp == "I" or temp == "X" or temp == "C"):
                tempStr = s[i] + s[i + 1]
                if tempStr in dict:
                    temp = tempStr
                    i = i + 1

            # 3. 真实求解
            result += dict[temp]
            i = i + 1
        return result

    # 别人的优秀做法：对字符串从左到右来，
    # 如果当前字符代表的值不小于其右边，就加上该值；
    # 否则就减去该值。以此类推到最右边的数
    def romanToInt2(self,s):
        a = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
        ans = 0
        for i in range(len(s)):
            if i < len(s) - 1 and a[s[i]] < a[s[i + 1]]:
                ans -= a[s[i]]
            else:
                ans += a[s[i]]
        return ans

    # 3. 公司组织leetcode比赛，重写
    def romanToInt(self,s: str) -> int:
        nums_dict = {
            "I": 1,"V": 5,"X": 10,"L": 50,
            "C": 100,"D": 500,"M": 1000
        }

        answer,length = 0,len(s)
        for i in range(length):
            # if i + 1 < length and s[i: i + 2] in ["IV", "IX", "XL", "XC", "CD", "CM"]:
            if i + 1 < length and nums_dict[s[i]] < nums_dict[s[i + 1]]:
                answer -= nums_dict[s[i]]
            else:
                answer += nums_dict[s[i]]
        return answer


# 开始测试
solution = Solution()

print(solution.romanToInt("MCDLXXVI") == 1476)
print(solution.romanToInt("VI") == 6)
print(solution.romanToInt("IV") == 4)
print(solution.romanToInt("XIV") == 14)
print(solution.romanToInt("LVIII") == 58)
print(solution.romanToInt("MCMXCIV") == 1994)
print(solution.romanToInt("III") == 3)
