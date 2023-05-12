grade = input()
score =0

# if '+' in grade:
#     score += 0.3
# elif '-' in grade:
#     score -=1
#     score += 0.7

if 'A' in grade: # A- : 3.7이듯이 일의자리가 4가 아니었음
    score +=4
elif 'B' in grade:
    score +=3
elif 'C' in grade:
    score +=2
elif 'D' in grade:
    score +=1
else:
    score = 0

if '+' in grade: 
    score += 0.3
elif '-' in grade:
    score -=1 # 해결 : 이걸 밑에 두고 score -=1
    score += 0.7

print("%.1f" %score)

