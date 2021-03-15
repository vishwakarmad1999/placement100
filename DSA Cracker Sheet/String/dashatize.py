from math import floor

def dashatize(n):
    if n is not None:
        if n < 0:
            return -n
        
        if floor(n) != n:
            return ''

        if n < 10:
            return str(n)
        
        temp = ''
        
        for i in str(n):
            if int(i) % 2 != 0:
                if not temp:
                    temp = i + '-'
                elif temp[-1] == '-':
                    temp += i + '-'
                else:
                    temp += '-' + i + '-'
            else:
                temp += i
                
        if temp[-1] == '-':
            return temp[:-1]
        return temp
    else:
        return 'None'
        
n = int(input())
print(dashatize(n))