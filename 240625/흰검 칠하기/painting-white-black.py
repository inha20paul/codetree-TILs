# 명령 수
n=int(input())

dirr={
    'L':-1,
    'R':1
}

arr=[0]
curr=0

# 오류수정
bug=[]
cnt=0

for i in range(n):
    x,d=input().split()
    x=int(x)
    curr+=(x-1)*dirr[d]
    arr.append(curr)
    if x==1:
        bug.append(dirr[d])


size=max(arr)-min(arr)+1

gray=[0]*size
bw=[0]*size
g=0
for j in range(len(arr)-1):
    start,end=arr[j]-min(arr),arr[j+1]-min(arr)
    if start<end:
        for k in range(start,end+1):
            bw[k]=1
            gray[k]+=1
    elif start==end:
        if bug[cnt]==1:
            for k in range(start,end+1):
                bw[k]=1
                gray[k]+=1
        else:
            for k in range(end,start+1):
                bw[k]=0
                gray[k]+=10
        cnt+=1
    else:
        for k in range(end,start+1):
            bw[k]=0
            gray[k]+=10


for i in range(len(gray)):
    if gray[i]%10>=2 and gray[i]>=20:
        bw[i]=0
        g+=1

b=sum(bw)
w=size-b-g

print(g,b,w)
# print(gray)
# print(bw)
# print(arr)