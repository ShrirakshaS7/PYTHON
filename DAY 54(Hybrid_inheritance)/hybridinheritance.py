# Hybrid Inheritance
#1
class A:
    def display_A(self):
        print(f'Class A')
class B(A):
    def display_B(self):
        print(f'Class B')
class C(A):
    def display_C(self):
        print('Class C')
class D(B,C):
    def display_D(self):
        print('Class D')
obj=D()
obj.display_A()
obj.display_B()
obj.display_C()
obj.display_D()

#2 Eg for hybrid inheritance using constructor
class A:
    def __init__(self):
        print('Constructor A')
class B(A):
    def __init__(self):
        super().__init__()
        print('Constructor B')
class C(A):
    def __init__(self):
        super().__init__()
        print('Constructor C')
class D(C,B):
    def __init__(self):
        super().__init__()
        print('Constructor D')
obj=D()
print(D.__mro__)

#3 WAP to create hybrid inheritance with combination of single level, heirarchical and multiple inheritance
class Account:
    def __init__(self,acc_holder,balance):
        self.acc_holder=acc_holder
        self.balance=balance
    def show_balance(self):
        print(f'account holder:{self.acc_holder}')
        print(f'balance:{self.balance}')
class saving(Account): #SI
    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f'deposited:{amount}')
class current(Account): #HI
    def withdraw(self,amount):
        self.balance-=amount
        print(f'withdraw:{amount}')
class combineAccount(saving,current): #MI
    pass
acct=combineAccount('smith',98000)
acct.show_balance()
acct.deposit(1000)
acct.withdraw(500)
acct.show_balance()

#4 WAP to implement combination of single, multilevel and heirarchical inheritance using constructor chaining and method chaining
class Animals:
    def __init__(self):
        print('welcome to animal world')
class cat(Animals):
    def __init__(self):
        super().__init__()
    def display_cat(self):
        print('I am cat')
        return self
class dog(cat):
    def __init__(self):
        super().__init__()          
    def display_dog(self):
        print('I am dog')
        return self
class cow(Animals):
    def __init__(self):
        super().__init__()
    def display_cow(Self):
        print('I am cow')
        return Self
class horse(cow,dog):
    def __init__(self):
        super().__init__()
    def display_horse(self):
        print('I am horse')
        return self
obj=horse()        
obj.display_cat().display_dog().display_cow().display_horse()


