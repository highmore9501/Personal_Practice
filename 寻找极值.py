# -*- coding: utf-8 -*-
def findMinAndMax(L):
    x1,x2 = L[0]
    for i in L:
        if i < x1:
            x2 = i
        elif i > x1:
            x1 = i
    return (x1,x2)
    pass

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
