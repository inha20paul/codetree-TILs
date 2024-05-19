A=input()

def f(A):
    start=A[0]
    lght=len(A)
    if lght==1:
        return True
    for i in range(1,lght):
        if A[i]!=start:
            return True
    return False

if f(A):
    print("Yes")
else:
    print("No")