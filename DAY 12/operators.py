# TRUE DIVISION

a = 98
b = 45
print(a/b)

a = 6
b = 3
print(a/b)


# FLOOR DIVISION

a = 90
b = 45
print(a//b)

a = 91
b = 45
print(a//b)

a = 39
b = 3
print(a//b)

a = 45.98
b = 23.78
print(a//b)


# WAP TO REMOVE LAST DIGIT FROM GIVEN NUMBER

num = 787654
print(num//10)


# WAP TO REMOVE LAST 2 DIGITS FROM GIVEN NUMBER

num = 787654
print(num//100)


# WAP TO REMOVE LAST 3 DIGITS FROM GIVEN NUMBER

num = 787654
print(num//1000)


# MODULUS OPERATOR

a = 11
b = 2
print(a%b)

a = 10
b = 2
print(a%b)


# WAP TO DISPLAY LAST DIGIT FROM GIVEN NUMBER

num = 7684568
print(num%10)


# WAP TO DISPLAY LAST 2 DIGITS FROM GIVEN NUMBER

num = 7684568
print(num%100)


# WAP TO DISPLAY LAST 4 DIGITS FROM GIVEN NUMBER

num = 7684568
print(num%10000)


# EXPONENT OPERATOR

print(2**3)


# RELATIONAL OPERATORS

a = 98
b = 98
print(a==b)

a = 98
b = 45
print(a==b)

s1 = 'jspiders'
s2 = 'JSpiders'
print(s1==s2)

list1 = [10,20,30]
list2 = [10,20,30]
print(list1==list2)

a = 98
b = 100
print(a!=b)

a = 98
b = 98
print(a>=b)

a = 98
b = 40
print(a>b)

a = 100
b = 150
print(a<b)

a = 198
print(a>100)

s1 = 'python'
s2 = 'java'
print(s1!=s2)

s1 = 'python'
s2 = 'java'
print(s1>s2)


# ORD FUNCTION

print(ord('p'))
print(ord('j'))


# WAP TO FIND ASCII VALUE OF 'A'

char = 'A'
print(ord(char))


# WAP TO FIND ASCII VALUE OF 'a'

char = 'a'
print(ord(char))


# WAP TO CONVERT UPPERCASE TO LOWERCASE

s1 = 'A'
result = ord(s1) + 32
print(chr(result))


# WAP TO CONVERT LOWERCASE TO UPPERCASE

s2 = 'a'
result = ord(s2) - 32
print(chr(result))


# SWAP WITHOUT USING 3RD VARIABLE

a = 5
b = 10
print("before swapping a:",a,"and b:",b)
a,b = b,a
print("after swapping a:",a,"and b:",b)


# SWAP USING 3RD VARIABLE

a = 10
b = 5
print("before swapping a:",a,"and b:",b)

temp = a
a = b
b = temp

print("after swapping a:",a,"and b:",b)