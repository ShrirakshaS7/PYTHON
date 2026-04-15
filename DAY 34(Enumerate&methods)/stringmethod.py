# String Method
# Find method
#1
msg='python'
print(msg.find('t'))
print(msg.find('n'))
print(msg.find('j'))

#Rindex method
#1
msg='python python python'
print(msg.rindex('h'))

#Replace method
#1
msg='welcome to python'
print(msg.replace('o','*'))
print(msg.replace('o','*',1))
print(msg.replace('o','*',2))
print(msg.replace('o','*',10))

#Startswith method
#1
msg='python'
print(msg.startswith('p'))
print(msg.startswith('P'))
print(msg.startswith('j'))

#Endswith method
#1
msg='python'
print(msg.endswith('n'))
print(msg.endswith('a'))

#Split method
#1
msg='welcome to python'
print(msg.split())
print(msg.split('o'))

#2 WAP to display extension of a file
filename='python.txt'
extension=filename.split('.')
print(extension[-1])

#3 WAP to display only filename
filename='python.txt'
file=filename.split('.')
print(file[0])

#4 WAP to print domain of a given url
link='https://pyspiders.com'
res=link.split('://')
print(res[-1])

#5 WAP to print protocol of a given url
link='https://pyspiders.com'
res=link.split('://')
print(res[0])

#Join method
#1
msg='Hello python'
res='*'.join(msg)
print(res)

#2
words=['hello','python']
res='*'.join(words)
print(res)

#ISALPHA method
#1
msg='python'
print(msg.isalpha())

#2
msg='python12345'
print(msg.isalpha())

#ISALNUM method
#1
msg='python123'
print(msg.isalnum())

#2
msg='python**&12345'
print(msg.isalnum())

#ISLOWER method
#1
msg='python'
print(msg.islower())

#2
msg='pythoN'
print(msg.islower())

#ISUPPER method
#1
msg='PYTHON'
print(msg.isupper())

#2
msg='pYTHON'
print(msg.isupper())

#ISDIGIT method
#1
num='12345'
print(num.isdigit())