#소수찾기
def is_Prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True

n = int(input())

nums = list(map(int,input().split()))
cnt = 0
for i in nums:
    if i == 1:
        continue
    if is_Prime(i):
        cnt +=1

print(cnt)