#求前N个数字的平方和
def sum_of_square(n):
    result = 0
    for numeber in range(1, n+1):
        result += numeber*numeber
    return result
    return n
print(sum_of_square(3))
print(sum_of_square(5))
print(sum_of_square(10))

#GPT
def sum_of_squares(n):
    return sum(i**2 for i in range(1, n+1))

print(sum_of_squares(3))
print(sum_of_squares(5))
print(sum_of_squares(10))


