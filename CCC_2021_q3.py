n = input()
last = ''
while n != '99999':
    out = ''
    add = int(n[0])+int(n[1])
    if add == 0:
        out += f'{last} '
    elif add%2:
        out += 'left '
        last = 'left '
    else:
        out += 'right '
        last = 'right '
    out += n[2:]
    print(out)
    n = input()
