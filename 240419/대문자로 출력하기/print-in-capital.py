x=input()
lght=len(x)

for i in range(lght):
    if x[i].isalpha():
        print(x[i].upper(),end="")