N=int(input())
H=[int(input()) for _ in range(N)]
H=[elem-min(H)+1 for elem in H]
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

ans=0

for i in range(1,max(H)+1):
    ans=max(ans,count_ice(i))

print(ans)