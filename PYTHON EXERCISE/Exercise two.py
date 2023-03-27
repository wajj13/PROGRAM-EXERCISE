
#数字的阶乘
def get_jiecheng(number):
    result = 1
    while number > 0:
        result *= number
        number -= 1
    return result
print("jiecheng 6 = ",get_jiecheng(6))
print("jiecheng 3= ",get_jiecheng(3))
print("jiecheng 30 = ",get_jiecheng(30))

#GPT:
from math import factorial

def get_jiecheng(number):
    return factorial(number)

print("jiecheng 6 = ", get_jiecheng(6))
print("jiecheng 3 = ", get_jiecheng(3))
print("jiecheng 30 = ", get_jiecheng(30))