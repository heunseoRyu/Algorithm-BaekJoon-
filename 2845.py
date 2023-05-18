l,p = map(int,input().split())
nums = list(map(int,input().split()))

for i in nums:
    print(i-l*p,end=' ') #차이
