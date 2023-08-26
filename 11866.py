import sys

N,K = map(int,sys.stdin.readline().split())
num_list = [i+1 for i in range(N)] # N-1번째 자리까지 있음.
sq = []

# 1칸에서 원을 따라서 K칸씩 이동하면서 도착한 칸의 수를 지운다.
p = 0
while True:
    if len(sq) == N:
        print("<",end='')
        print(*sq,sep=', ',end='>')
        break
    if p < K-1:
        temp = num_list[0]
        num_list.pop(0)
        num_list.append(temp)
        p +=1
    else:
        p = 0
        sq.append(num_list[0])
        num_list.pop(0)


