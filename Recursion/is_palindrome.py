def util(s, r, l=0):
    if s[r] != s[l]:
        return False
    elif l >= r:
        return True

    return util(s, r - 1, l + 1)

s = input()
print(util(s, len(s) - 1))