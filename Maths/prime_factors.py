from math import sqrt

def is_prime(n):
    if n == 1:
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0: 
            return False
        i += 6
    
    return True

def prime_factors(n):
    arr = []

    for i in range(2, n // 2 + 1):
        if is_prime(i):
            if n % i == 0:
                temp = i * i
                count = 1
                while n % temp == 0:
                    count += 1
                    temp = pow(i, count + 1)

                arr.append((i, count))

    return arr

n = int(input())
print('Prime factorization of', n)
for i in prime_factors(n):
    print('%d^%d' %(i[0], i[1]))