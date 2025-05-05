def add(x,y):
    num1=x+y
    num2=x*y
    return num1+num2

print(add(2,3))

#username and password are parameters
def login(username,password):
    if username=="admin" and password=="admin123":
        print('Login Success')
    else:
        print('Invalid Credentials')
        
uname=input('Enter Username: ')
pass1=input('Enter Password: ')
login(uname,pass1) #uname and pass1 are the arguments