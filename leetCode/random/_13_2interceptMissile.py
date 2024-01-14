# 敌人发来n枚导弹，高度为h1, h2, … , hn; 我方有导弹拦截系统，第一发任意高度，以后一发比一发低，求最多能拦截多少导弹?
# 实际上为求最长递减序列；
#    第一发导弹最关键
# 例如对于int x[] = {89, 207, 155, 300, 299, 170, 158, 265};
#
# 最关键是逆序，可以下个结论：一维数组的都要逆序，
# 但是o(n^2)的复杂度还是绕不开的


class Solution:
    def findMax(self,array):
        length = len(array)
        # 下面两字段为了后续输出方便
        firstIndex = length - 1  # 第一枚应该拦截的导弹位置
        maxNum = 1  # 最多能拦截几个
        # 用一维度数组来记录可以拦截多少个，但是遍历还得两层for循环
        maxNums = [1 for i in range(length)]
        for i in range(length - 2,-1,-1):
            # 本层循环i不变，j变；maxNums[i+1:]之后都是算好了的，要给maxNums[i]赋值
            for j in range(i,length - 1):
                # 导弹高度小于array[i] && 记录在案的拦截数量多余maxNums[i]
                if array[j] < array[i] and maxNums[j] >= maxNums[i]:
                    maxNums[i] = maxNums[j] + 1

            # 记录一下，为了方便后续输出结果
            if maxNums[i] > maxNum:
                maxNum = maxNums[i]
                firstIndex = i

        # 输出最大递减序列
        print("can intercept maxLenth: ",maxNum)
        print("序列顺序为：",array[firstIndex],end=" ")
        nextIndex = firstIndex
        for i in range(nextIndex,length):
            if array[i] < array[nextIndex] and maxNums[i] == maxNums[nextIndex] - 1:
                print(array[i],end=" ")
                nextIndex = i
        print()


solution = Solution()
array = [389,207,155,300,299,170,158,65]
solution.findMax(array)  # 389 300 299 170 158

array = [65,300,155,300,299,170,158,389]
solution.findMax(array)  # 300 299 170 158
