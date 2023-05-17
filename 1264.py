while True:
    tot = 0
    sent = input()
    if sent == '#':
        break
    for i in sent:
        if i=='a' or i=='A':
            tot +=1
        elif i=='e' or i=='E':
            tot +=1
        elif i=='i'or i=='I':
            tot +=1
        elif i=='o' or i=='O':
            tot +=1
        elif i=='u'or i=='U':
            tot +=1
    print(tot)
#모음수 세기