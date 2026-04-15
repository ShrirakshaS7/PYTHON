# CSV file handling
# w mode

#1 without using with statement 

import csv
file=open('pythonE18.csv','w',newline='')
writer=csv.writer(file)
writer.writerow(['ename','salary','deptno'])
writer.writerow(['smith',3000,10])
writer.writerow(['king',3500,20])
file.close()

#2 using with statement

import csv
with open('pythonE18.csv','w',newline='') as file:
    writer=csv.writer(file)
    writer.writerow(['ename','salary','deptno'])
    writer.writerows([['smith',10,10],['allen',1000,30]])

# r mode
#3 without using with statement 

import csv
file=open('pythonE18.csv','r')
reader=csv.reader(file)
for row in reader:
    print(row)
file.close()

#4 using with statement
import csv
with open('pythonE18.csv','r') as file:
   reader=csv.reader(file)
   for row in reader:
    print(row)

# a mode
#5 without using with statement 
import csv
file=open('pythonE18.csv','a')
writer=csv.writer(file)
writer.writerow(['jones',9000,20])
file.close()

#6 using with statement
import csv
with open('pythonE18.csv','a',newline='') as file:
   writer=csv.writer(file)
   writer.writerow(['king',900,10])

# w+ mode
#7 without using with statement 
import csv
file=open('pythonE18.csv','w+',newline='')
writer=csv.writer(file)
writer.writerow(['ename','salary','deptno'])
writer.writerow(['smith',3000,10])
writer.writerow(['king',3500,20])
file.seek(0)
reader=csv.reader(file)
for row in reader:
    print(row)
file.close()

#8 using with statement
import csv
with open('pythonE18.csv','w+') as file:
    writer=csv.writer(file)
    writer.writerow(['ename','salary','deptno'])
    writer.writerows([['smith,2000,10'],['allen',1000,30]])
    file.seek(0)
    reader=csv.reader(file)
    for row in reader:
        print(row)

# r+ mode
#9 without using with statements
import csv
file=open('pythonE18.csv','r+')
reader=csv.reader(file)
for row in reader:
    print(row)
writer=csv.writer(file)
writer.writerow(['smith',2000,10])
file.close()

#10 using with statement
import csv
with open('pythonE18.csv','r+') as file:
   reader=csv.reader(file)
   for row in reader:
      print(row)
   writer=csv.writer(file)
   writer.writerow(['sandy',300,20])

# a+ mode
#11 without using with statement
import csv
file=open('pythonE18.csv','a+', newline='')
writer=csv.writer(file)
writer.writerow(['allexa',34000,10])
file.seek(0)
reader=csv.reader(file)
for row in reader:
   print(row)
file.close()

#12 using with statement
import csv
with open('pythonE18.csv','a+',newline='') as file:
   writer=csv.writer(file)
   writer.writerow(['allen',400,10])
   file.seek(0)
   reader.csv.reader(file)
   for row in reader:
       print(row)