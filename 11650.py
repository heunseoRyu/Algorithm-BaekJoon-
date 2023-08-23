# 좌표 정렬하기
import sys

N = int(sys.stdin.readline())
xs = [[0 for j in range(100001)] for i in range(2)]
ys = [[[] for j in range(100001)] for i in range(2)]
Xzero = []
for i in range(N):
    x,y = map(int, sys.stdin.readline().split())
    if x<0:
        xs[0][-x] +=1
        ys[0][-x].append(y)
    elif x>0:
        xs[1][x] +=1
        ys[1][x].append(y)
    else:
        Xzero.append(y)

ys = ys.sort()

for i in range(100000,0,-1):
    if xs[0][i] != 0:
        ys[0][i].sort() # ys 리스트를 정렬
        for j in ys[0][i]:
            print(-i,j)

if len(Xzero) > 3: # Xzero 리스트 처리 추가
    for j in Xzero:
        print(0,j)

for i in range(1,100001):
    if xs[1][i] != 0:
        ys[1][i].sort() # ys리스트를 정렬
        for j in ys[1][i]:
            print(i,j)
