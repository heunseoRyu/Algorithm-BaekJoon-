# 2292
# https://rightbellboy.tistory.com/122
# 힌트 : 규칙을 찾아라!
# 규칙찾는 수학 문제에서는 (구할 수 있다면) 직접 입력, 출력 값을 만들어 보는 것이 중요!!
# 문제의 특징에도 집중 , 힌트 : 육각형 -> 규칙이 6과 관련되지 않았을까?

# 알 수 있는 것 (리트)
# 2째 줄은 2개, 3째 줄은 3개(아무리 돌아가도 각자 줄만큼의 값을 받음.)
# 1. 육각형이 각 줄마다 얼마나 늘어나는지 구함.
# 1-1, 2-6 , 3-12 , 4-18

# 싸발
# def Calln(n,num):
#     if num==1:
#         print(1)
#         return
#     if n*6 >= num:
#         print(n+1)
#         return
#     Calln(n+1,num-n*6) # n +=1 , num-6
#     # n -> n-6 return

# 일단 특수한 거 아니면, while문 쓰자.
num = int(input())

n = 1   # n개
nmax = 1    # n째줄 최대값
add = 6     # 증감값 1-1, 2-6 , 3-12 , 4-18 -> 6씩 증가(중요)

while nmax < num: # num보다 작을때까지 반복, -> 크거나 같으면 반복안함.
    nmax += add # 먼저 더해야함. -> add초기값 6
    n += 1
    add += 6

    # num -= n * 6

print(n)


