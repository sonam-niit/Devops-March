def add(x,y):
    num1=x+y
    num2=x*y
    return num1+num2

print(add(2,3))

def login(username,password):
    if username=="admin" and password=="admin123":
        print('Login Success')
    else:
        print('Invalid Credentials')
        
uname=input('Enter Username: ')
password=input('Enter Password: ')
login(uname,password)