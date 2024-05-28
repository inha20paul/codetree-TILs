N=int(input())
H=[]
# m=[]
diff=[]
diff_cnt=[]

h=int(input())
H.append(h)

for i in range(N-1):
    h=int(input())
    H.append(h)
    if h-H[i]>0:
        if H[i] not in diff:
            diff.append(H[i])
            diff_cnt.append(0)
        else:
            idx=diff.index(H[i])
            diff_cnt[idx]+=1


    # if h not in m:
    #     m.append(h)

def count_ice(height):
    cnt=0
    switch=False
    arr=[max(0,elem-height) for elem in H]
    for i in range(N):
        if not switch and arr[i]!=0:
            cnt+=1
            switch=True
        elif arr[i]==0:
            switch=False
    return cnt

# ans=0

# for i in m:
#     ans=max(ans,count_ice(i))

# print(ans)
ans=0
ans_idx=0
for i in range(len(diff_cnt)):
    if diff_cnt[i]>ans:
        ans_idx=i

print(count_ice(diff[ans_idx]))