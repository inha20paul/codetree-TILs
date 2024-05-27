N=int(input())
H=[]
m=[]

for i in range(N):
    h=int(input())
    H.append(h)
    if h not in m:
        m.append(h)

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

for i in m:
    ans=max(ans,count_ice(i))

print(ans)