n=int(input())
students=[]
for i in range(n):
    name,a,b,c=input().split()
    students.append((name,int(a),int(b),int(c)))

students.sort(key=lambda x:x[1]+x[2]+x[3])

for name,a,b,c in students:
    print(name,a,b,c)