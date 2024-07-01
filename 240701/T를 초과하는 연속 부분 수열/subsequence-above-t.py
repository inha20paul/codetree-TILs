n,t=map(int,input().split())
arr=list(map(int,input().split()))
arr.append(0)
ans=[]
cnt=0
for i in range(n):
    if arr[i]>t:
        cnt+=1
    else:
        cnt=0
    ans.append(cnt)
    if arr[i+1]<t:
        cnt=0


print(max(ans))