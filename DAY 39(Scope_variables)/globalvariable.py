#Scope of variables
#Global variable

#1
num=98
def display():
    print(f'accessing global variable inside function:{num}')
display()
print(f'accessing global variable outside function:{num}')

#2
num1=100
num2=200
def addition():
    res=num1+num2
    print(f'inside function:{res}')
addition()
outside=num1+num2
print(f'outside function:{outside}')

#3 Modify global variable
num=98
def display():
    num=num+3
    print(f'after addition number is:{num}')
display()
#UnboundLocalError

#or
num=98
def display():
    global num
    num=num+3
    print(f'after addition number is:{num}')
display()


