A=input()
B=input()

while True:
    if B in A:
        idx=A.index(B)
        lgth=len(B)
        A=A[:idx]+A[idx+lgth:]
    else:
        break

print(A)