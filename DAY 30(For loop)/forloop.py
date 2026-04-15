#19
nums=[10,20,45,98,35]
highest=nums[0]
for i in nums:
    if i>highest:
        highest=i
print(highest)

#20
nums=[10,20,45,98,35]
lowest=nums[4]
for i in nums:
    if i<lowest:
        lowest=i
print(lowest)

#21
nums=[10,20,45,98,35]
highest=second_highest=float('-inf')
for i in nums:
    if i>highest:
        second_highest=highest
        highest=i
    elif i >second_highest and i!=highest:
        second_highest=i
print(second_highest)

#22
text='eye'
res=''
for ch in text:
    rev=ch+rev
if rev==text:
    print(f'{text} is palindrome')
else:
    print(f'{text} is not a palindrome')

#23
s1='education'
res=''
for ch in s1:
    res=res+ch
print(res)

#24
input_str='education123python'
res=''
for ch in input_str:
    if 'A'<= ch<='Z' or 'a'<=ch<='z':
        res=res+ch
print(res)

#25
input_str='education123python'
res=''
alphabet=''
digit=''
for ch in input_str:
    if 'A'<=ch<='Z' or 'a'<=ch<='z':
        alphabet=alphabet+ch
    elif '0'<=ch<='9':
        digit=digit+ch
print(alphabet)
print(digit)

#26
input_str='PyThoN'
res=''
for ch in input_str:
    if 'A'<=ch<='Z':
        lowest=chr(ord(ch)+32)
        res=res+lowest
    else:
        res=res+ch
print(res)

#27
input_str='PyThoN'
res=''
for ch in input_str:
    if 'A'<=ch<='Z':
        lowest=chr(ord(ch)+32)
        res=res+lowest
    elif 'a'<=ch<='z':
        upper=chr(ord(ch)-32)
        res=res+upper
print(res)

#28
input_str='EDUCATION'
res=''
for ch in input_str:
    if ch in 'AEIOU':
        lower=chr(ord(ch)+32)
        res=res+lower
    else:
        res=res+ch
print(res)


#29
input_str = "Welcome To Python"
uppercase_chars = ''
for ch in input_str:
    if 'A' <= ch <= 'Z':  
        uppercase_chars = uppercase_chars +ch
print("Uppercase characters:", uppercase_chars)




#30
input_str = "Welcome To Python"
lowercase_chars = ''

for ch in input_str:
    if 'a' <= ch <= 'z':  
        lowercase_chars += ch
print("Lowercase characters:", lowercase_chars)


#31

input_str = "User123"
digits = ''
for ch in input_str:
    if '0' <= ch <= '9': 
        digits += ch
print("Digits in the string:", digits)




#32
input_str = "Hello @ python"
special_chars = ''
for ch in input_str:
    if not (('A' <= ch <= 'Z') or ('a' <= ch <= 'z') or ('0' <= ch <= '9')):
        if ch != ' ':       # Optional: ignore spaces
            special_chars += ch
print("Special characters:", special_chars)




#23

st = 'Hello 123 python'
result = ''
for ch in st:
    if ch in 'AEIOUaeiou' or ch == ' ':
        result = result + ch
print(result)


#34 
st = 'Hello 123 python'
vow = ''
con = ''
digit = ''
for ch in st:
    if ch in 'AEIOUaeiou':
        vow = vow + ch
    elif ch not in 'AEIOUaeiou' and not ch.isdigit():
        con = con + ch
    elif '0' <= ch <= '9':
        digit = digit + ch  
print("Vowels:", vow)
print("Consonants:", con)
print("Digits:", digit)

#35
input_str = "Python"
lowercase_chars = ''
for ch in input_str:
    if 'a' <= ch <= 'z':
        lowercase_chars += ch

print("Lowercase characters:", lowercase_chars)


# using method

string = 'JspiderS'
s1 = ''
for char in string:
    if char.islower():
        s1=s1+char
print(s1)   

#36
string = 'python123jspiders'
s1 = ''
for char in string:
    if char.isdigit():
        s1=s1+char  
print(s1)               

#38
string = 'hello good evening'
out = ''
for i in string:
    if i == ' ':         
        out = out + '_' 
    else:
        out = out + i  
print(out)


# using isspace method

string = 'hello good evening'
out = ''
for i in string:
    if i.isspace():
       out=out+'_'
    else:
        out=out+i
print(out)  

#38
string = 'python'
s1 = ''
for char in string:
    if char not in 'aeuio':
        s1 = s1+char
print(s1)  


# 39 strong number using nested for loop
num = 145
total =0
for i in str(num):
    fact = 1
    for j in range(1, int(i)+1):
        fact = fact * j
    total = total + fact        
if total == num :
    print(f'{num} is strong number')
else:
    print(f'{num} is not a strong number')





#40 Write a program to check a given number is a perfect number or not
# Perfect number is the sum of the given number the proper factors excluding the given number should be equal to the given number.

# 6 can be divide by 1 , 2 , 3  so 1+2+3=6
# 28 can be divide by 1,2,4,7,14 so 1+2+4+7+14=28

num = 6
sum = 0 
temp = num
for i in range(1, num):
    if num % i == 0:
        sum = sum + i
if temp == sum:
    print(f'{temp} is a perfect number.')
else:
    print(f'{temp} is not a perfect number.')   



# 41. spy number program 
# sum of digits equals product of digits

num=1124
sum=0
prod = 1
for digit in str(num):
    sum = sum + int(digit)
    prod = prod * int(digit)
if sum == prod:
    print(num, 'is a spy number')
else:
    print(num, 'is not a spy number') 





# 42 Fibonacci sequence
# each number is sum of previous two number

num=10
a=0
b=1
for i in range(10):
    print(a , end=' ')
    a,b = b , a+b   





#43. Neon number or not
# # a number for which the sum of the digit of its square equals to original number 

a = 9
n = a * a
sum = 0
for digit in str(n):
    sum = sum + int(digit)
if sum == a:
    print(a, 'is Neon number')
else:
    print(a, 'is not Neon number')

