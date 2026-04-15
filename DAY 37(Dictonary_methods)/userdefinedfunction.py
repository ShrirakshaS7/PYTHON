#User Defined Function
#Function without argument and without return

# WAP to display hello python using user defined function
def msg():
    print('hello python')
msg()

# WAP to print 1,2,3 numbers
def num():
    print(1)
    print(2)
    print(3)
num()

#Function with argument and without return

# WAP to print hello smith
def display(name):
    print(f'hello {name}')
display('smith')

#WAP to print square of given number
def square(num):
    res=num*num
    print(res)
square(3)

#Function without argument and with reurn

#1
def add():
    a=98
    b=89
    return a+b
# add()
print(add())

#Function with argument and with return
#1
def addition(x,y,z):
    return x+y+z
res=addition(10,20,30)
print(res)

#WAP to print cube of number
def cube(num):
    return num*num*num
cube(3)

#WAP to check given number is even or odd
def check(num):
    if num%2==0:
        return f'{num} is even number'
    else:
        return f'{num} is odd number'
check(98)