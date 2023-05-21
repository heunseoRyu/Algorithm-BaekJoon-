def opos(n):
    temp =''
    for i in range(2,-1,-1):
        temp += n[i]
    return temp
a,b = input().split()
a = opos(a)
b = opos(b)

if a >= b:
    print(a)
else:
    print(b)

