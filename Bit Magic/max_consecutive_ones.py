def foo(n):
    n = bin(n)[2:]
    count = 0
    mx_count = 0
    print(n)
    for i in n:
        if i == '0':
            mx_count = max(mx_count, count)
            count = 0
        else:
            count += 1
    mx_count = max(mx_count, count)
    return mx_count

n = int(input())
print(foo(n))