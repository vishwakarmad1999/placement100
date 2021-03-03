n, k = map(int, input().split())

'''
Method 1
if 1 << (k - 1) & n:
    print("Yes")
else:
    print("No")

Method 2
if n >> (k - 1) & 1:
    print("Yes")
else:
    print("No")
'''
