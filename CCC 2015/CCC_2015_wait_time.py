a = int(input())
lst, lst_T, lst1 = [], [], []
#Creating a list of the inputs
for i in range(a):
    lst.append(input())
    
for j in range(len(lst)):
    count = -1
    if lst[j][0] == "R":
        for k in lst[j:]: #Finding the nearest sent/S
            if k[0] == "W":
                count += int(k[2:])-1
            else:
                count += 1
            if k[0] == "S" and k[2:] == lst[j][2:]:
                break
            
        #Adding the times to lst_T
        if not(("S " + lst[j][2:]) in lst[j:]):
            if lst[j][2:] in lst_T:
                lst_T[int(lst_T.index(lst[j][2:]))+1] = -1
            else:
                lst_T.append(lst[j][2:])
                lst_T.append(-1)
        elif lst[j][2:] in lst_T:
            lst_T[int(lst_T.index(lst[j][2:]))+1] += count
        else:
            lst_T.append(lst[j][2:])
            lst_T.append(count)
            
#Splitting into individual lists for sorting            
for m in range(1, len(lst_T), 2):
    lst1.append([lst_T[m-1], lst_T[m]])
    
lst1.sort() #Sorting by friend number

#Giving the Output
for n in lst1:
    print(n[0], n[1])
