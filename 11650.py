# 좌표 정렬하기
import sys

N = int(sys.stdin.readline())
# xs = [[0 for j in range(100001)] for i in range(2)]
# ys = [[[] for _ in range(100001)] for _ in range(2)]
xs = [[[] for _ in range(100001)] for _ in range(2)] # 걍 하나에 통합
Xzero = []

for i in range(N):
    x,y = map(int, sys.stdin.readline().split())
    if x<0:
        xs[0][-x].append(y)
        # print(xs[0][-x])
        # print(ys[0][-x])
    elif x > 0:
        xs[1][x].append(y)
        # print(xs[0][-x])
        # ys[1][x].append(y)
        # print(ys[0][-x])
    else:
        Xzero.append(y)

# print(ys)
# print(xs)

for i in range(100000,0,-1):
    if xs[0][i] != 0:
        xs[0][i].sort() # ys 리스트를 정렬
        for j in xs[0][i]:
            print(-i,j)

Xzero.sort()
for i in Xzero:
    print(0,i)

for i in range(1,100001):
    if xs[1][i] != 0:
        xs[1][i].sort() # ys리스트를 정렬
        for j in xs[1][i]:
            print(i,j)

