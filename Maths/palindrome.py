n = int(input())

rev = 0
org = n
while n != 0:
    rem = n % 10
    rev = rev * 10 + rem
    n //= 10

if (org == rev):
    print('Palindrome')
else:
    print('Not in Palindrome')