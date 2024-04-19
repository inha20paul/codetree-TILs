A=input()
B=input()
n=0
while True:
    if A==B or n>len(A):
        break
    else:
        A=A[-1]+A[:-1]
        n+=1

if n<=len(A):
    print(n)
else:
    print(-1)