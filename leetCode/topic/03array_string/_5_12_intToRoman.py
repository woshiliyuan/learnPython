# 罗马数字包含以下七种字符：I，V，X，L，C，D和M。
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
# 通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做IIII，而是IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为IX。这个特殊的规则只适用于以下六种情况：
#
# I可以放在V(5) 和X(10) 的左边，来表示 4 和 9。
# X可以放在L(50) 和C(100) 的左边，来表示 40 和90。
# C可以放在D(500) 和M(1000) 的左边，来表示400 和900。
# 给定一个整数，将其转为罗马数字。输入确保在 1到 3999 的范围内。
#
# 示例1:
# 输入:3
# 输出: "III"
#
# 示例2:
# 输入:4
# 输出: "IV"
#
# 示例3:
# 输入:9
# 输出: "IX"
#
# 示例4:
# 输入:58
# 输出: "LVIII"
# 解释: L = 50, V = 5, III = 3.
#
# 示例5:
# 输入:1994
# 输出: "MCMXCIV"
# 解释: M = 1000, CM = 900, XC = 90, IV = 4.
#
# 链接：https://leetcode-cn.com/problems/integer-to-roman

class Solution:
    # 太菜了我，本次不会写
    # def intToRoman(self, num: int) -> str:
    #     result = ""
    #     str = str(num)
    #     if len(str) == 4:
    #         for i in range(num/1000):
    #             result += "M"
    #         num = num % 1000
    #         str = str(num)
    #     if len(str) == 3:
    #
    #     return 0

    # 借鉴别人写的，厉害，佩服: 从大位到小位分解
    def intToRoman1(self,num: int) -> str:
        values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        reps = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]

        res = ""
        for i in range(len(values)):
            while num >= values[i]:
                num -= values[i]
                res += reps[i]
        return res

    # 从小到大，从各位到大位分解
    def intToRoman(self,num: int) -> str:
        nums_dict = {
            1: "I",2: "II",3: "III",4: "IV",5: "V",6: "VI",7: "VII",8: "VIII",9: "IX",
            10: "X",20: "XX",30: "XXX",40: "XL",50: "L",60: "LX",70: "LXX",80: "LXXX",90: "XC",
            100: "C",200: "CC",300: "CCC",400: "CD",500: "D",600: "DC",700: "DCC",800: "DCCC",900: "CM",
            1000: "M",2000: "MM",3000: "MMM",
        }

        answer,position = "",1
        while num != 0:
            key = num % 10 * position
            if key != 0:
                answer = nums_dict[key] + answer
            num,position = num // 10,position * 10
        return answer


solution = Solution()
print(solution.intToRoman(3) == "III")
print(solution.intToRoman(4) == "IV")
print(solution.intToRoman(9) == "IX")
print(solution.intToRoman(10) == "X")
print(solution.intToRoman(58) == "LVIII")
print(solution.intToRoman(1994) == "MCMXCIV")
