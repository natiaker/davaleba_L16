class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def transfer(self, money_amount):
        self.balance += money_amount
        print(f"{self.account_holder}ს ანგარიშზე ({self.account_number}) ჩაირიცხა თანხა {money_amount}ლარი. \n"
              f"ბალანსი შეადგენს: {self.balance} ლარს. \n")


account1 = BankAccount("123456", "ნათია", 1000)
account1.transfer(100)
