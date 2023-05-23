# 백준에서 막 오차 어쩌구 하는데 다 그 매길때 오차범위를 말하는 것이고 상대오차,절대오차가 있기 때문에 아무튼 
# 소수점 땜에 답이 달라도 쑤셔넣고 보기 


def crazsum(score,m,n):
    tot = 0
    for i in score:
        tot += (i/m)*100
    return tot/n
n = int(input())
score = list(map(int,input().split()))
nmax = score[0]
for i in score:
    if nmax < i:
        nmax = i

print(crazsum(score,nmax,n))

