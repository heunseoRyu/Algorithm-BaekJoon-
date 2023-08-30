import sys
# 공부 : https://chancoding.tistory.com/45
_ = int(sys.stdin.readline())
N = map(int,sys.stdin.readline().split())
_ = int(sys.stdin.readline())
M = map(int,sys.stdin.readline().split())
hashmap = {}

# 시간을 줄이기 위한 문제이므로 count()는 부적절
for n in N:
    if n in hashmap: # 해당 키가 있다면
        hashmap[n] +=1
    else: # 없다면
        hashmap[n] = 1

# 딕셔너리 : count()를 쓰지 않았고 , 또 시간복잡도도 최소화함.
print(' '.join(str(hashmap[m]) if m in hashmap else '0' for m in M))
# '문자열'.join(list) list 요소들 사이에 문자열 끼워넣은 문자열 반환
# 즉, 'list' 안에서 바로 리스트 만들어서 넣어줌.

# 어이없지만 젤 시간 짧은거
# from sys import stdin
# from collections import Counter
# _ = stdin.readline()
# N = stdin.readline().split()
# _ = stdin.readline()
# M = stdin.readline().split()
#
# C = Counter(N)
# print(' '.join(f'{C[m]}' if m in C else '0' for m in M))
#
# n의 요소들이 몇 개가 있는지를 알기위한 dictioinary를 알아내기 위한 노력을 하였습니다.
# 하지만, 파이썬에는 이미 해당 요소들이 몇개가 있는지 세어주는 함수가 존재합니다.
# from collections import Counter를 통해서 Counter 메서드를 가져옵니다.
# 리스트 N을 Counter에 넣으면 N의 요소들의 숫자를 센 Dictionary자료형이 출력됩니다.
# Counter(N)에 M의 요소가 있다면 해당 숫자를 출력하고 없으면 0을 출력하면 됩니다.

