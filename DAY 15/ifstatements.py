# Conditional statements

# if statement

#1
a=98
b=45
if a>b:
    print(f' a:{a} is greater than b:{b}')

#2
num=eval(input('enter the number:'))
if num>0:
    print(f'{num} is positive')


num=98
if num>0:
    print(f'{num} is positive')

#3
num=46
if num%2==0:
    print(f'{num} is even number')

#4
num=77
if num%2!=0:
    print(f'{num} is odd number')

#5
num=15
if num%3==0:
    print(f'{num} is divisible by 3')

#6
num=25
if num%5==0:
    print(f'{num} is divisible by 5')

#7
num=15
if num%3==0 and num%5==0:
    print(f'{num} is divisible by 3 and 5')

#8
s1='apple'
if s1[0] in 'aeiouAEIOU':
    print(f'{s1} is starts with vowel')

#9
s2='microsoft'
if s2[0] not in 'aeiouAEIOU':
    print(f'{s2} is starts with consonent')

#10
s3='hello'
if s3[-1] in 'aeiouAEIOU':
    print(f'{s3} is ends with vowel')

#11
s4='ram'
if s4[2] not in 'aeiouAEIOU':
    print(f'{s4} is ends with consonents')

#12
ch='Apple'
if ch[0]>='A' and ch[0]<='Z':
    print(f'{ch} is starts with uppercase')


ch='Apple'
if 'A'<=ch[0]<='Z':
    print(f'{ch} is starts with uppercase')

#13
char='e'
if 'A'<=char<='Z':
    print(f'{char} is lowercase')

#14
char='9'
if '0'<=char<='9':
    print(f'{char} is digit')

#15
char='$'
if not('A'<=char<='Z' or 'a'<=char<='z' or 'o'<=char<='9'):
    print(f'{char} is special symbol')