# methods in ooops
#Object method
#1 WAP to create object method
class bankaccount:
    def __init__(self,cname,balance):
        self.cname=cname
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance=self.balance+amount
            print(f'{amount} has been deposited')
            print(f'after deposit updated bank balance:{self.balance}')
        else:
            print(f'amount should be grater than zero')
b1=bankaccount('allen',98000)
b1.deposit(8000)

# Class method
#eg
class bankaccount:
    bankname='icici'
    def __init__(self,cname,balance):
        self.cname=cname
        self.balance=balance
    @classmethod
    def change_bankname(cls,new_bankname):
        print(f'before modifying the bankname:{bankaccount.bankname}')
        cls.bankname=new_bankname
        print(f'after modifying the bankname:{bankaccount.bankname}')
    def deposit(self,amount):
        if amount>0:
            self.balance=self.balance+amount
            print(f'{amount} has been deposited')
            print(f'after deposit updated bank balance:{self.balance}')
        else:
            print(f'amount should be grater than zero')
    def display(self):
        print(f'customer name:{self.cname} and initial bank balance:{self.balance}')
b1=bankaccount('allen',1000)
b1.display()
b1.deposit(100)
b1.change_bankname('hdfc')

# static method
#eg
class calculator:
    @staticmethod
    def addition(a,b):
        return a+b
print(calculator.addition(100,300))

# WAP TO CREATE A INSTANCE METHOD,CLASS METHOD AND STATIC METHOD .TO DISPLAY STUDENT NAME,MARKS AND SCHOOL NAME 
# 1. INSTANCE VARAIBLES(STUDENT NAME AND MARKS)
# 2. CLASS VARIABLES(SCHOOL NAME)
# 3. INSTANCE METHOD(ADD BONUS MARKS)
# 4. CLASS METHOD(CHANGE SCHOOL NAME)
# 5. STATIC METHOD(CHECK PASS OR FAIL) PASS IF MARKS>=35

class student:
    school_name='Qspiders'
    def __init__(self,sname,marks):
        self.sname=sname
        self.marks=marks
    def add_bonus(self,extra_marks):
        self.marks=self.marks+extra_marks
        print(f'after adding the extra marks:{self.marks}')
    @classmethod
    def change_schoolname(cls,new_schoolname):
        cls.school_name=new_schoolname
        print(f'after changing the school name:{cls.school_name}')
    @staticmethod
    def check(marks):
        return marks>=35
    def display(self):
        print(f'student name:{self.sname} and marks:{self.marks}')
        if student.check(self.marks):
            print(f'result: PASS')
        else:
            print(f'FAIL')
s1=student('smith',80)
s1.display()
s1.add_bonus(10)
s1.change_schoolname('dhee coding lab')

    
    