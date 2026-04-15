#Continue statements
#1 WAP to print number from 1 to 5 except 3

for num in range(1,6):
    if num==3:
        continue
    print(num, end=' ')

#2 WAP to print only odd numbers from 1 to 10

for num in range(1,11):
    if num%2==0:
        continue
    print(num, end=' ')

#3 WAP to print even numbers from 1 to 10

for num in range(1,11):
    if num%2!=0:
        continue
    print(num, end=' ')