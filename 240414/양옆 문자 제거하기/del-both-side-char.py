# #1 슬라이싱
# s=input()
# s=s[0]+s[2:-2]+s[-1]
# print(s)

#2 리스트에 담아서 pop
arr=list(input())
arr.pop(1)
arr.pop(-2)
s=''.join(arr)
print(s)