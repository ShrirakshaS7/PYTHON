# Match case statements
#1 WAP to print Day based on number
day=eval(input("enter a num:"))
match day:
    case 1:
        print('Monday')
    case 2:
        print('Tuesday')
    case 3:
        print('Wednesday')
    case 4:
        print('Thursday')
    case 5:
        print('Friday')
    case 6:
        print('saturday')
    case 7:
        print('Sunday')
    case _:
        print('Invalid Numbers')

#2 WAP to create simple calculator using match case statements
operation=eval(input('enter a number:'))
num1=9
num2=2
match operation:
    case 1:
        print(f'sum of {num1} and {num2}:{num1+num2}')
    case 2:
        print(f'differnce of {num1} and {num2}:{num1-num2}')
    case 3:
        print(f'product of {num1} and {num2}:{num1*num2}')
    case 4:
        if num2!=0:
            print(f'true division:{num1/num2}')
        else:
            print('ZeroDivisionError')
    case 5:
        if num2!=0:
            print(f'floor division:{num1//num2}')
        else:
            print('ZeroDivisionError')
    case 6:
        print(f'exponent is:{num1**num2}')
    case 7:
        print(f'modulus is:{num1%num2}')
    case _:
        print(f'Invalid operation')


#3 WAP to perform ATM operation
# 1) check balance deposite 2)Deposite 3)Withdraw 4)Exit

balance=98000
while True:
    print("\n ----ATM Menu----")
    print("1.Check Balance")
    print("2.Deposite")
    print("3.Withdraw")
    print("4.Exit")
    choice=eval(input("enter your choice(1-4):"))
    match choice:
        case 1:
            print(f'Your balance is:{balance}')
        case 2:
            amount=float(input('enter amount to deposite:'))
            if amount>0:
                balance=balance+amount
                print(f'Rs {amount} deposited successfull')
                print(f'updated balance:{balance}')
            else:
                print("Invalid amount!")
        case 3:
            amount=float(input('enter the amount to withdraw:'))
            if amount<=balance and amount>0:
                balance=balance-amount
                print(f'Rs {amount} withdraw successfull')
                print(f'updated balance:{balance}')
            else:
                print("Insufficient balance")
        case 4:
            print(f'Thank you for using ATM! Bye')
        case _:
            print("Invalid Operation")

#4 WAP to perform 1)palindrome 2)Armstrong number 3)Strong number
num=eval(input("enter the number:"))
while True:
    print("1.Palindrome")
    print("2.Armstrong Number")
    print("3.Strong Number")
    print("4.Exit")
    choice=eval(input("enyter your choice:"))
    match choice:
        case 1:
            temp=num
            rev=0
            while num>0:
                digit=num%10
                rev=rev*10+digit
                num=num//10
            if temp==rev:
                print(f'{temp} is palindrome number')
            else:
                print(f'{temp} is not a palindrome number')
        
        case 2:
            temp=num
            sum_cubes=0
            length=len(str(num))
            while num>0:
                digit=num%10
                sum_cubes=sum_cubes+digit**length
                num=num//10
            if temp==sum_cubes:
                print(f'{temp} is armstrong number')
            else:
                print(f'{temp} is not a armstrong numbe')
            
        case 3:
            temp=num
            sum=0
            while num>0:
                digit=num%10
                fact=1
                i=1
                while i<=digit:
                    fact=fact*i
                    i=i+1
                    sum=sum+fact
                    num=num//10
                if sum==temp:
                    print(f'{temp} is strong number')
                else:
                    print(f'{temp} is not a strong number')
        
        case 4:
            print("Exit")

        case _:
            print("Invalid Choice")