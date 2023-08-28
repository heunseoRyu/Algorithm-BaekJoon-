import sys

N = int(sys.stdin.readline())
sangs = set(map(int,sys.stdin.readline().split())) # sangs 집합 활용
M = int(sys.stdin.readline())
cards = list(map(int,sys.stdin.readline().split()))

for i in cards:
    print(sangs.count(i),end=' ')
