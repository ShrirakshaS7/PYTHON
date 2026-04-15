#5 WAP to display company name,location along with emp name, slary and their designation using class variables and object varaibles

class employee:
    company_name='pyspiders'
    location='basavangudi'
e1=employee()
e1.ename='smith'
e1.sal=98000
e1.job='analyst'

print(f'employee name:{e1.ename} , sal:{e1.sal} , job:{e1.job} , company name:{employee.company_name} and locatioon:{employee.location}')


#6 WAP to create class and access class variables without creating object

class emp():
    ename='smith'
    sal=98000
    deptno=10
    def display():
        print(f'employee name:{emp.ename}')
        print(f'employee sal:{emp.sal} and deptno:{emp.deptno}')
emp.display()


#7 WAP to create function inside class and to access class variables using object

class student:
    sname='smith'
    age=26

    def display(self):
        print(f'student name is:{s1.sname}')
        print(f'student age is:{s1.age}')
s1=student()
s1.display() 

#or

class student:
    sname='smith'
    age=26

    def display():
        print(f'student name is:{s1.sname}')
        print(f'student age is:{s1.age}')
s1=student()
student.display()

#8 WAP to perform employee annual salary

class employee:
    ename='smith'
    sal=45000

    def display(self):
        print(f'employee name:{self.ename}')
        print(f'employee monthly sal:{self.sal}')
        print(f'employee annual salary:{self.sal*12}')
e1=employee()
e1.display()


# using function as an object

class employee:
    dname='research'
    def details(self,ename,sal):
        self.ename=ename
        self.sal=sal
    
    def display(self):
        print(f'employee name:{self.ename}')
        print(f'employee department name:{self.dname}')
        print(f'employee salary:{self.sal}')
e1=employee()
e1.details('smith',9800)
e1.display()
e2=employee()
e2.details('king',8900)
e2.display()


#9 WAP to perform check balance,deposite and withdraw operartion

class bank:
    bank_name='BOB'

    def details(self,cname,balance):
        self.cname=cname
        self.balance=balance

    def deposit(self,amount):
        if amount>0:
            self.balance=self.balance+amount
            print(f'{amount} has been deposited')
            print(f'after deposit updated balance:{self.balance}')
        
        else:
            print(f'amount should be greater than zero')

    def withdraw(self,amount):
        if amount<self.balance:
            self.balance=self.balance-amount
            print(f'{amount} has been debited')
            print(f'after withdrawn updated balance:{self.balance}')
        else:
            print(f'insufficient balance')
    
    def display(self):
        print(f'customer name:{self.cname}')
        print(f'initial bank balance:{self.balance}')

c1=bank()
c1.details('smith',98000)
c1.display()
c1.deposit(1000)
c1.withdraw(3000)


#10 WAP  to create class to represent an emp management system
#1)the company name should be class varaible
#2) each emp has name and salary
#3) create method add salary to increase emp salary

class management:
    company_name='Google'

    def details(self,ename,sal):
        self.ename=ename
        self.sal=sal

    def add(self,amount):
        if amount>0:
            self.sal=self.sal+amount
            print(f'Salary after increment:{self.sal}')
        else:
            print(f'amount should be greater than zero')
    
    def display(self):
        print(f'Employee name:{self.ename}')
        print(f'Employee present salary:{self.sal}')

m1=management()
m1.details('smith',98000)
m1.display()
m1.add(1000)