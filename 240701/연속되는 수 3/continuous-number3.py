N=int(input())
arr=[0]
ans=[]
cnt=1
for i in range(N):
    num=int(input())
    check_num=num*arr[-1]
    if check_num>0: # 곱했을때 부호 양수 (부호 같을때)
        cnt+=1
    elif check_num<0: # 부호 음수 (연속 X)
        cnt=1
    arr.append(num)
    ans.append(cnt)


print(max(ans))