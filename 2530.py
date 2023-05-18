a,b,c = map(int,input().split())
d = int(input())
ds = d%60
d //= 60
dm = d%60
dh = d//60

a +=dh
b +=dm
c +=ds

if c>= 60:
    b += c // 60
    c %= 60
if b>= 60:
    a += b // 60
    b %= 60
if a>= 24:
    a %=24
# 이렇게 풀면 48이든 64든 1씩 더하고 한번만 빼고..대환장
# if c>= 60:
#     c -= 60
#     b +=1
# if b>= 60:
#     b -= 60
#     a +=1
# if a>= 24:
#     a -=24
print(a,b,c)
