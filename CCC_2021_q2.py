n = int(input())
highest = 0
win_name = ''
for i in range(n):
    name = input()
    bid = int(input())
    if bid > highest:
        highest = bid
        win_name = name
print(win_name)
