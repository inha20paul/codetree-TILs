N=int(input())
H=[-1]
ans=0
cnt=0
for i in range(N):
    h=int(input())
    H.append(h)
H.append(-1)


for i in range(1,len(H)):
    mx_idx=H.index(max(H))
    if H[mx_idx-1]!=0 and H[mx_idx+1]!=0:
        cnt+=1
    elif H[mx_idx-1]==0 and H[mx_idx+1]==0:
        cnt-=1
    # 방문 체크
    H[mx_idx]=0
    ans=max(cnt,ans)
    
print(ans)