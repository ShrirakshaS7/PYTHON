#34
num=5
i=1
count=0
while i<=num:
    if num%i==0:
        count=count+1
    i+=1
if count==2:
    print(f'{num} is prime number')
else:
    print(f'{num} is not a prime number')

#35
num=153
temp=num
sub_cubes=0
length=len(str(num))
while num>0:
    digit=num%10
    sum_cubes=sum_cubes**length
    num=num//10
if temp==sub_cubes:
    print(f'{temp} is armstrong number')
else:
    print(f'{temp} is not a armstrong number')

#36
n=5
a,b=0,1
count=0
while count<n:
    print(a, end='')
    a,b=b,a+b
    count=count+1

#37
num=9
square=num*num
sum_digit=0
temp=square
while temp>0:
    digit=temp%10
    sum_digi=sum_digit+digit
    temp=temp//10
if sum_digit==num:
    print(num,"is a neon number")
else:
    print(num,"is a neon number")
    


