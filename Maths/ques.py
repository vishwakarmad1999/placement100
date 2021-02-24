import math

N = int(input())
states = input().split()
Q = int(input())
ch_states = input().split()

states = [int(i) for i in states]
ch_states = [int(i) for i in ch_states]


def toggle(x):
    if states[x - 1] == 0:
        states[x - 1] = 1
    else:
        states[x - 1] = 0

def state_check():
    sum_ = 0
    switch = 0
    standard = math.ceil(N / 2)
    # global change_count
    # change_count = 0
    temp = 0
    for y in states:
        sum_ += y
    if sum_ >= standard:
        switch = 1
    else:
        switch = 0
    global prev_switch
    if switch != prev_switch:
        temp = temp + 1
    prev_switch = switch
    return temp
        
in_sum_ = 0
in_standard = math.ceil(N / 2)
for i in states:
    in_sum_ += i
if in_sum_ >= in_standard:
    prev_switch = 1
else:
    prev_switch = 0

for i in ch_states:
    toggle(i)
    print(prev_switch)
    change_count = state_check()

print(change_count)
