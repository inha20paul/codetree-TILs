x=input()
lght=len(x)

for i in range(lght):
    if x[i].isalpha():
        if 'a'<=x[i] and x[i]<='z':
            cap=ord('A')-ord('a')
            ascii=ord(x[i])+cap
            print(chr(ascii),end="")
        else:
            print(x[i],end="")