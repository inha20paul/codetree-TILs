N=int(input())

def pivo(N):
    if N==1 or N==2:
        return 1
    return pivo(N-1)+pivo(N-2)

print(pivo(N))