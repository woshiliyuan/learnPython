# coding=utf-8
def equals_array(a, b):
    """
    判断两个一维或者二维数组是否相等
    """
    if len(a) != len(b):
        print(False)
        return

    # 二维数组，有点点麻烦; a可能为[]
    if type(a and a[0]) is list:
        for item in a:
            item.sort()
        for item in b:
            item.sort()
            if item not in a:
                print(False)
                return
        print(True)

    else:
        a.sort()
        b.sort()
        print(a == b)


if __name__ == '__main__':
    list1 = ["one","two","three"]
    list2 = ["one","two2","three"]
    equals_array(list1, list2)

    list1 = [[1,2], [3,4]]
    list2 = [[3,4], [1,2]]
    equals_array(list1, list2)

    list1 = [[1, 2], [], [3, 4]]
    list2 = [[3, 4], [1, 2], []]
    equals_array(list1, list2)



