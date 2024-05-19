A=input()
B=input()

def f(A,B):
    if B in A:
        print(A.index(B))
    else:
        print(-1)

f(A,B)