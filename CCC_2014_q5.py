n = int(input())
lst1 = input().split()
lst2 = input().split()
def main(lst1, lst2):
    pairs = {}
    while lst1:
        a, b = lst1.pop(), lst2.pop()
        if a == b:
            return 'bad'
        try:
            if pairs[a] != b:
                return 'bad'
        except:
            pairs[b] = a
    return 'good'
print(main(lst1, lst2))
##for i in range(1,6):
##    f1 = open(f'j5.{i}a.in', 'r')
##    f2 = open(f'j5.{i}a.out', 'r')
##    n = f1.readline()
##    lst1 = f1.readline().split()
##    lst2 = f1.readline().split()
##    print(f2.readline().strip() == main(lst1, lst2))
##
##    f1 = open(f'j5.{i}b.in', 'r')
##    f2 = open(f'j5.{i}b.out', 'r')
##    n = f1.readline()
##    lst1 = f1.readline().split()
##    lst2 = f1.readline().split()
##    print(f2.readline().strip() == main(lst1, lst2))
