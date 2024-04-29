a,b=map(int,input().split())

def isThird(n):
    return n%3==0
def isTSN(n):
    a=str(n)
    return ("3" in a) or ("6" in a) or ("9" in a)

def Mnumber(n):
    return isThird(n) or isTSN(n)

cnt=0
for i in range(a,b+1):
    if Mnumber(i):
        cnt+=1
print(cnt)