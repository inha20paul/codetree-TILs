N=int(input())

def f1(N):
    # 종료 조건
    if N==0:
        return
    print(N,end=" ")
    f1(N-1)

def f2(N):
    # 종료 조건
    if N==0:
        return
    f2(N-1)
    print(N,end=" ")

f2(N)
print()
f1(N)