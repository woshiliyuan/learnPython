"""
题目：给一个函数传参n，n可以等于100，10000，10万，100万，请用程序分别求出n以内的所有素数之和。
"""


class Solution:
    def sumOfPrime(self,n: int):
        result = 0
        for temp in range(2,n + 1):
            flag = self.isPrime(temp)
            if (flag):
                print("Prime: ",temp)
                result += temp
        return result

    # 判断一个数是否为素数
    def isPrime(self,n):
        for index in range(2,int(n ** 0.5) + 1):
            if n % index == 0:
                return False
        return True


solution = Solution()

# 求解n以内的所有素数之和
# result = solution.sumOfPrime(10)
# print("sum: ", result)

result = solution.sumOfPrime(100)
print("sum: ",result)
#
# result = solution.sumOfPrime(10000)
# print("sum: ", result)
#
# result = solution.sumOfPrime(100000)
# print("sum: ", result)
#
# result = solution.sumOfPrime(1000000)
# print("sum: ", result)
