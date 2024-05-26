n=int(input())
digits=[]

while True:
    if n<2:
        digits.append(n)
        break
    digits.append(n%2)
    n=n//2
digits=digits[::-1]

for elem in digits:
    print(elem,end="")