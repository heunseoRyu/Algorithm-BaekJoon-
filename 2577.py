#count numbers

a = int(input())
b = int(input())
c = int(input())
result = str(a*b*c)
for i in range(10):
    cnt = 0
    if str(i) in result:
       for j in range(len(result)):
           if str(i) == result[j]:
               cnt +=1
    print(cnt)