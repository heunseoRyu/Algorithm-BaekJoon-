while True:
    try: # 시도해봐라
        a,b = map(int,input().split())
        print(a+b)
    except EOFError as a: #만약 a에 입력값이 없는 에러가 난다면
        break
    except EOFError as b: # ''
        break

# EOFError에러 : https://blog.naver.com/PostView.nhn?blogId=redtaeung&logNo=221906225810
# 파이썬 예외처리 : https://wikidocs.net/30