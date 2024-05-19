string=input()

def backward(string):
    bck=string[::-1]
    return bck

def isPalindrome(string):
    check=backward(string)
    return check==string

if isPalindrome(string):
    print("Yes")
else:
    print("No")