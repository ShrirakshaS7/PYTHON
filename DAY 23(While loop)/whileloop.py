#28
num=1234
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print(rev)

#29
num=191
temp=num
rev=0
while temp>0:
    digit=temp%10
    rev=rev*10+digit
    temp=temp//10
if num==rev:
    print(f'{num} is palindrome')
else:
    print(f'{num} is not palindrome')

#WAP to check the given number is palindrome or not
num=1214
rev=0
temp=num
while temp>0:
    didgit=temp%10
    rev=rev*10+digit
    temp=temp//10
if num==rev:
    print(f'{num} is palindrome')
else:
    print(f'{num} is not a palindrome')

#30
n=1
while n<=1000:
    temp=n
    rev=0
    while temp>0:
        digit=temp%10
        rev=rev*10+digit
        temp=temp//10
    if n==rev:
        print(n)
    n=n+1




