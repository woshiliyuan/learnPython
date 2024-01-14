# coding=utf-8


def fib_recursion(n):
    if n <= 2:
        return 1
    else:
        return fib_recursion(n-1) + fib_recursion(n-2)


def fib_stack(n):
    stack, result = [], 0
    stack.append(n)

    while len(stack) > 0:
        num = stack.pop()
        if num <= 2:
            result += 1
        else:
            stack.append(num-1)
            stack.append(num-2)
    return result


# 测试
print(fib_recursion(5))
print(fib_stack(5))

