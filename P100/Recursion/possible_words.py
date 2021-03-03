d = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz'
}

def possible_words(arr, N, i=0, curr=""):
    if i == N:
        print(curr)
        return

    for ch in d[arr[i]]:
        possible_words(arr, N, i + 1, curr + ch)

possible_words([2, 3, 4], 3)