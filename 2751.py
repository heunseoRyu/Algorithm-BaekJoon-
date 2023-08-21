import sys


N = int(sys.stdin.readline())
nums = [[0 for i in range(1000001)] for i in range(2)]

for i in range(N):
    t = int(sys.stdin.readline().strip())
    if t<0:
        nums[0][-t] = 1 #ㅇㄴ 마이너스 써야지 미친 뒤에서 부터 넣고 있었네
    elif t==0:
        nums.append(t)
    else:
        nums[1][t] = 1


for i in range(1000000,0,-1):
    if nums[0][i] == 0:
        continue
    print(-i)

if len(nums) == 3:
    print(0)

for i in range(1,1000001):
    if nums[1][i] == 0:
        continue
    print(i)