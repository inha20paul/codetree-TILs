n=int(input())
class person:
    def __init__(self,name,addr,city):
        self.name=name
        self.addr=addr
        self.city=city

arr=[]

for i in range(n):
    a,b,c=input().split()
    p = person(a,b,c)
    arr.append(p)

name_list=[p.name for p in arr]
name_list.sort()

ans_name=name_list[-1]

for p in arr:
    if p.name==ans_name:
        print(f"name {p.name}") 
        print(f"addr {p.addr}") 
        print(f"city {p.city}")