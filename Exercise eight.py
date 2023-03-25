# 去除区间中某些数
# def remove_elements_from_list(L1, L2):
#     for item in L2:
#         L1.remove(item)
#     return L1
#
#
L1 = [12, 3, 123, 12, 3, 12, 23, 3, 1, 24, 345, 345]
L2 = [12, 23]
data = [item for item in L1 if item not in L2]
# print(f"from {L1} remove {L2}, result: ", remove_elements_from_list(L1, L2))
print(data)