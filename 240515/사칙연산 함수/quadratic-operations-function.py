a,o,c=input().split()
a,c=int(a),int(c)

def opertion(a,c,o):
    if o=="+":
        print(f"{a} {o} {c} = {a+c}")
    elif o=="-":
        print(f"{a} {o} {c} = {a-c}")
    elif o=="/":
        print(f"{a} {o} {c} = {a//c}")
    elif o=="*":
        print(f"{a} {o} {c} = {a*c}")
    else:
        print("False")

opertion(a,c,o)