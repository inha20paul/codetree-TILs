N=int(input())

def f(N):
    if N==0:
        return
    print("* "*N)
    f(N-1)
    print("* "*N)

f(N)