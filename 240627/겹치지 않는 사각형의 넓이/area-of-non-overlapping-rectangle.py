arr=[[0]*2000 for _ in range(2000)]
for i in range(2):
    r1,c1,r2,c2=map(int,input().split())
    for j in range(r1,r2):
        for k in range(c1,c2):
            arr[j][k]=1

r1,c1,r2,c2=map(int,input().split())
for j in range(r1,r2):
        for k in range(c1,c2):
            arr[j][k]=0

s=0

for row in arr:
    for elem in row:
        s+=elem

print(s)