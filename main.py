from time import time, ctime


class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
    


class Account:
    def __init__(self, user, password):
        self.min_balance = 0
        self.current = 0
        self.user = user
        self.password = password
        self.history = []
    
    def withdraw(self, cash):
        trials = 2;
        while (trials > 0):
            print('NOTE: You only have 3 trials to enter password.')
            check = input('Enter password: ');
            if (check == self.password):
                break
            elif (check != self.password):
                print('WRONG PASSWORD!')
                print('You have {} trails.'.format(trials))
            
            print('You can not use this account.')

        if (self.current <= self.balance):
            print('You can not deposit')
        self.current -= cash
        when = ctime(time())
        self.add_to_history('withdraw', cash, when)
        
    
    def deposit(self, cash):
        self.current += cash
        self.add_to_history('deposit', cash, ctime(time()))

    
    def set_balance(self, new_balance):
        self.balance = new_balance
        when = ctime(time())
        self.add_to_history('balancing', new_balance, when)

    
    def add_to_history(self, operation_name, cash, operation_date):
        operation = {
            'operation_name': operation_name,
            'amount': cash,
            'operation_time': operation_date
        }
        self.history.append(operation)
    
    def get_history(self):
        for operation in self.history:
            print(operation)


    def set_password(self, new_password):
        print('Making Sure that it is you...')
        check_old = input('Enter The old password: ')

        if (check_old == self.password):
            self.password = new_password
            print("You changed password successfully.")
        else:
            print('You can not change the password of this account.')
        
        
    

    def get_current(self):
        self.add_to_history('inquiry', self.current, ctime(time()))
        return self.current


class Bank:
    def __init__(self):
        self.accounts = []
        self.users = []

    def add_account(self, new_account):
        self.accounts.append(new_account)
    
    def create_account(self, first_name, last_name, age, email, password):
        # first_name = str(input('Enter your first name: ')).strip().lower()
        # last_name = str(input('Enter your last name: ')).strip().lower()

        # age = int(input('Enter your age: ').strip())
        # if (age < 18):
        #     print('you are too young to make an account.')

        # email = str(input('Enter your email: ')).strip()
        # if(email.__contains__('@') and email.__contains__('.')):
        #     pass
        # else:
        #     print('invalid email address')

        # password = str(input('Enter your password: ')).strip()
        # password_verify = str(input('Enter your password again: ')).strip()

        # while (password != password_verify):
        #     print('InCorrect Password verfication')
        #     password_verify = str(input('Enter your password again: ')).strip()
        
        # print('You created an account successfully.')
        
        
        
        new_user = User(first_name, last_name, age, email)
        new_account = Account(new_user, password)
        self.users.append(new_user)
        self.accounts.append(new_account)

        return new_account


alahly = Bank()

my_account = alahly.create_account('abdulrahman', 'mahmoud', 19, 'abcd@gmail.com', 123546)
my_account.set_balance(5000)
my_account.deposit(10000)
my_account.set_password(1235465)

        