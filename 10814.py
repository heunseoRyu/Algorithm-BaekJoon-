import sys

N = int(sys.stdin.readline())

old = [0 for i in range(201)] # 나이 1~200
names = [[] for i in range(201)] # 굳

for i in range(N):
    o,n = sys.stdin.readline().split()
    o = int(o)
    old[o] += 1
    names[o].append(n)

for i in range(1,201):
    if old[i] != 0:
        for j in range(old[i]):
            print(i,names[i][j])
