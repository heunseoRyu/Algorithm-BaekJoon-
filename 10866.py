from sys import stdin
import math
N = int(stdin.readline())
stack = [0 for i in range(20002)]
front = 10001
rear = 10001

def isEmpty(f,r):
    return f == r

for i in range(N):
    code = stdin.readline()
    if "push_front" in code:
        code, X = code.split()
        # print(code)
        X = int(X)
        stack[front] = X
        front -= 1
        # print("push",stack[front],X)
    elif "push_back" in code:
        code, X = code.split()
        # print(code)
        X = int(X)
        stack[rear] = X
        rear += 1
    elif "pop_front" in code:
        if isEmpty(front,rear):
            print("-1")
        else:
            print(stack[front+1])
            front +=1
    elif "pop_back" in code:
        if isEmpty(front,rear):
            print("-1")
        else:
            print(stack[rear-1])
            rear -=1
    elif "size" in code:
        # print(front, rear)
        # if isEmpty(front,rear):
        #     print("-1")
        # else:
            print(abs(front - rear))
    elif "empty" in code:
        print(int(isEmpty(front,rear)))
    elif "front" in code:
        if isEmpty(front,rear):
            print(-1)
        else:
            print(stack[front+1])
    elif "back" in code:
        if isEmpty(front,rear):
            print(-1)
        else:
            print(stack[rear-1])
    print(code , stack[front:rear+1],sep='이랑')


print(rear,front,stack[front:rear+1])
