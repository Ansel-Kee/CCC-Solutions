from math import ceil
from collections import deque
import sys

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


M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
grid = deque(tuple(map(int, sys.stdin.readline().split())) for i in range(M))
print(escape(M, N, grid))
