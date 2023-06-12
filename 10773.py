k = int(input())
nums = []
# 후입선출
# 받은 값이 0이면 가장 최근에 들어온거 빼기
for i in range(k):
    n = int(input())
    if n==0:
        nums.pop(-1)
    else:
        nums.append(n)
print(sum(nums))
