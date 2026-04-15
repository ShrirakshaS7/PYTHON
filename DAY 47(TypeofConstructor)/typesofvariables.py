# TYPES OF VARIABLES
# instance varaibles

#eg
class Emp:
    def __init__(self,ename,job):
        self.ename=ename
        self.job=job

    def display(self):
        print(f'emp name:{self.ename} and job:{self.job}')

e1=Emp('smith','analyst')
e2=Emp('allen','developer')
e1.display()
e2.display()

# static variable

class Emp:
    company_name='Techcrop'

    def __init__(self,ename,job):
        self.ename=ename
        self.job=job

    def display(self):
        print(f'emp name:{self.ename} and job:{self.job}')

e1=Emp('smith','analyst')
e2=Emp('allen','python_developer')
e1.display()
e2.display()

# local variable

class emp:
    def __init__(self,ename,monthly_salary,job):
        self.ename=ename
        self.monthly_salary=monthly_salary
        self.job=job
    def calculate_annual_salary(self):
        annual_salary=self.monthly_salary*12
        print(f'employee:{self.ename},job:{self.job}, annual salary:{annual_salary}')
e1=emp('ram',5,'pythondeveloper')
e1.calculate_annual_salary()