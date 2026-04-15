# Constructor Chaining

# eg 1 without using super keyword
class parent:
    def __init__(self):
        print('this is parent class')
class child(parent):
    def __init__(self):
        print('this is child class')
obi=child()

# eg 2 using super keyword
class parent:
    def __init__(self):
        print('this is parent class')
class child(parent):
    def __init__(self):
        super().__init__()
        print('this is child class')
obj=child()

#3 WAP to display student name,age and subject using single level inheritance and constructor chaining
class college:
    def __init__(self,sname,age):
        self.sname=sname
        self.age=age
class student(college):
    def __init__(self, sname, age,subject):
        super().__init__(sname, age)
        self.subject=subject
    def display(self):
        print(f'student name:{self.sname}')
        print(f'age:{self.age}')
        print(f'subject:{self.subject}')
s1=student('smith',26,'python')
s1.display()

#4 WAP to display initial bank balance, customer name, acctno, bankname and perform deposoit and withdraw operation using single level inhertance (using constructor chaining)
class bank:
    def __init__(self, bname,cname):
        self.bname=bname
        self.cname=cname
    def details(self):
        print(f'bank name:{self.bname}')
        print(f'customer name:{self.cname}')
class account(bank):
    def __init__(self, bname, cname,balance, acctno):
        super().__init__(bname, cname)
        self.balance=balance
        self.acctno=acctno
    def display(self):
        print(f'initial bank balance:{self.balance}')
        print(f'customer acctno:{self.acctno}')
    def deposit(self, amount):
        if amount>0:
            self.balance=self.balance+amount
            print(f'{amount} has been deposited')
            print(f'After deposit updated bank balance:{self.balance}')
        else:
            print(f'amount should be greater than zero')
    def withdraw(self,amount):
        if amount<self.balance:
            self.balance-=amount
            print(f'{amount} has been debited')
            print(f'After withdrawn updated bank balance:{self.balance}')
        else:
            print(f'Insufficient balance')
obj=account('ICICI','smith',98000,12345)
obj.details()
obj.display()
obj.deposit(3000)
obj.withdraw(1000)

