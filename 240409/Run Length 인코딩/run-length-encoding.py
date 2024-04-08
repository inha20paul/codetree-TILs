str_A=input()
str_A=str_A+'0'
lgth=len(str_A)
cnt=1
ans=''

for i in range(lgth-1):
    if cnt==1:
            ans=ans+str_A[i]
    if str_A[i]==str_A[i+1]:
        cnt+=1
    else:
        ans=ans+str(cnt)
        cnt=1

print(len(ans))
print(ans)