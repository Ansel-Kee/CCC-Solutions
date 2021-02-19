from math import ceil
from collections import deque
from time import time

def coords(n, M, N):
    fact = set()
    for i in range(1, ceil(n**0.5)+1):
        if not n%i:
            b = n//i
            if i <= M and b <= N:
                fact.add((i-1, b-1))
            if b <= M and i <= N:
                fact.add((b-1, i-1))
    return deque(fact)

def escape(M, N, grid):
    pos = (0, 0)
    seen = {}
    junctions = deque()
    factors = {}

    if grid[0][0] == M*N:
        return 'yes'

    while True:
        
        num = grid[pos[0]][pos[1]]
        try:
            options = factors[num]
        except:
            options = coords(num, M, N)
            factors[num] = options
        
        seen[pos] = None

        try:
            pos = options.popleft()
            if not junctions and pos == (0, 0):
                return 'no'
            if options:
                junctions.append(options)
        except:
            pass

        try:
            seen[pos]
            if not junctions:
                return 'no'

            try:
                options = junctions.popleft()
                pos = options.popleft()
                if options:
                    junctions.append(options)
            except:
                pass
        except:
            pass
        
        if pos == (M-1, N-1):
            return 'yes'

##
##M = int(input())
##N = int(input())
##grid = deque(tuple(map(int, input().split())) for i in range(M))
##print(escape(M, N, grid))

test={1: range(1, 8), 2: range(1, 7), 3: range(1, 6),
      5: range(1, 5), 6: range(1, 7), 7: range(1, 8)}
##for i in test.keys():
##    for j in test[i]:
##        f = open(f'j5.0{i}.0{j}.in', 'r')
##        f1 = open(f'j5.0{i}.0{j}.out', 'r')
##        case = list([int(f.readline()), int(f.readline())])
##        case.append(tuple(tuple(map(int, f.readline().split())) for i in range(case[0])))
##        print(f'j5.0{i}.0{j}.in')
##        t = time()
##        result = escape(case[0], case[1], case[2])
##        print(time()-t)
##        ans = f1.read().strip()
##        print(ans in result)
##        #print(result)
##        print()
##        f.close(), f1.close()
f = open(f'j5.07.05.in', 'r')
f1 = open(f'j5.07.05.out', 'r')
case = list([int(f.readline()), int(f.readline())])
case.append(tuple(tuple(map(int, f.readline().split())) for i in range(case[0])))
t = time()
result = escape(case[0], case[1], case[2])
print(time()-t)
ans = f1.read().strip()
print(ans in result)
print()
f.close(), f1.close()
