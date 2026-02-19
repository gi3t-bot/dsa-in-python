from random import randint


class Bank:

    def __init__(self):
        self.account_number = randint(100, 999)
        self.full_name = input("Enter your name: ")
        self.phone_no = int(input("Enter your number: "))
        self.balance = 0

    def show_info(self):
        print(f"Account number: {self.account_number}")
        print(f"Full Name: {self.full_name}")
        print(f"Phone Number: {self.phone_no}")
        print(f"Current balance: {self.balance}")
        print("")

    def show_balance(self) -> None:
        print(f"Account number: {self.account_number}")
        print(f"Current balance: {self.balance}")

    def withdraw(self) -> None:
        amount = int(input("Enter the amount to withdraw: "))

        if amount > self.balance:
            print("Insufficient Balance...")
            self.show_balance()

        else:
            self.balance -= amount
            self.show_balance()

    def deposit(self) -> None:
        amount = int(input("Enter the amount to deposit: "))

        self.balance += amount
        self.show_balance()


# bank1 = Bank()

# bank1.show_balance()

# bank1.deposit()
# bank1.withdraw()

# in this case the number of objects is limited so we dont have that much problem.....
# but when the number of objects will increase then we will have difficult time in inserting the objects manually...

# so inorder to avoid writing manually, we will just create a list and then start appending the objects that we create...

# customer = []

# cust1 = Bank()
# customer.append(cust1)

# print(customer) # this will show the address of the first object stored in the memory

# cust2 = Bank()
# customer.append(cust2)

# print(customer) # this will show the address of the first, second object stored in the memory


# # after the insertion we can access the data in the objects as:

# customer[0].show_balance()
# customer[1].deposit()
# customer[1].show_balance()


# still instead of writing all this, we will make use of while loop
customer = []

while True:
    print("1. Create a new customer: ")
    print("2. Show Account info: ")
    print("3. Deposit: ")
    print("4. Withdraw: ")
    print("5. Exit: ")
    print("")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        cust = Bank()
        customer.append(cust)

    elif choice == 2:
        if len(customer) == 0:
            print("No account has been created...")

        else:
            for account in customer:
                account.show_info()

        print("")

    elif choice == 3:
        if len(customer) == 0:
            print("No account has been created...")

        else:
            acc_no = int(input("Enter the account number to deposit: "))

            for obj in customer:
                if obj.account_number == acc_no:
                    obj.deposit()
                    break

    elif choice == 4:
        if len(customer) == 0:
            print("No account has been created...")

        else:
            acc_no = int(input("Enter the account number to withdraw: "))

            for obj in customer:
                if obj.account_number == acc_no:
                    obj.withdraw()
                    break

    elif choice == 5:
        break

    else:
        print("Invalid choice")
        print("")
