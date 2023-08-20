# 미친 한번만에 100점 폼 미쳤쥬?
# 정렬할때 꿀팁 -> 입력받는 범위를 정해놓고 하기(빈리스트 금지!!) -> 이거 옛날에 코테랑도 비슷한듯..다름ㅎ
# sys 쓰기

# 단어 정렬
# 1. 길이가 짧은 것부터
# 2. 길이가 같으면 사전 순으로
# 중복된 단어는 하나만 남기고 제거
import sys
# 문자열 길이 50까지 정해놓고(리스트 50개 만들기) 1이면 1 리스트에 추가
N = int(sys.stdin.readline())
data = [[] for i in range(51)]

for i in range(N):
    temp = sys.stdin.readline().strip()
    L = len(temp)
    if temp not in data[L]:
        data[L].append(temp)


for i in range(1,51):
    if len(data[i]) != 0: # 리스트 비엇는지 확인!!
        data_sorted = sorted(data[i])
        # print(*data_sorted,) # 줄바꿈 안됨..
        for j in data_sorted:
            print(j)



