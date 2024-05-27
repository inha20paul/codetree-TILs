prod,code=input().split()

class A:
    def __init__(self,prod='codetree',code=50):
        self.prod=prod
        self.code=code

p1=A()
p2=A(prod,code)

print(f'product {p1.prod} is {p1.code}')
print(f'product {p2.prod} is {p2.code}')