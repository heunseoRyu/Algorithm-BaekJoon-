# 부녀회장이 될테야

# 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.
# 0층 1      2      3       4       5
# 1층 1(0+1) 3(1+2) 6(3+3) 10(6+4) 15(10+5)



T = int(input()) # test case 수
for i in range(T):
    k = int(input()) # k층
    n = int(input()) # n호
    nums = [i for i in range(n+1) ] #0층 채우기(n호만큼)
    for j in range(1,k+1): # k층 만큼 반복
        for t in range(1,n+1): # 1호~n호까지 반복
            nums[t] = nums[t-1] + nums[t] # 이전 호수에 사는 사람 수 + 아래층에 사는 사람 수(쓸때없이 temp 쓰는 버릇 고치기)


    print(nums[-1])