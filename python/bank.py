class BankAccount:
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self.balance

    def display_balance(self):
        print(f"${self.balance}")


def format_number(number):
    return "{:,.2f}".format(number)


Adrian = BankAccount('Adrian', 'Fletnok', 25421542, 'Savings', 1253, 1397.50)
Alec = BankAccount('Alec', 'Rudisill', 25121543, 'Savings', 2532, 11389141551.62)
accounts = {Adrian.account_id: Adrian, Alec.account_id: Alec}

account_id = int(input("Enter your account ID: "))


if account_id in accounts:
    account = accounts[account_id]
    pin = int(input("Enter your pin: "))
    if pin == account.pin:
        print(f"Welcome {account.first_name} {account.last_name}")
        print(f"Account ID: {account.account_id}")
        print(f"Balance: ${format_number(account.balance)}")
        ans = input("What transaction would you like to make?: ")
        if ans == "withdraw":
            amount = float(input("How much?: "))
            account.withdraw(amount)
            print(f"${format_number(amount)} has been withdrawn from your account. Your new balance is ${format_number(account.balance)}")
        elif ans == "deposit":
            amount = float(input("How much?: "))
            account.deposit(amount)
            print(f"${format_number(amount)} has been deposited into your account. Your new balance is ${format_number(account.balance)}")
        else:
            print("Invalid transaction")
    else:
        print("Incorrect pin")
else:
    print("This account does not exist.")
