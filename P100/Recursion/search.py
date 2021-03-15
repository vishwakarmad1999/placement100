def search(arr, l, r, k):
    if l > r:
        return False

    if arr[l] == k:
        return True

    if arr[r] == k:
        return True

    return search(arr, l + 1, r - 1, k)

arr = list(map(int, input().split()))
k = int(input())
print(search(arr, 0, len(arr) - 1, k))