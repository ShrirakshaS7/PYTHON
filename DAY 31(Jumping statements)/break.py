#Break Statement
#1 WAP to print number from 1 to 4 using 1 to 20 range

for i in range(1,21):
    if i==5:
        break
    print(i,end=' ')

#2 WAP to print char upto e

for i in 'abcdefghijk':
    if i=='e':
        break
    print(i, end=' ')

#3 WAP to loop when number is divisible by 7 in 1 to 20 range

for i in range(1,21):
    if i%7==0:
        break
    print(i, end=' ')