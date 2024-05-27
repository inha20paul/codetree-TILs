col,cod,sec=input().split()

class A:
    def __init__(col,cod,sec):
        self.col=col
        self.cod=cod
        self.sec=sec

ans=A(col,cod,sec)

print(f'code : {ans.col} ')
print(f'color : {ans.cod} ')
print(f'second : {ans.sec} ')