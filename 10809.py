sent = input()
# 122 ~ 97
exist = []
for i in range(1,27):
    if chr(i+96) in sent:
        for j in range(len(sent)):
            if sent[j] == chr(i+96):
                exist.append(j)
                break
    else:
        exist.append(-1)

for i in range(26):
    print(exist[i],end=' ')