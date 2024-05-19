N=int(input())
ans=0
def f(N):
    global ans
    nxtN=0
    if N==1:
        return
    if N%2==0:
        nxtN=int(N/2)
    else:
        nxtN=int(N//3)
    ans+=1
    f(nxtN)

f(N)
print(ans)