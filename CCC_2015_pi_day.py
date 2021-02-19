n = int(input())
k = int(input())
def pi_day(slices, people, least):
    print(slices, people)
    total = 0
    if people == 1 or slices == people:
        return 1
    else:
        largest = slices//people
        for j in range(least, largest+1):
            #print(slices-j, people-1, j, largest)
            print(total)
            total += pi_day(slices-j, people-1, j)
        print()
        return total
print(pi_day(n, k, 1))
'''
n = int(input())
k = int(input())
def pi_day(n, k, least):
    total = 0
    if k == 1 or n == k:
        return 1
    else:
        largest = n//k
        for i in range(least, largest+1):
            total += pi_day(n-i, k-1, i)
        return total
'''
