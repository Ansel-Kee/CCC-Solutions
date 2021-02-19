m, n, k = int(input()), int(input()), int(input())
grid = [['t' for i in range(n)] for j in range(m)]
total = 0
for i in range(k):
    direction, pos = input().split()
    pos = int(pos)-1
    if direction == 'R':
        grid[pos] = list(''.join(grid[pos]).swapcase())
    else:
        for i in grid:
            i[pos] = i[pos].swapcase()
print(sum(i.count('T') for i in grid))

