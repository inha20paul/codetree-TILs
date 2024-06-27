n=int(input())
isBlue=0
arr=[[0]*201  for _ in range(201)]
for i in range(n):
    x1,y1,x2,y2=map(int,input().split())
    x1+=100
    x2+=100
    y1+=100
    y2+=100
    for j in range(x1,x2):
        for k in range(y1,y2):
            if isBlue: #파랑
                arr[j][k]=1
            else: #빨강
                arr[j][k]=2
    isBlue=(isBlue+1)%2
    
blue=0

for i in range(201):
    for j in range(201):
        if arr[i][j]==1:
            blue+=1

print(blue)