def convert(n):
    return n ^ n >> 1

n = int(input())
print(convert(n))