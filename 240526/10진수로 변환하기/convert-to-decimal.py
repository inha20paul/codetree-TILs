binary=input()
binary=binary[::-1]
deci=0

for i in range(len(binary)):
    deci+=(2**i)*int(binary[i])

print(deci)