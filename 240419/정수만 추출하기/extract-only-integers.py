a,b=input().split()

def numbering(string):
    num=''
    for i in range(len(string)):
        if string[i].isdigit():
            num=num+string[i]
        else:
            break
    return int(num)

print(numbering(a)+numbering(b))