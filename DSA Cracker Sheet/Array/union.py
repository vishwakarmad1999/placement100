MAX = 100005

def union(a, n, b, m):
    arr = [False] * MAX
    
    for i in a:
        arr[i] = True
    
    for i in b:
        arr[i] = True

    count = 0
    for i in arr:
        if i:
            count += 1

    return count

