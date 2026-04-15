# With Statements

#1 'w' mode using with statement

with open ('pythonE18.txt','w') as file:
    file.write('we are using with statement')

#2 'r' mode using with statement

with open ('pythonE18.txt','r') as file:
    display=file.read()
    print(display)

# Types of read mode
# 1.read
# 2.readline

# eg
with open ('pythonE18.txt','r') as file:
    display=file.readline()
    print(display)

# 3.readlines 

#eg
with open ('pythonE18.txt','r') as file:
    display=file.readlines()
    print(display)

#eg
with open ('pythonE18.txt','r') as file:
    display=file.readlines()[2]
    print(display)

#3 'a' mode using with statement
with open ('pythonE18.txt','a') as file:
    file.write('\n we are appending new data using with statements')

#4 'w+' mode using with statemt
with open('pythonE18.txt','w+') as file:
    file.write('we are using with statemets')
    file.seek(2)
    display=file.read()
    print(display)

#5 'r+' mode using with statemets
with open('pythonE18.txt','r+') as file:
    display=file.read()
    print(display)
    file.write('we are using with statemets')
    file.seek(2)
    display2=file.read()
    print(display2)

#6 'a+' mode using with statements
with open('pythonE18.txt','a+') as file:
    file.write('\nwe are appending new data using with statements')
    file.seek(0)
    display=file.read()
    print(display)
