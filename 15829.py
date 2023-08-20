# hash 함수

L = int(input())
sent = input()
summ = 0
for i in range(L):
    # cnum = ord(sent[i]) - 96
    # temp = cnum * (31**i)
    # # print(cnum)
    # summ += temp
    summ += (ord(sent[i])-96) * (31**i) #이 정도는 한줄로
    # print(summ)

# 나눈 나머지를 통해 구함. 문자열의 종류는 무한하지만 출력 범위는 정해져있다.유한한 범위의 출력을 가져야 한다고 했으니까 적당히 큰 수 M으로 나눠주자
print(summ % 1234567891)

# # 뭔 진수마냥 사용
# 예제 1: abcde의 해시 값은 1 × 310 + 2 × 311 + 3 × 312 + 4 × 313 + 5 × 314 = 1 + 62 + 2883 + 119164 + 4617605 = 4739715이다.
#
# 예제 2: zzz의 해시 값은 26 × 310 + 26 × 311 + 26 × 312 = 26 + 806 + 24986 = 25818이다.