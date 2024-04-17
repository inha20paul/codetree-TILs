A=input()
ascii_A=ord(A)
if ascii_A==122:
    ascii_A=97
else:
    ascii_A+=1

print(chr(ascii_A))