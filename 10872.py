n = int(input())
tot = 1 # n=0이라면 n! = 1
for i in range(2,n+1):
    tot *=i


print(tot)