# 이항계수(binomial coefficien) 알고리즘
# https://shoark7.github.io/programming/algorithm/3-ways-to-get-binomial-coefficients

# 전체 집합에서 원소의 개수 n에 대해 k개의 아이템을 뽑는 이항계수(조합의 수)는 다음과 같이 정의한다.
# 4개의 집합 중에서 2개를 순서없이 고르는 조합의 수는 4C2, 즉 6이 된다.

def factorial(n):
    avg = 1
    for i in range(2,n+1):
        avg *= i
    return avg

def bino_coef_factorial(n,k):
    return factorial(n)/(factorial(n-k)*factorial(k))

# 1. 팩토리얼 : 이항계수의 정의 이용하기
N,K = map(int,input().split())
print("%d" %bino_coef_factorial(N,K))


