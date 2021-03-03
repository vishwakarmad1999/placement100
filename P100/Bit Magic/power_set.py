def bin_to_str(b, s):
    b = b[2:].rjust(len(s), '0')
    res = ''
    for i in range(len(s)):
        if b[i] == '1':
            res += s[i]
    
    return res

def power_set(s):
    output = []
    for i in range(2 ** len(s)):
        output.append(bin_to_str(bin(i), s))

    return output      

s = input()
res = power_set(s)
print(len(res))