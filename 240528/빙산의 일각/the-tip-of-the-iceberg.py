N=int(input())
H=[-1]
idx=[]
ans=0
cnt=0
for i in range(N):
    h=int(input())
    H.append(h)
    idx.append((h,i))
H.append(-1)

idx.sort(key=lambda x:x[0])

for tup in idx:
    mx_idx=tup[1]
    if H[mx_idx-1]!=0 and H[mx_idx+1]!=0:
        cnt+=1
    elif H[mx_idx-1]==0 and H[mx_idx+1]==0:
        cnt-=1
    # 방문 체크
    H[mx_idx]=0
    ans=max(cnt,ans)
    
print(ans)