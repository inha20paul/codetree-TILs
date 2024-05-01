string=input()
N=len(string)
# 시작점
x,y=0,0
# 북,동,남,서
dx=[0,1,0,-1]
dy=[1,0,-1,0]
# 초기방향: 북
direction=0
cnt=0
ans=-1

def atHome(x,y):
    return x==0 and y==0

for ways in string:
    if ways=='F':
        x+=dx[direction]
        y+=dy[direction]
    elif ways=='R':
        direction=(direction+1)%4
    elif ways=='L':
        direction=(direction-1)%4
    cnt+=1
    if atHome(x,y):
        ans=cnt
        break

print(ans)