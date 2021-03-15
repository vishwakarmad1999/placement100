arr = list(map(int, input().split()))
n = len(arr)
d = int(input()) % n

arr[:d] = arr[:d][::-1] # Reverse first d elements
arr[d:] = arr[d:][::-1] # Reverse rest of the n - d elements
arr = arr[::-1] # Reverse the complete array

print(arr) # You got the result