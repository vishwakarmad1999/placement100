from math import log, floor

# Using recursion
def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

# Using iteration
def count_digits(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count

# Using log
def count_digits(n):
    return floor(log(n, 10)) + 1

n = int(input())

if n == 0:
    res = 1
else:
    res = count_digits(n)
    
print(res)