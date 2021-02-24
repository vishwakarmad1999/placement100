n = int(input())

if n == 0:
    print("No")
else:
    if n & (n - 1) == 0:
        print("Yes")
    else:
        print("No")