stud=[]
for i in range(5):
    name,h,w=input().split()
    h=int(h)
    w=float(w)
    stud.append((name,h,w))

stud.sort(key=lambda x:x[0])

print("name")
for name,h,w in stud:
    print(f'{name} {h} {w:.1f}')
print()

stud.sort(key=lambda x:-x[1])

print("height")
for name,h,w in stud:
    print(f'{name} {h} {w:.1f}')