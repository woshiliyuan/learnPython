"""
导弹拦截问题
敌人发来n枚导弹，高度为h1, h2, … , hn; 我方有导弹拦截系统，第一发任意高度，以后一发比一发低，求最多能拦截多少导弹?
实际上为求最长递减序列；
"""


class Solution:
    # 1. 逆序. d[i]: 从第i枚开始，能拦截多少枚
    def findMax0(self,array):
        length = len(array)
        # 第一枚应该拦截的导弹位置, 最多能拦截几个
        firstIndex,maxNum,maxNums = length - 1,1,[1] * length
        for i in range(length - 2,-1,-1):
            # 找到(i, length-1)中与maxNum[i]差距最小的那个高度
            for j in range(i,length):
                if array[j] < array[i] and maxNums[j] >= maxNums[i]:
                    maxNums[i] = maxNums[j] + 1

            if maxNums[i] > maxNum:
                maxNum = maxNums[i]
                firstIndex = i

        # 输出最大递减序列
        answer = [array[firstIndex]]
        last_index = firstIndex
        for i in range(last_index + 1,length):
            if array[i] < answer[-1] and maxNums[i] == maxNums[last_index] - 1:
                answer.append(array[i])
                last_index = i
        return answer

    # 2. 正序. d[i]：从第i枚结束，能拦截多少递减的
    def findMax(self,array):
        length = len(array)
        max_end,max_size,last_index = [1] * length,1,0
        for i in range(1,length):
            for j in range(i):
                if array[i] < array[j] and max_end[i] <= max_end[j]:
                    max_end[i] = max_end[j] + 1

            if max_end[i] > max_size:
                max_size = max_end[i]
                last_index = i
        print(max_size,max_end)

        answer = [array[last_index]]
        for i in range(last_index - 1,-1,-1):
            if array[i] > array[last_index] and max_end[i] == max_end[last_index] - 1:
                last_index = i
                answer.append(array[i])
        answer.reverse()
        print(answer)
        return answer


s = Solution()
print(s.findMax([389,207,155,300,299,170,158,65]) == [389,300,299,170,158,65])
print(s.findMax([65,300,155,300,299,170,158,389]) == [300,299,170,158])
