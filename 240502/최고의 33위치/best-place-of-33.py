N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]
ans=[]
def add(r,c):
    num=0
    for i in range(-1,2):
        for j in range(-1,2):
            num+=arr[r+i][c+j]
    return num

for i in range(1,N-1):
    for j in range(1,N-1):
        ans.append(add(i,j))

print(max(ans))