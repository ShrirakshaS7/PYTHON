# Constructor
#11 WAP to display person name and age by creating constructor method
class person:
    def __init__(self,name,age):
        self.name=name 
        self.age=age
    
    def display(self):
        print(f'person name:{self.name} and age:{self.age}')
p1=person('smith',98000)
p1.display()
p2=person('king',89000)
p2.display()

#12 WAP to display empname,sal and designation along with their company name using constructor method

class employee:
    company_name='canara'
    def __init__(self,ename,sal,job):
        self.ename=ename
        self.sal=sal
        self.job=job
    def display(self):
        print(f'employee name:{self.ename}, sal is:{self.sal}, job:{self.job} and company name:{employee.company_name}')
e1=employee('roshan',35000,'tax associate')        
e1.display()

#13 WAP to perform application scenario (check balance,deposiot,withdraw)

class BankAccount:
    bankname='ICICI'
    def __init__(self,cname,balance):
        self.cname=cname
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance=self.balance+amount
            print(f'{amount} has been deposited')
            print(f'After deposit updated balance : {self.balance}')
        else:
            print("Amount should be greater than zero")
    def withdraw(self,amount):
        if amount<self.balance:
            self.balance=self.balance-amount
            print(f'{amount} has been debited')
            print(f'After withdraw updated balance {self.balance}')
        else:
            print("Insufficient balance")
    def check_balance(self):
        print(f'Initial balance is:{self.balance}')
b1=BankAccount('smith',98000)
b1.check_balance()
b1.deposit(1000)
b1.withdraw(500)


#14
class BookMyShow:
    def __init__(self, theater_name):
        print("Welcome to Book My Show!")
        self.theater_name = theater_name

        if self.theater_name == "PVR":
            print("\nMovies available at PVR:")
            self.movie1 = "Avatar: The Way of Water"
            self.movie2 = "The Batman"
            self.price1 = 850   
            self.price2 = 800

        elif self.theater_name == "INOX":
            print("\nMovies available at INOX:")
            self.movie1 = "Mission: Impossible - Fallout"
            self.movie2 = "Jurassic World: Dominion"
            self.price1 = 900
            self.price2 = 950

        else:
            print("Sorry, theater not available.")
            return

        print(f"1. {self.movie1}")
        print(f"2. {self.movie2}")

        # Ask movie choice AFTER showing movies
        self.movie_choice = input("\nEnter your movie choice (1 or 2): ")
        self.select_movie()

    def select_movie(self):
        if self.movie_choice == "1":
            self.selected_movie = self.movie1
            self.price = self.price1
        elif self.movie_choice == "2":
            self.selected_movie = self.movie2
            self.price = self.price2
        else:
            print("Invalid choice")
            return

        print(f"\nSelected Movie: {self.selected_movie}")
        print(f"Ticket Price: RS {self.price}")

        # Ask confirmation AFTER selection
        self.confirm = input("\nDo you want to book ticket? (yes/no): ")
        self.confirm_booking()

    def confirm_booking(self):
        if self.confirm == "yes":
            print(f"\nTicket for '{self.selected_movie}' booked successfully!")
        else:
            print("\nBooking cancelled.")


# Step 1: Take only theater input
theater = input("Enter the name of the theater (PVR, INOX): ")

# Step 2: Pass to constructor
booking = BookMyShow(theater)






