class A():
    def __init__(self,code,point,time):
        self.code=code
        self.point=point
        self.time=time

code,point,time=input().split()
ans=A(code,point,time)

print(f'secret code : {code}')
print(f'meeting point : {point}')
print(f'time : {time}')