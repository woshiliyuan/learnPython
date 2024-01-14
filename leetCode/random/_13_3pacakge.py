# 著名的“01背包”问题：
# 给你一个背包，最大能承受之重W，现在有物品数N
# 求怎么组合能装出最大价值呢？
#
# 输入：
# 背包重量，物品数
# w1, v1
# w2, v2
# …
# wn, vn
# 输出：
# 最大价值
#
# 输入样例：
# 10 3
# 3 4
# 4 5
# 5 6
# 样例输出：
# 11


class Solution:
    W,N = input("请输入背包最大重量和物品数：").split(" ")
    W = int(W)
    N = int(N)
    print(W,", ",N)
    ws = []
    vs = []
    for i in range(N):
        w,v = input(str(i) + " 请输入物品重量和价值：").split(" ")
        ws.append(int(w))
        vs.append(int(v))
    values = []

    def findMaxValue(self):
        global values
        # 常用套路，从1开始真正计算，index=0处默认填充
        values = [[0 for i in range(self.W + 1)] for i in range(self.N + 1)]
        for i in range(1,self.N + 1):
            for j in range(1,self.W + 1):
                if j >= self.ws[i - 1]:
                    # 1. abort object i
                    # v1 = values[i-1][j]
                    # 2. add object i
                    # print(j, " ", ws[i-1])
                    addiValue = values[i - 1][j - self.ws[i - 1]] + self.vs[i - 1]
                    values[i][j] = max(values[i - 1][j],addiValue)
                else:
                    values[i][j] = values[i - 1][j]
        return values[self.N][self.W]

    def findDetail(self):
        global values
        j = self.W
        for i in range(self.N,0,-1):
            if values[i][j] != values[i - 1][j]:
                print("added object %s: w %s, v %s " % (i,self.ws[i - 1],self.vs[i - 1]))
                j = j - self.ws[i - 1]

    # 使用一维数组搞定
    def findMaxValue2(self):
        global values
        # 初始化 w+1容量，为什么呢？
        values = [0 for i in range(self.W)]
        # 有多少个物品，就遍历多少次
        for i in range(self.N):
            # j从W开始，values[W]取的就是数组最后的位置，长度为（W+1）,
            for j in range(self.W - 1,self.ws[i] - 2,-1):
                if j >= self.ws[i]:
                    addiValue = values[j - self.ws[i]] + self.vs[i]
                else:
                    addiValue = self.vs[i]
                values[j] = max(values[j],addiValue)
        print(values)
        return values[self.W - 1]

    # def findDetail2(self):


solution = Solution()

# result = solution.findMaxValue()
# print("maxValue: ", result)
# print(solution.values)
# solution.findDetail()

result = solution.findMaxValue2()
print("maxValue: ",result)
print(solution.values,", W: ",solution.W)
