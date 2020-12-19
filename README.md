# Simple ATM Controller

#### Installation
```
git clone https://github.com/timkim0713/ATMController
python ATM.py
```


#### Instruction
The file contains simple user interactino for running tests. As described in the code, the file's sample test data has 1 Bank, 4 Accounts, and 1 ATM of that Bank.
Bank itself does not take any arguments, but the accounts take 3 parameters of account number, pin number, balance. As Accounts belong to Bank, their association is also handled with 
addData or addAccount method from Bank. There, cardNumber and Account is needed for the relationship.

Sample Test Data are as follows.

Data 1 <br>
Account= bankAccount1,
Bank= bank1,
AccountNumber= 111111,
PinNumber= 1010,
Balance= 1500,
CardNumber= 1111

Data 2 <br>
Account= bankAccount2,
Bank= bank1,
AccountNumber= 222222,
PinNumber= 2020,
Balance= 2500,
CardNumber= 2222

Data 3 <br>
Account= bankAccount3,
Bank= bank1,
AccountNumber= 333333,
PinNumber= 3030,
Balance= 5000,
CardNumber= 3333

Data 4 <br>
Account= bankAccountTest,
Bank= bank1,
AccountNumber= 444444,
PinNumber= 4040,
Balance= 7700,
CardNumber= 4444

