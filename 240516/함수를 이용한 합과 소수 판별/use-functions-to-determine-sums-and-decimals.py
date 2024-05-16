a,b=map(int,input().split())
ans=0

def IsSosu(num):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                return False
    return True

def sumAll(num):
    string=str(num)
    arr=[int(string[i]) for i in range(len(string))]
    sum_arr=sum(arr)
    return sum_arr%2==0
        
for i in range(a,b+1):
    if IsSosu(i) and sumAll(i):
        ans+=1

print(ans)