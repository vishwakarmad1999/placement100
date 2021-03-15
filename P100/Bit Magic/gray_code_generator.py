n = int(input())

out = []
for i in range(2 ** n):
    temp = bin(i ^ i >> 1)[2:].rjust(n, '0')
    out.append(temp)

for i in out:
    print(i)
