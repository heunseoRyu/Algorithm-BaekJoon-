nums = list(map(int, input().split()))
nums.sort()
s = nums[0]
b = nums[1]

for i in range(s, 0, -1): #일단 0으로 해야지 최대공약수가 1인경우를 커버침.
    if s % i == 0 and b % i == 0: 
        print(i)
        break

for i in range(b, s * b + 1, b): # b씩 증가하면 b의 배수가 되고  
    if i % s == 0:#b의 배수가 s의 배수인지
        print(i)
        break
    