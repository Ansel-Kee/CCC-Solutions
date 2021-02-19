for i in range(1,16):
    # Accessing the input file
    if i < 10:
        f1 = open(f'j3.0{i}.in', "r")
        f2 = open(f'j3.0{i}.out', "r")
    else:
        f1 = open(f'j3.{i}.in', "r")
        f2 = open(f'j3.{i}.out', "r")
    lst = []
    for line in f1:
        lst.append((line.strip().split(" ")))

    #Program code
    distance = abs(int(lst[0][0]) - int(lst[1][0])) + abs(int(lst[0][1]) - int(lst[1][1]))
    if distance == int(lst[2][0]) or (distance < int(lst[2][0]) and distance%2 == int(lst[2][0])%2):
        a = 'Y'
    else:
        a = 'N'
    print(f'{i}:', a == f2.readline().strip())
