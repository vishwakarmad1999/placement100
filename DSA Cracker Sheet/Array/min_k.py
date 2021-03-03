def kthSmallest(arr, l, r, k):
    if k > 0 and k <= r - l + 1:  
        pos = partition(arr, l, r)
        if pos - 1 == k - 1:
            return arr[pos - 1]
        elif pos - 1 > k - 1:
            return kthSmallest(arr, l, pos - 1, k)

        return kthSmallest(arr, pos + 1, r, k - pos + l - 1)
            

    return -1

def partition(arr, l, r):
    x = arr[r]
    i = l - 1

    for j in range(l, r):
        if arr[j] < x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i], arr[r] = arr[r], arr[i]
    return i 

n = int(input())
arr = list(map(int, input().split()))
k = int(input())

print(kthSmallest(arr, 0, n - 1, k))