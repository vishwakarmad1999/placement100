from math import sqrt

def prime_factors(n):
    arr = []

    for i in range(2, int(sqrt(n)) + 1):
        count = 0
        while n % i == 0:
            count += 1
            n //= i

        if count:
            arr.append((i, count))

    return arr

n = int(input())
res = prime_factors(n)

if len(res):
    for i in res:
        print(i[0], i[1])
else:
    print((n, 1))