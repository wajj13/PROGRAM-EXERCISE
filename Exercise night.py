# 对列表元素去重
L1 = [123, 12, 31, 254, 12, 4, 32, 54523, 4, 4, 4, 4, 4]


def p(x):
    result = []
    for item in x:
        if item not in result:
            result.append(item)
    return result
print(p(L1))

