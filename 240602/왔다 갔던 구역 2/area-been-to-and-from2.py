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
        current+=dirr[D]
        if current in visited:
            cnt+=1
        visited.append(current)


print(cnt)