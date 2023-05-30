
#생성자인지 계산하는 함수
def is_produce(m,n):
    temp = m
    m = int(m)
    for j in temp: #계산
        m += int(j)
    if m == n: #맞다면 
        return temp
    else: #아니라면
        return False

n = int(input()) #분해합

for i in range(n//2,n+1): #일단 값이 너무 작으면 더해도 소용이 없을 것.최소 중간이상
    m = str(i)
    temp = is_produce(m, n) #생성자인지 계산 
    # 생성자라면 
    if temp:
        print(temp) 
        break
#생성자가 없다면
else: 
    print(0)
