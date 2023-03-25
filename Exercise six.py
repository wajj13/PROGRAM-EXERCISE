# 求列表数字之和

def sum_of_list(p):
    total = 0
    for item in p:
        total += item
    return total


l1 = [4, 6, 23, 4, 3432, 42, 34, 234, 23, 423, 4, 235, 236, 2]
l2 = [12, 31, 23, 12, 312, 42, 35, 347, 646756856, 756, 7, 568, 76, 867, 8];
print(sum_of_list(l1))
print(sum_of_list(l2))

# print(f"sum of {l1},", sum_of_list(l1))
# print(f"sum of {l2},", sum_of_list(l2))


#gpt
def sum_of_list(p):
    return sum(p)

l1 = [4, 6, 23, 4, 3432, 42, 34, 234, 23, 423, 4, 235, 236, 2]
l2 = [12, 31, 23, 12, 312, 42, 35, 347, 646756856, 756, 7, 568, 76, 867, 8]
print(sum_of_list(l1))
print(sum_of_list(l2))
