plus, sub = map(int, input().split())
# plus = a+b(a>b)
# sub = a-b
flag = 0
for a in range(plus+1):
    for b in range(plus+1): #plus+1로 해야함. plus말고 
        if a-b == sub and a>=b and a+b==plus: # a>b말고 a>=b 하셈
            print(a,b)
            flag = 1
            break

if not flag:
    print(-1)