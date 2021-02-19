for i in range(1,16):
    # Accessing the input file
    if i < 10:
        f1 = open(f'j2.0{i}.in', "r")
        f2 = open(f'j2.0{i}.out', "r")
    else:
        f1 = open(f'j2.{i}.in', "r")
        f2 = open(f'j2.{i}.out', "r")
    lst = []
    for line in f1:
        lst.append(int(line.strip()))

    # Program code
    shifty_sum = 0
    for j in range(lst[1]+1):
        shifty_sum += lst[0]
        lst[0] *= 10
    print(f'{i}:', shifty_sum == int(f2.readline().strip()))
    f1.close()
    f2.close()  
