A=input()
B=input()
number1=""
number2=""

for i in range(len(A)):
    if A[i].isdigit():
        number1=number1+A[i]

for i in range(len(B)):
    if B[i].isdigit():
        number2=number2+B[i]

print(int(number1)+int(number2))