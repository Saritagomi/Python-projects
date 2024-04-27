class Atm:
    def __init__(self):
        self.__pin = ""
        self.__balance = 0
        self.__menu()

    def get_pin(self):
        return self.__pin

    def set__pin(self,new_pin):
        if type(new_pin)==str:
            self.__pin = new_pin
            print("pin changed")
        else:
            print("not allowed")
    def __menu(self):
        user_input = input("""
        Hello,how would you like to proceed?
        1. Enter 1 to create pin
        2. Enter 2 to deposit
        3. Enter 3 to withdraw
        4. Enter 4 to check balance 
        5. Enter 5 to exit
        """)
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        else:
            print("bye")

    def create_pin(self):
        self.__pin = input("enter your pin")
        print("pin set successfully")
        self.__menu()

    def deposit(self):
        temp = input("enter your pin")
        if temp == self.__pin:
            amount = int(input("enter the amount"))
            self.__balance = self.__balance + amount
            print("deposit successfully")
        else:
            print("invalid pin")
        self.__menu()

    def withdraw(self):
        temp = input("enter your pin")
        if temp == self.__pin:
            amount = int(input("enter your amount"))
            if amount < self.__balance:
                self.balance = self.__balance - amount
                print("operation successfully")
            else:
                print("insufficient funds")
        else:
            print("invalid pin")
        self.__menu()

    def check_balance(self):
        temp = input("enter your pin")
        if temp == self.__pin:
            print(self.__balance)
        else:
            print("invalid pin")
        self.__menu()
SBI = Atm()
print(get_pin)