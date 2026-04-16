# Encapsulation
# Public access modifier
# 1
class bank:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def display(self):
        print(f'customer name:{self.name} and balance:{self.balance}')
obj=bank('smith',98000)
obj.display()
print()
print(f'customer name accessing outside the class:{obj.name}')
print(f'customer balance accessing outside the class:{obj.balance}')
obj.name='allen'
obj.balance=78000
print(f'after modifying value name:{obj.name} and balance:{obj.balance}')

# Protected access modifier
#1
class bank:  
    def __init__(self,name,balance):
        self._name=name
        self._balance=balance
    def display(self):
        print(f'customer name:{self._name} and balance:{self._balance}')
obj=bank('allen',45000)
obj.display()
        

#2 using protected methods
class bank:
    def __init__(self,name,balance):
        self.__name=name
        self.__balance=balance
    def _showdetails(self):
        print(f'customer name:{self.__name} and balance:{self.__balance}')
class customer(bank):
    def display(self):
        self._showdetails()
obj=customer('john',89000)
obj.display()
        
# Private access specifiers
#1
class bank:
    def __init__(self,name,balance):
        self.__name=name
        self.__balance=balance
    def _showdetails(self):
        print(f'customer name:{self.__name} and balance:{self.__balance}')
class customer(bank):
    def display(self):
        self._showdetails()
obj=customer('smith',98000)
obj.display()
# print(obj.__balance) AttributeError: 'customer' object has no attribute '__balance'
print(obj._bank__balance)

# using Getter and Setter method
class employee:
    def __init__(self,empno,ename,salary):
        self.empno=empno
        self.ename=ename
        self.__salary=salary
    def get_salary(self):
        return self.__salary
    def set_salary(self,new_salary):
        if new_salary>0:
            self.__salary=new_salary
        else:
            print('salary should be more than zero')
e=employee(7839,'allen',45000)
print(f'empno:{e.empno} and ename :{e.ename}')
print(f'emp salary:{e.get_salary()}')
e.set_salary(35000)
print(f'updated salary:{e.get_salary()}')

# using @decorator to define gettter and setter method
class bankAccount:
    def __init__(self,balance):
        self.__balance=balance
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self,new):
        if isinstance(new,int):
            self.__balance=new
        else:
            raise ValueError('invalid formatted data')
c1=bankAccount(3000)
c1.balance=5000
print(c1.balance)


        