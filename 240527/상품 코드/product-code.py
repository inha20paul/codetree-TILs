prod,code=input().split()

class A:
    def __init__(self,prod='codetree',code=50):
        self.prod=prod
        self.code=code

p1=A()
p2=A(prod,code)

print(f'product {p1.code} is {p1.prod}')
print(f'product {p2.code} is {p2.prod}')