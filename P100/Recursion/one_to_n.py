'''
Non Tail Recursive Method
def foo(n):
    if n == 0:
        return
    
    foo(n - 1)
    print(n)
'''

# Tail Recursive Method
def foo(n, k=1):
    if k == n + 1:
        return

    print(k)
    foo(n, k + 1)

n = int(input())
foo(n)

