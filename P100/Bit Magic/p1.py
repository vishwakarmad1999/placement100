t = int(input())
s = input()
n = len(s)

temp = []
i = 0
while i < n:
    if ord(s[i]) >= 48 and ord(s[i]) <= 57:
        if i + 3 < n and ord(s[i + 3]) >= 48 and ord(s[i + 3]) <= 57:
            temp.append((int(s[i]), int(s[i + 2] + s[i + 3])))
            i += 3
        elif i + 2 < n:
            temp.append((int(s[i]), int(s[i + 2])))
            i += 2
    i += 1

total = 0
for i in range(len(temp)):
    if i > 0:
        total += temp[i][1] - max(temp[i][0], temp[i - 1][1])
    else:
        total += temp[i][1] - temp[i][0]

print(total)