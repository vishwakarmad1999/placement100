# An effecient approach. Time Complexity = O(sqrt(n)) / 3
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

n = int(input('Enter a number: '))

if is_prime(n):
    print('%d is a prime number' %n)
else:
    print('%d is not a prime number' %n)