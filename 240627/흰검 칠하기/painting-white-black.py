max_size=100*1000
n=int(input())
arr=[0]*(max_size*2+1)
cnt_b=[0]*(max_size*2+1)
cnt_w=[0]*(max_size*2+1)
curr=max_size

for i in range(n):
    x,d=input().split()
    x=int(x)
    while x>0:
        if d=='R':
            arr[curr]=1
            cnt_b[curr]+=1
            x-=1
            if x:
                curr+=1
        else:
            arr[curr]=-1
            cnt_w[curr]+=1
            x-=1
            if x:
                curr-=1

g,b,w=0,0,0

for j in range(len(arr)):
    if cnt_b[j]>=2 and cnt_w[j]>=2:
        g+=1
    elif arr[j]==1:
        b+=1
    elif arr[j]==-1:
        w+=1

print(w,b,g)