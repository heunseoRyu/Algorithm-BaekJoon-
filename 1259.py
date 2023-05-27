def rev(c):
    nc = ''
    for i in range(len(c)-1,-1,-1):
        nc += c[i]
    return nc


while True:
    c = input()
    if c=='0':
        break
    if c==rev(c):
        print("yes")
    else:
        print("no")