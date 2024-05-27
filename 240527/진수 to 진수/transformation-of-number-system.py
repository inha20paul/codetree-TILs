a,b=map(int,input().split())
n=input()

def a2deci(a,n):
    n=n[::-1]
    num=0
    for i in range(len(n)):
        num+=(a**i)*int(n[i])
    return num

def deci2b(b,n):
    arr=[]
    while True:
        if n<b:
            arr.append(n)
            break
        arr.append(n%b)
        n=n//b
    arr=[str(i) for i in arr[::-1]]
    return ''.join(arr)

deci=a2deci(a,n)
ans=deci2b(b,deci)
print(ans)