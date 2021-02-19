smile = ":-)"
sad = ":-("
count = 0
a = input()
for i in range(2, len(a)):
    if a[i-2]+a[i-1]+a[i] == smile:
        count += 1
    elif a[i-2]+a[i-1]+a[i] == sad:
        count -= 1
if count == 0:
    if smile in a:
        print("unsure")
    else:   
        print("none")
elif count > 0:
    print("happy")
elif count < 0:
    print("sad")
