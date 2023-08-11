# 1차원 배열만 사용한다면 그저 간단한 계산식으로 되는 건 아닌지 고민해보자..

T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())  # H : 호텔 층 수 , W : 각 층 방의 수, N : 몇번째 손님
    # checkIn = [0 for i in range(W)]  # 각 호실마다 1칸씩은 무조건 이동 해야 하므로 기본값 : 1
    temp = 0
    ph = 0
    pw = 1
    for j in range(N):  # n명 반복
        if ph >= H:
            ph = 1 # 호 수 1더해지고 한칸 체크인하는거니까 ph=1 (중요!!!)
            pw += 1
        else:
            ph += 1
        # if checkIn[temp] >= H: # 같거나 크면으로 바꾼 이유, +1했을때 같아지기 때문에 +1하게되면 더 커짐.
        #
        #     temp += 1
        # else:
        #     checkIn[temp] += 1
        #     temp = 1 # 이거 했어야함..안했어 야발
        #     print(checkIn[temp])
    print(f'{ph}{pw:02d}')

