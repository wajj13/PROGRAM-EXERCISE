# 求区间偶数
def a_evennumbers(begin, end):
    result = []
    for item in range(begin, end):
        if item % 2 == 0:
            result.append(item)
    return result


begin = 1
end = 50
print(f"begin={begin}, end={end},even numbers:", a_evennumbers(begin, end))
#gpt
def even_numbers(begin, end):
    return list(range(begin + (begin % 2), end, 2))

begin = 1
end = 50
print(f"begin={begin}, end={end}, even numbers:", even_numbers(begin, end))
