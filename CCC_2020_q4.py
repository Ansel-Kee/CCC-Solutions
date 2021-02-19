from more_itertools import circular_shifts

T = input()
S = input()
yes = False
for i in circular_shifts(S):
    if ''.join(i) in T:
        yes = True
        break
print('yes') if yes else print('no')
