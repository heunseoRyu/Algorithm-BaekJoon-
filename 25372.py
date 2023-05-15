# 아씨 의외로 푸는데 오래 걸림..

n = int(input())
for i in range(n):
        key = input()
        if len(key) < 6 or len(key) > 9:
            print("no") # 여기 yes넣으면 어캄;;
        else:
            print("yes")
    # except ValueError :
    #     print("no")
    # as key 안해도됨.->두개 이상의 변수가 에러날때 오류번수 지정 안해도됨.
    # (물론 이 문제는 문자가 입력되서 no가 나오는 문제가 아님.)
    # 아무튼 ValueError는 잘못된 값을 int() 뭐 이런거에 넣어서 생기는 에러