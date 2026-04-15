# To check given number is greater than 5
 
num=int(input("Enter a number: "))
res=num>5
print(res)

# The given number is greater than 10 and less than 20

num=int(input())
res=num>10 and num<20
print(res)

# the given number is divisible by 3

num=int(input())
res=num%3==0
print(res)

# the number divisible by both 3 and 5
num=int(input())
res=num%3==0 and num%5==0
print(res)

# to check the given char is uppercase

ch=input()
res=ch>='A' and ch<='Z'
print(res)

# the last digit of given char is divisible by 3 or not

ch=input()
ascii=ord(ch)
ld=ascii%10
res=ld%3==0
print(res)

