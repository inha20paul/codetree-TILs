a,b=map(int,input().split())
ans=0

def IsOnjeonsu(num):
    if num%2==0:
        return False
    elif num%10==5:
        return False
    elif num%3==0 and num%9!=0:
        return False
    else:
        return True

def checkall(a,b):
    global ans
    for i in range(a,b+1):
        if IsOnjeonsu(i):
            ans+=1

checkall(a,b)
print(ans)