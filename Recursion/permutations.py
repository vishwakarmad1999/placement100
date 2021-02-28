def permute(arr, n, i=0):
    if i == n - 1:
        print(''.join(arr))

    for j in range(i, n):
        arr[i], arr[j] = arr[j], arr[i]
        permute(arr, n, i + 1)
        arr[i], arr[j] = arr[j], arr[i]

s = input()
s = list(s)

permute(s, len(s))