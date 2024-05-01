N=int(input())
cnt=0
x,y=0,0
mapping={
    'E':0,
    'W':1,
    'S':2,
    'N':3
}
# 동,서,남,북
dx=[1,-1,0,0]
dy=[0,0,-1,1]

def atHome(x,y):
    return x==0 and y==0

homeIn=False

for i in range(N):
    way,num=input().split()
    num=int(num)
    direction=mapping[way]
    for j in range(num):
        x+=dx[direction]
        y+=dy[direction]
        cnt+=1
        if atHome(x,y):
            print(cnt)
            homeIn=True

if not homeIn:
    print(-1)