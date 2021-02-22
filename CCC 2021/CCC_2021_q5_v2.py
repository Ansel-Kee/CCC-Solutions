import sys
m, n, k = int(sys.stdin.readline()), int(sys.stdin.readline()), int(sys.stdin.readline())
moves = {}

for i in range(k):
    move = tuple(sys.stdin.readline().split())
    try:
        moves[move] += 1
    except:
        moves[move] = 1


ans={'R':0, 'C':0}
for j in moves:
    if moves[j]%2:
        ans[j[0]] += 1
R_count, C_count = ans['R'], ans['C']          
print(R_count*n + C_count*m - R_count*C_count*2)
