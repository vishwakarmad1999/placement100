def is_lucky(n, counter=2):
    if counter > n:
        return True
    if n % counter == 0:
        return False

    next_pos = n - n // counter
    return is_lucky(next_pos, counter + 1)

n = int(input())
print(is_lucky(n))