x=input()

for i in range(len(x)):
    if 'a'<=x[i]<='z':
        print(x[i].upper(),end="")
    else:
        print(x[i].lower(),end="")