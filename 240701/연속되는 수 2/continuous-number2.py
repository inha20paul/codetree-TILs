N=int(input())
arr=[-1]
ans=[]
cnt=1
for i in range(N):
    num=int(input())
    # 비교
    if num==arr[-1]:
        cnt+=1
    else:
        cnt=1
    ans.append(cnt)
    arr.append(num)

print(max(ans))