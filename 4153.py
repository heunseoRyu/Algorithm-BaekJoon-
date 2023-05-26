while True:
    length = list(map(int, input().split()))
    length.sort() # sort() 괜히 줄인다고 리스트 뒤에 붙이지 마셈.
    if length[0] == 0:
        break
    a = length[0]
    b = length[1]
    c = length[2]

    if a + b > c and a ** 2 + b ** 2 == c ** 2:
        print("right")
    else:
        print("wrong")




