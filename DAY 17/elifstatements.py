# Elif statements

#1
ch=input("Enter the char:")
if 'A'<=ch<='Z':
    print("char is uppercase")
elif 'a'<=ch<='z':
    print("char is lowercase")
else:
    print("Given char is not an alphabet")

#2
num=int(input("enter the char:"))
if num%3==0 and num%5==0:
    print("num is divisible by both")
elif num%5==0:
    print("num is divisible by 5")
elif num%3==0:
    print("num is divisible by 3")

#3
ch=input("enter the char:")
if 'A'<=ch<='Z' and 'a'<=ch<'z':
    print("char is alphabet")
elif '0'<=ch<='9':
    print("char is digit")

#4
ch=input()
if 'A'<=ch<='Z':
    print("char is uppercase")
elif 'a'<=ch<='z':
    print("char is lowercase")
