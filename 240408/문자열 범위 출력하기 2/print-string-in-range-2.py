str_in=input()
n=int(input())

if len(str_in)<n:
    n=len(str_in)

for i in range(n):
    print(str_in[-i-1],end="")