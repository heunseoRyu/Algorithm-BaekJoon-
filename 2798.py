# 2798
# 브루트포스 알고리즘


n,m = map(int,input().split())
nums = list(map(int,input().split()))
nmax = 0
l = len(nums)

for i in range(l):
    for j in range(l):
        for k in range(l):
            if i < j and j < k:
                temp = nums[i] + nums[j] + nums[k]
                # print(i,j,k)
                # if temp > m: # 다음 거는 클수도 있잖슴.k바로 초기화시키면 안됨.break걸면 안됨.
                #     continue
                if nmax < temp and temp>m:
                    nmax = temp




print(nmax)

#
# # 더 쉽게 풀기
#
# n,m = map(int,input().split())
# arr = list(map(int,input().split()))
# result = 0
#
# for i in range(n):
#     for j in range(i+1,n): # 중복제거
#         for k in range(j+1,n): # 중복제거
#             if arr[i] + arr[j] + arr[k] > m: # 합 비교
#                 continue #중요!! break하면 안됨!! 오름차순 정렬 아니기 때문
#             else:
#                 result = max(result,arr[i]+arr[j]+arr[k]) # 값 비교 쉽게하는법