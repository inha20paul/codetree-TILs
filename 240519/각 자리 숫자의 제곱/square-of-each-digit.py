N=int(input())

def f(N):
    if N<1:
        return 0
    return (N%10)**2 + f(int(N//10))

print(f(N))