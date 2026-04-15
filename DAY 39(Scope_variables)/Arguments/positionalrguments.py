#Positional Arguments

#1 WAP to add 2 numbers using positional arguments
def addition(num1,num2):
    print(f'addition of {num1} and {num2}:{num1+num2}')
addition(10,27)

#WAP to display ename and salary
def employee(ename,sal):
    print(f'employee name is : {ename}')
    print(f'employee salary is : {sal}')
employee('smith',98000)

#Keyword Argument

#1
def addition(a,b):
    res=a+b
    print(f'addition of {a} and {b} is:{res}')
addition(b=30,a=70)

#2
def emp(ename,sal):
    print(f'emp name:{ename}')
    print(f'emp salary:{sal}')
emp(ename='king',sal=18000)

#Default Argument

#1
def display(ename,sal=98000):
    print(f'emp name:{ename} and sal:{sal}')
display('martin')

#2
def display(ename,sal=98000):
    print(f'emp name:{ename} and sal:{sal}')
display('martin',sal=99000)

#Variable Argument
#1) Multiple postional arguments

#1
def addition(*args):
    print(f'addition of multiple numbers:{sum(args)}')
addition(10,20,30)

#2) Multiple keyword arguments

#1
def details(**data):
    for key, value in data.items():
        print(key,':',value)
details(ename='smith',sal=98000)
