# 야발 존나 공부하자

# n!

import sys

def pibo(N):
    tot = 1
    nums = []
    for i in range(1,N+1):
        tot *= i
        # nums.append(tot)
    return tot


N = int(sys.stdin.readline()) # 정수형
tot = str(pibo(N))
cnt = 0

# n!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.
for i in range(len(str(tot))-1,-1,-1):
    if tot[i] != '0':
        break
    else:
        cnt +=1

# for i in range(N-1,-1,-1):
#     str_numsI = str(nums[i])
#     if str_numsI[-1] == 0:
#         break
#     elif '0' in str_numsI:
#         cnt +=1

print(cnt)
