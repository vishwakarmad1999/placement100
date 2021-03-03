def checkBit(pattern, arr, n):
    count = 0
    for i in range(n):
        if pattern & arr[i] == pattern:
            count += 1
    return count

def foo(arr, n):
    res = 0
    for i in range(16, -1, -1):
        count = checkBit(res | 1 << i, arr, n)
        if count >= 2:
            res |= 1 << i
    return res

n = int(input())
arr = list(map(int, input().split()))
print(foo(arr, n))

