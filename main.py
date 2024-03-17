class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal Details")
        print("Name\t", self.name)
        print("Age\t", self.age)
        print("Gender\t", self.gender)

class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return

        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return

        self.balance += amount
        print(f"Account has been updated.\nBalance is {self.balance}")

    def withdraw(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return

        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return

        if amount > self.balance:
            print(f"Insufficient Funds\nBalance available is {self.balance}")
        else:
            self.balance -= amount
            print(f"Account has been updated.\nBalance is {self.balance}")

    def show_balance(self):
        self.show_details()
        print(f"Balance in your account is {self.balance}") 

def show_main_menu():
    print("\n1. Add User\n2. Deposit\n3. Withdraw\n4. Show Balance\n5. Users Existed\n6. Exit")

print("Welcome to the Simple Banking System")

users = []

while True:
    show_main_menu()
    choice = input("Enter an Option from above: ")

    if choice == '1':
        name = input("Enter the User Name: ")
        age = input("Enter the User Age: ")
        gender = input("Enter the User Gender: ")
        users.append(Bank(name, age, gender))
        print(f"User {name} added successfully.")
    elif choice == '6':
        print("God Bye!!!\n\t\t\t\tSHUTDOWNING SERVERS\t\t\t\t")
        break
    elif choice in {'2', '3', '4', '5'}:
        if not users and choice != '1':
            print("No users added yet. Please add a user first.")
        elif choice == '5':
            print("Users Existed:")
            for i, user in enumerate(users):
                print(f"Index: {i}, Name: {user.name}, Age: {user.age}, Gender: {user.gender}")
        else:
            print("Available Users:")
            for i, user in enumerate(users):
                print(f"Index: {i}, Name: {user.name}, Age: {user.age}, Gender: {user.gender}")

            user_index = input(f"Enter the user index to {['deposit', 'withdraw', 'show balance'][int(choice) - 2]}: ")
            if user_index.isdigit():
                user_index = int(user_index)
                if 0 <= user_index < len(users):
                    if choice == '2':
                        amount = input("Enter the amount to be deposited: ")
                        users[user_index].deposit(amount)
                    elif choice == '3':
                        amount = input("Enter the amount to be withdrawn: ")
                        users[user_index].withdraw(amount)
                    elif choice == '4':
                        users[user_index].show_balance()
                else:
                    print("Invalid user index.")
            else:
                print("Invalid input. Please enter a valid user index.")
    else:
        print("Invalid option. Please choose a valid option.")