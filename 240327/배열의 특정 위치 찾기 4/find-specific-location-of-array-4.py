arr = list(map(int,input().split()))
ans=[]

for i in arr:
    if i==0:
        break
    elif i%2==0:
        ans.append(i)

print(f"{len(ans)} {sum(ans)}")