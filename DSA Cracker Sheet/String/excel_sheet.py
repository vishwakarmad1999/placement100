def column_name(n):
    s = ''
    while n > 0:
        if n % 26 == 0:
            s += 'Z'
            n = n // 26 - 1
        else:
            s += chr(65 + (n % 26 - 1))
            n = n // 26

    return s[::-1]

n = int(input())
print(column_name(n))