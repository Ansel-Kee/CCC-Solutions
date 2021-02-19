import itertools
for i in range(1, 29):
    # Accessing the input file
    print(f'Test case {i}: ')
    if i < 10:
        f1 = open(f'j5.0{i}.in', "r")
        f2 = open(f'j5.0{i}.out', "r")
    else:
        f1 = open(f'j5.{i}.in', "r")
        f2 = open(f'j5.{i}.out', "r")
    lst = []
    for line in f1:
        lst.append(list(map(int,line.strip().split(' '))))
    
    # Program code
    wood_combos = []
    wood_dict = dict.fromkeys(lst[1], 0)
    
    for j in lst[1]:
        wood_dict[j] += 1
        
    if len(wood_dict) == 1:        
        a = wood_dict[list(wood_dict.keys())[0]]//2
        b = 1
        
    else:
        wood_heights = {}
        wood_lengths = list(wood_dict.keys())
        combos = list(itertools.combinations_with_replacement(list(wood_dict.keys()), 2))
        for combo in combos:
            combo_count = min(wood_dict[combo[0]], wood_dict[combo[1]])
            if combo[0] == combo[1]:
                combo_count = wood_dict[combo[0]]//2
            combo_sum = sum(combo)
            if combo_sum in wood_heights:
                wood_heights[combo_sum] += combo_count
            else:
                wood_heights[combo_sum] = combo_count
        a = max(wood_heights.values())
        b = list(wood_heights.values()).count(a)

    print(f'{a} {b}' == f2.readline().strip())        
    print()
    

