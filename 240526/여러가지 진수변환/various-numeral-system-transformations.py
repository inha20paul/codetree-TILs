N,B=map(int,input().split())
arr=[]

while True:
    # 종료조건
    if N<B:
        arr.append(N)
        break
    arr.append(N%B)
    N=N//B

arr=arr[::-1]
for elem in arr:
    print(elem,end="")