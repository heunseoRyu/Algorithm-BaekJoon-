# A : 낮에 올라가는 높이 , B : 밤에 미끄러지는 높이 , V : 나무막대 길이
A,B,V = map(int,input().split())

# 뭔가 수식이 필요하다. 반복문말고 최대한 피하자 반복문은
if A>V:
    print(1)
else:
    # V-A : 마지막날 A만큼 가고 끝남.그거빼고, A-B : 하루에 가는 길이로 나누셈
    if (V-A)%(A-B) == 0: # 나눈 몫이 0이라면 -> A-B로 갈 수 있는 길이가 안남으면
        print((V-A)//(A-B)+1) # +1(낮에 이동하고 끝)
    else:
        print((V-A)//(A-B)+2) # +1(낮에 이동하고 끝) +1(A-B로 갈수있는 길이 남음.)