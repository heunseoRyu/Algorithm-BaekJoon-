# sys(여러줄 입력받을때 시간초과 방지) : https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline
# https://yoonsang-it.tistory.com/49
import sys

n = int(sys.stdin.readline())
nums = [0] * 10001 # n개의 줄에는 0~ 10000 중의 수가 주어진다.
'''
for문 속에서 append를 사용하게 되면 메모리 재할당이 이루어져서 메모리를 효율적으로 사용못한다.
일반적으로 입력값이 크지않은 경우에는 상관없지만 이렇게 입력값이 극한으로 많이 주어질 때에는
메모리를 좀 더 효율적으로 관리해야한다.
그래서 입력값이 10000개 까지 주어질 수 있으니 10000개 만큼의 리스트를 만들어 놓는다.
'''

# 버블정렬 : https://velog.io/@hwamoc/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%A0%95%EB%A0%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-1-%EB%B2%84%EB%B8%94-%EC%A0%95%EB%A0%AC-%EC%84%A0%ED%83%9D-%EC%A0%95%EB%A0%AC-%EC%82%BD%EC%9E%85-%EC%A0%95%EB%A0%AC
# for i in range(n-1,0,-1): # 1)
#     for i in range(0,i):
#         if nums[i] > nums[i+1]:
#             temp = nums[i+1]
#             nums[i+1] = nums[i]
#             nums[i] = temp
# snums = sorted(nums) # 2)

for i in range(n): # 3)
    nums[int(sys.stdin.readline())] += 1



for i in range(10001):
    if nums[i] != 0:
        for j in range(nums[i]):
            print(i)