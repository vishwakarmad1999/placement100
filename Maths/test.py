n = int(input())
arr = list(map(int, input().split()))

pfix = [arr[0]]
for i in range(1, len(arr)):
    pfix.append(arr[i] + pfix[i - 1])

q = int(input())
queries = list(map(int, input().split()))

output = []
for i in range(q):
    temp = queries[i] - 1

    total = arr[temp]
    j = temp + 1
    while j < n:
        if temp != 0:
            total += pfix[j] - pfix[temp - 1]
        else:
            total += pfix[j]
        j += 1

    output.append(total)

for i in output:
    print(i, end=' ')
