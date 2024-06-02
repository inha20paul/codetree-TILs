n=int(input())
visited=[]
cnt=0
current=0
dirr={
    'R':1,
    'L':-1
}
for i in range(n):
    x,D=input().split()
    x=int(x)
    for j in range(x):
        if D=='R':
            visited.append(current)
            current+=dirr[D]
        else:
            current+=dirr[D]
            visited.append(current)


arr2=[0]*(max(visited)-min(visited)+1)
isVisit=[False]*(max(visited)-min(visited)+1)
num=min(visited)

for elem in visited:
    idx=elem-num
    if isVisit[idx]:
        arr2[idx]=1
    isVisit[idx]=True

print(sum(arr2))