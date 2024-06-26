n=int(input())
size=100*1000
arr=[0]*(size*2+1)

curr=size

for i in range(n):
    x,d=input().split()
    x=int(x)
    while x>0:
        if d=='R':
            arr[curr]=1
            x-=1
            if x:
                curr+=1
        else:
            arr[curr]=-1
            x-=1
            if x:
                curr-=1

w,b=0,0

for num in arr:
    if num==1:
        b+=1
    elif num==-1:
        w+=1

print(w,b)