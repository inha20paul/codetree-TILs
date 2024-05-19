n=int(input())
arr=list(map(int,input().split()))
ans=0
def f(n):
    global ans
    if n==0:
        return
    if ans<=arr[n-1]:
        ans=arr[n-1]
    f(n-1)

f(n)
print(ans)