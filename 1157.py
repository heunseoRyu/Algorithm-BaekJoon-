c = input()
c = c.upper()
flag = 0
maxc = 0
cnts = []
alpha = []
# 딕셔너리 안쓰고 품!!
for i in c:
    if i in alpha: #temp는 i가 아니라는 조건이 붙어야함!!왜냐면 temp=z인데 다음 글자도 z일수 있으니까
        continue
    # 시간초과를 고치기 위한 노력들
    cnt = c.count(i)
    cnts.append(cnt)
    alpha.append(i)
    if maxc < cnt:
        maxc = cnt
        temp = i



if cnts.count(max(cnts)) >=2 :
    print("?")
else:
    print(temp)


    #     flag = 0 # 값이 갱신되었으므로 flag 초기화
    # # 만약 현재 cnt가 maxc랑 같다면 flag = 1
    # elif maxc == cnt:
    #     flag = 1
# 야발 힘들었다.