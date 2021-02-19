n = int(input())
a, d = 100, 100
for i in range(n):
    roll = list(map(int, input().split()))
    if roll[0] > roll[1]:
        d -= roll[0]
    elif roll[0] < roll[1]:
        a -= roll[1]
print(a)
print(d)
