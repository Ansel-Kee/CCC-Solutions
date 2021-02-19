for i in range(1,16):
    # Accessing the input file
    if i < 10:
        f1 = open(f'j4.0{i}.in', "r")
        f2 = open(f'j4.0{i}.out', "r")
    else:
        f1 = open(f'j4.{i}.in', "r")
        f2 = open(f'j4.{i}.out', "r")
    n = int(f1.readline().strip())

    # Program code
    days = (n//(24*60))
    n = n%(24*60)
    time = 1200
    count = 0
    for j in range(1,n+1):
        shifty = True
        time += 1
        if time//100 == 12 and time%100 == 60:
            time = 100
        elif time%100 == 60:
            time = time + 100 - 60
        diff = int(str(time)[1]) - int(str(time)[0])        
        for k in range(2,len(str(time))):            
            if int(str(time)[k]) - int(str(time)[k-1]) != diff:
                shifty = False
        if shifty:
            count += 1
    count += days * 62
    print(f'{i}:', str(count) == f2.readline().strip())
    f1.close()
    f2.close()
