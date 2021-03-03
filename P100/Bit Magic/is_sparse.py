def is_sparse(n):
    # s = bin(n)[2:]
    
    # for i in range(len(s) - 1):
    #     if s[i] == '1' and s[i] == s[i + 1]:
    #         return False
    # return True
    return not bool(n & n >> 1)

n = int(input())
print(is_sparse(n))