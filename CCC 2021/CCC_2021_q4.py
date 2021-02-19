books = list(input())
n = 0
try:
    first_M= books.index('M')
except:
    first_M = None
try:
    first_L= books.index('L')
    first_S= books.index('S')

    L_pos = reversed(tuple(i for i in range(len(books)) if books[i] == 'L'))
    skip = False
    for i in L_pos:
        
        if first_M is None:
            pos = first_S
            s=True
        elif first_S > first_M:
            pos = first_M
            s=False
        else:
            pos = first_S
            s = True
        if i > pos:
            books[i], books[pos] = books[pos], books[i]
            if first_M is not None:
                first_M= books.index('M')
            if s:
                first_S= books.index('S')
            n+=1
            if books == sorted(books):
                skip = True
                break
    
    if first_M != None and not skip:
        M_pos = reversed(tuple(i for i in range(len(books)) if books[i] == 'M'))
        for i in M_pos:
            if i > first_S:
                books[i], books[first_S] = books[first_S], books[i]
                first_S = books.index('S')
                n+=1
            if books == sorted(books):
                break      
    print(n)
except:
    print(0)



