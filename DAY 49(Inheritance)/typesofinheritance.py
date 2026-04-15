# Inheritance
# Types of Inheritance
# single level inheritance
#1 WAP to create parent class as bank and child class saving account to perform deposit operation

class bank:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def display(self):
        print(f'Customer name:{self.name}')
        print(f'Ínitial bank balance:{self.balance}')
class savingaccount(bank):
    def deposit(self,amount):
        if amount>0:
            self.balance=self.balance+amount
            print(f'{amount} has been  deposited')
            print(f'after deposited updated bank balance:{self.balance}')
        else:
            print(f'amount should be greater than zero')
b1=savingaccount('smith',98000)
b1.display()
b1.deposit(1000)

#2. WAP to display student name,subject and marks and based on marks if marks are greater than equal to 35. display pass else fail

class student:
    def __init__(self,sname,subject,marks):
        self.sname=sname
        self.subject=subject
        self.marks=marks
    def display(self):
        print(f'student name:{self.sname} , subject:{self.subject} and marks:{self.marks}')
class result(student):
    def check_result(self):
        if self.marks>=35:
            print(f'Result:PASS')
        else:
            print(f'result:FAIL')
s1=result('smith','python',80)
s1.display()
s1.check_result()

#3 WAP to create employee as a parent class and designation as child class to display emp name, salary and designation

class emp:
    def __init__(self,ename,salary):
        self.ename=ename
        self.salary=salary
    def display_emp(self):
        print(f'emp name:{self.ename} and salary{self.salary}')
class designation(emp):
    def emp_designation(self,job):
        self.job=job
    def display_job(self):
        print(f'emp designation:{self.job}')
e1=designation('smith',98000)
e1.emp_designation('analyst')
e1.display_emp()
e1.display_job()

#4 WAP to perform check balance, deposit and withdraw operations using single level inheritance with exception handling validation

class bank:
    def __init__(self,acctno,balance):
        self.acctno=acctno
        self.balance=balance
    def account_details(self):
        print(f'Account number:{self.acctno}')
        print(f'balance:{self.balance}')
class savingaccount(bank):
    def deposit(self,amount):
        try:
            if amount<=0:
                raise ValueError('Deposit amount must be positive')
            self.balance=self.balance+amount
            print(f'deposited amount:{self.balance}')
        except ValueError as e:
            print('Deposit Error:',e)

    def withdraw(self,amount):
        try:
            if amount<=0:
                raise ValueError('withdrawal amount must be positive')
            if amount>self.balance:
                raise ValueError('Insufficient balance')
            self.balance = self.balance - amount
            print(f'withdrawal amount:{amount}')
        except ValueError as e:
            print('Withdrawal error',e)
        
    def updated(self):
        print(f'updated balance:{self.balance}')
a=savingaccount(12345,50000)
a.account_details()
a.deposit(1500)
a.withdraw(10000)
a.updated()
        
        
# 5
# Parent class
class Ticket:
    def set_ticket_details(self,name,ticket_no):
        self.name=name
        self.ticket_no=ticket_no
    def show_ticket_details(self):
        print("Passenger Name :",self.name)
        print("Ticket Number :",self.ticket_no)
# child class
class FlightTicket(Ticket):
    def set_flight_details(self,flight_name,seat_no):
        self.flight_name=flight_name
        self.seat_no=seat_no
    def show_flight_details(self):
        print("Flight Name:",self.flight_name)
        print("Seat number:",self.seat_no)
# creating object
obj=FlightTicket()
#Taking input
name=input("Enter passenger name:")
ticket_no=input("Enter ticket number:")
flight_name=input("Enter flight name:")
seat_no=input("Enter seat number:")
# setting values
obj.set_ticket_details(name,ticket_no)
obj.set_flight_details(flight_name,seat_no)
# Display output
obj.show_ticket_details()
obj.show_flight_details()