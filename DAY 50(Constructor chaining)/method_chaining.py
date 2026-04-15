# Method Chaining
#1 
class bank:
    def __init__(self,bname,name):
        self.bname=bname
        self.name=name
    def details(self):
        print(f'bankname is:{self.bname}')
        print(f'customer name:{self.name}')
        return self
class account(bank):
    def __init__(self, bname, name,balance,acctno):
        super().__init__(bname, name)
        self.balance=balance
        self.acctno=acctno
    def display(self):
        print(f'initial bank balance:{self.balance}')
        print(f'customer acctno:{self.acctno}')
        return self
    def deposit(self,amount):
        if amount>0:
            self.balance=self.balance+amount
            print(f'{amount} has been deposited')
            print(f'after deposit updated bank balance:{self.balance}')
        else:
            print(f'amount should be greater than zero')
        return self
    def withdraw(self,amount):
        if amount<self.balance:
            self.balance=self.balance-amount
            print(f'{amount} has been debited')
            print(f'after withdrawn updated bank balance:{self.balance}')
        else:
            print('Insufficient balance')
        return self
obj=account('icici','smith',98000,123)
obj.details().display().deposit(500).withdraw(500)

#2 WAP to perform single level inhertance to display customer name, balance and to perform deposit and withdraw raise valueError(max withdraw limit is 10000 using method chaining)
class bankaccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        if amount<=0:
            raise ValueError('deposit amount must be greater than zero')
        self.balance+=amount
        print(f'{amount} deposited. New balance:{self.balance}')
    def withdraw(self,amount):
        if amount>self.balance:
            raise ValueError('Insufficient funds')
        if amount<=0:
            raise ValueError('withdrawal amount must be greater than zero')
        self.balance-=amount
        print(f'{amount} is debited. Updated balance:{self.balance}')
class savingbankaccount(bankaccount):
    def __init__(self, name, balance):
        super().__init__(name, balance)
    def withdraw(self, amount):
        if amount>10000:
            raise ValueError('max withdraw limit is 10000')
        super().withdraw(amount)
c1=bankaccount('steeve',50000)
c2=savingbankaccount('alice',30000)

c1.deposit(10000)
c1.withdraw(20000)

try:
    c1.deposit(5000)
    c2.withdraw(15000)
except ValueError as e:
    print(e)

c2.withdraw(15000)

        

