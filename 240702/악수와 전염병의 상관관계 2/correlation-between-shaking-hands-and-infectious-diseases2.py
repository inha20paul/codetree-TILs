N,K,P,T=map(int,input().split())
arr=[0]*(N+1)
arr[P]=1
t_arr=[]
# 감염횟수
k_arr=[0]*(N+1)
k_arr[P]=K
for i in range(T):
    t,x,y=map(int,input().split())
    t_arr.append((t,x,y))

t_arr.sort(key=lambda x:x[0])

for t,x,y in t_arr:
    if k_arr[x]!=0 or k_arr[y]!=0:
        if k_arr[x]>0:
            k_arr[x]-=1
        else:
            if arr[x]==0:
                k_arr[x]=K
        if k_arr[y]>0:
            k_arr[y]-=1
        else:
            if arr[y]==0:
                k_arr[y]=K
        arr[x]=1
        arr[y]=1

for i in range(1,len(arr)):
    print(arr[i],end="")