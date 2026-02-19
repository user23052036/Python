

class ATM:

    # constructor
    # the variables created inside constructor is called instance variable
    # because it is different for different instances(object)

    # static /class variable
    __counter = 1

    def __init__(self):
        self.__pin = ''
        self.__balance = 0.0
        self.sno = ATM._counter
        ATM._counter += 1

        print(f'address of self = {id(self)}')
        self.menu()
    
    
    # --------------------
    # Getter & Setter counter
    # static methods are not onject dependent so dont need self
    # --------------------
    @staticmethod
    def get_counter():
        return ATM.__counter
    
    # --------------------
    # Getter & Setter counter
    # --------------------
    @staticmethod
    def set_counter(val):
        if type(val) == int:
            ATM.__counter = val
        else:
            print('Invalid counter set')

    # --------------------
    # Getter & Setter PIN
    # --------------------
    def set_pin(self, new_pin):
        if new_pin.isdigit():
            self.__pin = new_pin
            print("PIN set successfully")
        else:
            print("incorrect pin entered")

    def get_pin(self):
        return self.__pin


    # ------------------------
    # Getter for Balance only
    # ------------------------
    def get_balance(self):
        return self.__balance

    # Controlled balance update (no direct setter)
    def _update_balance(self, amount):
        self.__balance += amount

    def menu(self):
        usr_input = input("""
                        Helow follding are the valid operations
                        Enter
                          1. Enter 1 to create pin
                          2. Enter 2 to deposite
                          3. Enter 3 to withdraw
                          4. Enter 4 to check balance
                          5. Enter 5 to exit
                        """)
        if usr_input == '1':
            self.create_pin()
        elif usr_input == '2':
            self.deposite()
        elif usr_input == '3':
            self.withdraw()
        elif usr_input == '4':
            self.check_balance()
        else:
            print('Bye')
    
    def create_pin(self):
        self.__pin = input("Enter your pin: ")

    def deposite(self):
        pin = input('Enter pin: ')
        if pin == self.__pin:
            self.__balance += float(input('Enter deposite amount'))
        else:
            print('Wrong pin entered')
        
    def withdraw(self):
        pin = input('Enter pin: ')
        if pin == self.__pin:
            withdraw = float(input('Enter withdraw amount'))
            if withdraw > self.__balance:
                print('Insufficient balance')
            else:
                self.__balance -= withdraw
                print('successful withdrawn')
        else:
            print('Wrong pin entered')

    def check_balance(self):
        pin = input('Enter pin: ')
        if pin == self.__pin:
            print(f'current balance {self.__balance}')
        else:
            print('Wrong pin entered')