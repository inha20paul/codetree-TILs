n=int(input())
sums=0
for i in range(n):
    num=int(input())
    sums+=num

ans=str(sums)
ans=ans[1:]+ans[0]
print(ans)