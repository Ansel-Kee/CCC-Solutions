for i in range(1,16):
    # Accessing the input file
    if i < 10:
        f1 = open(f'j1.0{i}.in', "r")
        f2 = open(f'j1.0{i}.out', "r")
    else:
        f1 = open(f'j1.{i}.in', "r")
        f2 = open(f'j1.{i}.out', "r")
    lst = []
    for line in f1:
        lst.append(int(line.strip()))

    # Program code
    if lst[0] > 0:
        if lst[1] > 0:            
            a = '1'
        elif lst[1] < 0:
            a = '4'
    elif lst[0] < 0:
        if lst[1] > 0:
            a = '2'
        elif lst[1] < 0:
            a = '3'
    print(f'{i}:', a == f2.readline().strip())
    f1.close()
    f2.close()

