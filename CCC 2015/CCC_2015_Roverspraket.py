a = input()
b = ""
vowels = "aeiou"
alpha = "abcdefghijklmnoprstuvwxyz"
for i in a:
    forward = 0
    backward = 0
    b += i
    pos = alpha.index(i)
    if not(i in vowels):
        #adding the vowel
        for j in alpha[pos:]:
            if j in vowels:
                break
            forward += 1            
        for k in alpha[pos::-1]:
            if k in vowels:
                break
            backward += 1            
        if pos > 19:
            b += "u"
        elif forward < backward:
            b += j
        else:
            b += k
        
        #adding the consonant
        if i == "z":
            b += "z"
        else:
            if alpha[pos+1] in vowels:
                b += alpha[pos+2]
            else:
                b += alpha[pos+1]
print(b)
