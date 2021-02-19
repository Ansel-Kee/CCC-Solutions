P = int(input())
N = int(input())
R = int(input())
i = 0
total = N
new = N*R
while total <= P: 
    total += new
    new *= R
    i += 1
print(i)
