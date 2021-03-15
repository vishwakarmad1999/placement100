def f(n):
    if n <= 3:
        return n - 1

    total = 0
    for i in range(1, n):
        if i == n - 2:
            continue
        total += i

    return total + 1

n = int(input())
print(f(n))
