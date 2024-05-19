N=int(input())

def f(N):
    if N==1 or N==2:
        return N
    return N+f(N-2)

print(f(N))