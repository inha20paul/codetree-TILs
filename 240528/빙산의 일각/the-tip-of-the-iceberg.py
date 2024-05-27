N=int(input())
H=[int(input()) for _ in range(N)]

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

for i in H:
    ans=max(ans,count_ice(i))

print(ans)