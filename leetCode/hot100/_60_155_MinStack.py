# coding=utf-8
"""
155. 最小栈
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

实现 MinStack 类:

MinStack() 初始化堆栈对象。
void push(int val) 将元素val推入堆栈。
void pop() 删除堆栈顶部的元素。
int top() 获取堆栈顶部的元素。
int getMin() 获取堆栈中的最小元素。

https://leetcode.cn/problems/min-stack/
"""


class MinStack:

    def __init__(self):
        self.stack = []
        # stack的栈顶元素stack[-1]存在时，对应的全局最小值
        self.topStack = []

    def push(self,val: int) -> None:
        self.stack.append(val)
        if self.topStack and val > self.topStack[-1]:
            self.topStack.append(self.topStack[-1])
        else:
            self.topStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.topStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.topStack[-1]


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin() == -3)
minStack.pop()
print(minStack.top() == 0)
print(minStack.getMin() == -2)
minStack.push(3)
print(minStack.top() == 3)
print(minStack.getMin() == -2)
