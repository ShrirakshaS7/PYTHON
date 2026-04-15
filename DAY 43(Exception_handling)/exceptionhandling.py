# EXCEPTION HANDLING
# Single Exception handling

# 1 WAP to divide two numbers & handle ZeroDivisonError
try:
    a=20
    b=0
    res=a/b
    print(res)
except ZeroDivisionError:
    print('can not divide by zero')

# 2 WAP to access a list element, if there is index error display index value out of range
try:
    list=[10,20,30]
    print(list[4])
except IndexError:
    print('index value out of range')

# 3 WAP to convert string into integer, if it is not possible display invalid conversion
try:
    num=int('python')
    print(num)
except ValueError:
    print('Invalid Conversion')

# MULTIPLE EXCEPTION HANDLING

#1 WAP to handle ZeroDivisionError and ValueError
try:
    a=int(input('enter the value of a:'))
    b=int(input('enter the value of b:'))
    res=a/b
    print(res)
except ZeroDivisionError:
    print('can not divide by zero')
except ValueError:
    print('Invalid conversion')

#eg using else block
try:
    a=45
    b=2
    res=a//b
except ZeroDivisionError:
    print('can not divide by zero')
else:
    print(res)

# eg using finally block
try:
    a=45
    b=0
    res=a//b
except ZeroDivisionError:
    print('error')
finally:
    print('program completed')

#1 WAP to withdraw money from  a bank account, raise exception if insufficient balance and min balance 1000 must be maintained
try:
    balance=5000
    withdraw=int(input('enter the amount to withdraw:'))

    if withdraw>balance:
        raise Exception('Insufficient balance')

    if balance-withdraw<1000:
        raise ValueError('minimum balance 1000 must be maintained in bank account')
except Exception as e:
    print('error:',e)
except ValueError as v:
    print('error:',v)

else:
    balance=balance-withdraw
    print(f'{withdraw} has been debited from account')
    print(f'after withdraw updated balance:{balance}')

finally:
    print('Thankyou for using ATM')


# WAP to perform banking operations such as Balance,deposite and withdraw using exception handling

