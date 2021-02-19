m, n, k = int(input()), int(input()), int(input())
moves = {}

for i in range(k):
    move = tuple(input().split())
    try:
        moves[move] += 1
    except:
        moves[move] = 1

R_count, C_count = 0, 0

for j in moves:
    if moves[j]%2:
        if j[0] == 'R':
            R_count += 1
        else:
            C_count += 1
            
print(R_count*n + C_count*m - R_count*C_count*2)
