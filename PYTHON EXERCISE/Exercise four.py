#求区间素数
def a_prime(number):
    if number in (1, 2):
        return True
    for idx in range(2, number):
        if number % idx == 0:
            return False
    return True
def print_prime(begin, end):
    for number in range(begin, end+1):
        if a_prime(number):
            print(f"{number} is a prime")
begin = 1
end = 100
print_prime(begin, end)

#GPT:
def is_prime(number):
    if number < 2:
        return False
    for idx in range(2, int(number ** 0.5) + 1):
        if number % idx == 0:
            return False
    return True

def print_primes(begin, end):
    for number in range(begin, end + 1):
        if is_prime(number):
            print(f"{number} is a prime")

begin, end = 1, 100
print_primes(begin, end)
