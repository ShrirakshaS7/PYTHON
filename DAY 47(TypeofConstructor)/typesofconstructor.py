# Type of constructor
# Default constructor

#1 WAP TO CREATE DEFAULT CONSTRUCTOR AND TO DISPLAY EMP NAME AND SALARY

class employee:
    def read(self, ename='smith', salary=98000):
        self.ename=ename
        self.salary=salary
emp1=employee()
emp1.read()
print(f'employee name is :{emp1.ename} and salary is:{emp1.salary}')
emp2=employee()
emp2.read('king',45000)
print(f'employee name is:{emp2.ename} and salary is:{emp2.salary}')

#2

class trainer:
    def read(self,tname='ram',salary=98000):
        self.tname=tname
        self.salary=salary
t1=trainer()
t1.read()
print(f'trainer name is:{t1.tname} and salary is:{t1.salary}')
print()
t2=trainer()
t2.read('sheeraj',60000)
print(f'trainer name is:{t2.tname} and salary is:{t2.salary}')

#3 WAP TO CREATE PARAMETERIZED CONSTRUCTOR AND TO DISPLAY EMP NAME AND JOB

class Employee:
    def __init__(self,ename,job):
        self.ename=ename
        self.job=job
    def display(self):
        print(f'employee name is:{self.ename}')
        print(f'employee job is:{self.job}')
emp1=Employee('smith','analyst')
emp1.display()
print()
emp2=Employee('scott','salesman')
emp2.display()

#4

class Trainer:
    def __init__(self,tname,job):
        self.tname=tname
        self.job=job
    def display(self):
        print(f'trainer name is:{self.tname}')
        print(f'trainer job is:{self.job}')
t1=Trainer('Ram','Python Developer')
t1.display()
print()
t2=Trainer('Chanadana','Test Engineer')
t2.display()

#5 WAP TO CREATE NON PARAMETERIZED CONSTRUCTOR AND TO DISPLAY EMP NAME AND deptno

class emp:
    def __init__(self):
        pass
    def display(self):
        print(f'emp name is:{self.ename} and deptno is:{self.deptno}')
e1=emp()
e1.ename='smith'
e1.deptno=10
e1.display()

#6 
class trainiee:
    def __init__(self):
        pass
    def display(self):
        print(f'trainer name is:{self.tname} and teaching subject is:{self.sub}')
t1=trainiee()
t1.tname='roopa'
t1.sub='testing'
t1.display()