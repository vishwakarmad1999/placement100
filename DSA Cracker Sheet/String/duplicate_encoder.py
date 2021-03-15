def duplicate_encode(word):
    #your code here
    word = word.lower()
    temp = [0] * 128
    ord_arr = list(map(ord, word))
    
    for i in ord_arr:
        temp[i] += 1
    
    final = ''
    
    for i in ord_arr:
        if temp[i] == 1:
            final += "("
        elif temp[i] > 1:
            final += ")"
            
    return final

