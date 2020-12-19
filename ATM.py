# Daekyung Kim
# timkim0713@gmail.com
# Simple ATM Controller in Python 3.8.6


class Bank:
    def __init__(self):
        self.bankData = {}
        # {cardNumber: BankAccount}

    def addAccount(self, cardNumber, BankAccount):
        if cardNumber in self.bankData:
            self.bankData[cardNumber] = BankAccount

    def addData(self, cardNumber, BankAccount):
        self.bankData[cardNumber] = BankAccount

    def checkPinNumber(self, cardNumber, inputPinNumber):
        if cardNumber in self.bankData and self.bankData[cardNumber].getPinNumber() == inputPinNumber:
            return True
        else:
            return False

    def updateAccountData(self, cardNumber, balance):
        if self.bankData[cardNumber].getAccountNumber() in self.bankData.keys():
            self.bankData[cardNumber].setBalance(balance)
            return True
        else:
            return False

    def getBankAccount(self, cardNumber):
        return self.bankData[cardNumber]


# account / balance, deposit, withdraw
class BankAccount:

    def __init__(self, accountNumber, pinNumber, balance):
        self.accountNumber = accountNumber
        self.pinNumber = pinNumber
        self.balance = balance

    def __str__(self):
        return str(self.accountNumber)

    def getBalance(self):
        print(f"Your current balance is ${self.balance}")

    def setBalance(self, newBalance):
        self.balance = newBalance

    def deposit(self, amount):
        amount = int(amount)
        print(f"Depositing... ${amount}")
        self.balance += amount
        print(f"Balance before: ${self.balance - amount}")
        print(f"Balance now: ${self.balance}")

    def withdraw(self, amount):
        amount = int(amount)
        if self.balance < amount:
            print(f"${amount} is more than your balance to withdraw.")
        else:
            print(f"Withdrawing... ${amount}")
            self.balance -= amount
            print(f"Balance before: ${self.balance + amount}")
            print(f"Balance now: ${self.balance}")

    def getPinNumber(self):
        return self.pinNumber

    def setPinNumber(self, pin):
        print(f"Your pin number is now set to {pin}")
        self.pinNumber = pin

    def getAccountNumber(self):
        return self.accountNumber

    def setAccountNumber(self, accountNumber):
        print(f"Your account number is now set to {accountNumber}")
        self.accountNumber = accountNumber


class ATMController:
    def __init__(self, bank):  # cash bin future implementation
        self.bank = bank
        self.account = None
        self.cashBin = 0

    def insertCard(self, cardNumber, pinNumber):
        if self.bank.checkPinNumber(cardNumber, pinNumber):
            self.account = self.bank.bankData[cardNumber]
            return True
        else:
            return False  # INVALID

    def selectAccount(self, account):
        if account == self.account:
            return account
        else:
            return None

    def selectActions(self, cardNumber, account, action, amount):
        if action == "withdraw":

            self.account.withdraw(amount)
            self.bank.updateAccountData(
                cardNumber, self.account.getBalance())

            self.cashBin = amount  # --------------cashbin has "amount"
            print(
                f"The withdrawn cash ${amount} can be found at the cash bin of the ATM.")

        elif action == "deposit":
            self.account.deposit(amount)
            self.bank.updateAccountData(
                cardNumber, self.account.getBalance())

            self.cashBin = amount  # --------------cashbin receives "amount"

        elif action == "check balance":
            self.account.getBalance()


# Simple run of the ATM Controller
if __name__ == "__main__":

    # ----------Params -----accountNumber, pinNumber, balance
    # 2 ways to generate bank/account data in this system.
    # 1. Generating Sample Bank Accounts
    bankAccount1 = BankAccount(111111, 1010, 1500)
    bankAccount2 = BankAccount(222222, 2020, 2500)
    bankAccount3 = BankAccount(333333, 3030, 5000)
    # 2. Generating Bank Account for addAccount method testing
    bankAccountTest = BankAccount(444444, 4040, 7700)

    # New bank
    bank1 = Bank()

    # 1a. Generating data directly into the bank.
    bank1.addData(1111, bankAccount1)  # cardnumber,bankAccount
    bank1.addData(2222, bankAccount2)  # cardnumber,bankAccount
    bank1.addData(3333, bankAccount3)  # cardnumber,bankAccount

    # 2a. Generating only Card, empty account.
    bank1.addData(4444, None)
    # 2b. Adding account to the bank with only card.
    bank1.addAccount(4444, bankAccountTest)

    print("Welcome to ATM1.")

    userCardNumber = int(input("Insert a card (Enter the card number) \n"))
    userPinNumber = int(input("Enter your 4 digits PIN number \n"))

    # New ATM of bank1
    atm1 = ATMController(bank1)  # bank

    if atm1.insertCard(userCardNumber, userPinNumber):
        print("Verified PIN number for your card.")
        print("----------------------------------")
        print("Your account number \n", atm1.account, "\n")

        if atm1.selectAccount(atm1.account):
            userAccountNumber = input(
                "Enter the account number you want to navigate with \n")
            userSelectedAccount = bank1.getBankAccount(userCardNumber)
            userAction = ""
            while(userAction != "leave"):
                userAction = input(
                    "Enter your action: Check Balance, Deposit, Withdraw, Leave \n")
                userAction = userAction.lower()

                if(userAction == "deposit"):
                    userAmount = input(
                        "Place the cash to deposit in the cash bin / Enter the amount to deposit\n")
                elif userAction == "withdraw":
                    userAmount = input("Enter the amount to withdraw \n")
                else:
                    userAmount = 0

                if(userAction != "leave"):
                    atm1.selectActions(
                        userCardNumber, userSelectedAccount, userAction, userAmount)
            print("Bye.")

        else:
            print("That account is not available.")
    else:
        print("Not a valid PIN number for your card.")
