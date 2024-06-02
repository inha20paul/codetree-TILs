n=int(input())
curr=0
dirr={
    'R':1,
    'L':-1
}
arr=[]
for i in range(n):
    x,D=input().split()
    x=int(x)
    arr.append(curr)
    for j in range(x-1):
        curr+=dirr[D]
        arr.append(curr)

visit=[0]*(max(arr)-min(arr)+1)
for elem in arr:
    idx=elem-min(arr)
    visit[idx]+=1

w=0
b=0
g=0

for i in range(len(visit)):
    num=visit[i]
    if i>=-min(arr):
        if num>=4:
            g+=1
        elif num%2==1:
            b+=1
        elif num==2:
            w+=1
    else:
        if num>=4:
            g+=1
        elif num%2==1:
            w+=1
        elif num==2:
            b+=1
print(w,b,g)