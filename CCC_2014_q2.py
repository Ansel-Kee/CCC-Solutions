v = int(input())
votes = input()
a = votes.count('A')
b = votes.count('B')
if a > b:
    print('A')
elif a < b:
    print('B')
else:
    print('Tie')
