bigx, bigy, smallx, smally = 0, 0, 100, 100
for i in range(int(input())):
    c = list(map(int, input().split(',')))
    if c[0] > bigx:
        bigx = c[0]
    if c[1] > bigy:
        bigy = c[1]
    if c[0] < smallx:
        smallx = c[0]
    if c[1] < smally:
        smally = c[1]
print(f'{smallx-1}, {smally-1}')
print(f'{bigx+1}, {bigy+1}')
