def all_divisors(n):
    arr = []
    i = 1
    while i * i < n:
        if n % i == 0:
            arr.append(i)
        i += 1
    
    while i >= 1:
        if n % i == 0:
            arr.append(n // i)
        i -= 1
    
    return arr

n = int(input())
res = all_divisors(n)

print(res)