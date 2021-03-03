# Time Complexity: O(log(min(m, n)))
def gcd(m, n):
    if m < n:
        m, n = n, m

    if m % n == 0:
        return n

    while m % n != 0:
        m, n = n, m % n
    
    return n

m, n = map(int, input().split())
res = gcd(m, n)
print("GCD of %d and %d is %d" %(m, n, res))
print("LCM of %d and %d is %d" %(m, n, m * n // res))
