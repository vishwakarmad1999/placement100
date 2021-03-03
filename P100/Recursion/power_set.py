def powerSet(s):
    p = []
    util(s, len(s), p)
    return sorted(p)
    
def util(s, n, p, i=0, curr=""):
    if i == n:
        p.append(curr)
        return
    
    util(s, n, p, i + 1, curr)
    util(s, n, p, i + 1, curr + s[i])

print(powerSet('abc'))