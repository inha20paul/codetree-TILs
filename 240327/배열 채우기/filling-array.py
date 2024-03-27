arr = list(map(int,input().split()))
ans=[]

for i in arr:
    if i!=0:
        ans.append(i)
    elif i==0:
        break

for j in ans[::-1]:
    print(j,end=" ")