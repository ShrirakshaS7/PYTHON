# To write content

file=open('pythonE18.txt','w')
content=file.write('Welcome to Python class')
file.close()

# To Read the content

file=open('pythonE18.txt','r')
display=file.read()
print(display)
file.close()

# for append

file=open('pythonE18.txt','a')
content=file.write('\nwe are adding new data')
file.close()

# r+ using seek method

file=open('pythonE18.txt','r+')
content=file.write('we are using r+ mode to add new data')
file.seek(0)
display=file.read()
print(display)
file.close()

# r+ without using seek method

file=open('pythonE18.txt','r+')
content=file.write('we are using r+ mode to add new data')
file.close()

file=open('pythonE18.txt','r+')
display=file.read()
print(display)
file.close()

# w+
file=open('pythonE18.txt','w+')
content=file.write('we are using w+ mode to add new data')
file.seek(4)
display=file.read()
print(display)
file.close()

#a+
file=open('pythonE18.txt','a+')
content=file.write('\nappending new data using a+ mode')
file.seek(3)
display=file.read()
print(display)
file.close()

# tell method
file=open('pythonE18.txt','r')
display=file.read()
print(display)
pos=file.tell()
print(f'position of cursor is:{pos}')
file.close()

