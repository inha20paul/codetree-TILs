uid,lv=input().split()

class A:
    # 생성자
    def __init__(self,uid='codetree',lv=10):
        self.uid=uid
        self.lv=lv

user_default=A()
user_in=A(uid,lv)

print(f'user {user_default.uid} lv {user_default.lv}')
print(f'user {user_in.uid} lv {user_in.lv}')