#쉬어가는 김에 상덕버거 
tot = 0
sang = int(input())
jung = int(input())
ha = int(input())
coke = int(input())
cider = int(input())
burger = [sang,jung,ha]
drink = [coke,cider]
mintot = sang + coke - 50
for i in burger:
    for j in drink:
        tot = i + j -50
        if mintot > tot:
            mintot = tot

print(mintot)
