A=input()
arr=list(input())

for elem in arr:
    if len(A)>1:
        if elem=='L':
            A=A[1:]+A[0]
        elif elem=="R":
            A=A[-1]+A[:-1]

print(A)