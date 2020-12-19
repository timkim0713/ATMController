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

#### Note 
Not all the errors are covered in this project for the sake of simplicity.  


#### Sample Data
#### Data 1 <br>
Account= bankAccount1<br>
Bank= bank1<br>
AccountNumber= 111111<br>
PinNumber= 1010<br>
Balance= 1500<br>
CardNumber= 1111<br>

#### Data 2 <br>
Account= bankAccount2<br>
Bank= bank1<br>
AccountNumber= 222222<br>
PinNumber= 2020<br>
Balance= 2500<br>
CardNumber= 2222<br>

#### Data 3 <br>
Account= bankAccount3
Bank= bank1<br>
AccountNumber= 333333<br>
PinNumber= 3030<br>
Balance= 5000<br>
CardNumber= 3333<br>

#### Data 4 <br>
Account= bankAccountTest<br>
Bank= bank1<br>
AccountNumber= 444444<br>
PinNumber= 4040<br>
Balance= 7700<br>
CardNumber= 4444<br>
<br>
 
