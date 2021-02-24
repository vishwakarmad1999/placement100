def foo(s, n, curr="", i=0):
    if i == n:
        print(curr)
        return 

    foo(s, n, curr, i + 1)
    foo(s, n, curr + s[i], i + 1)

s = "abc"

foo(s, len(s))