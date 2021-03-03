'''
def count_set_bits(n):
    count = 0
    while n > 0:
        if n & 1:
            count += 1
        n = n >> 1
    return count
'''

# Brian Kerningam's Method
def count_set_bits(n):
    count = 0
    while n > 0:
        n = n & (n - 1)
        count += 1
    return count

n = int(input())
print(count_set_bits(n))