class bank:
    history = []
    def __init__(self,acctnum,balance):
        self.acctnum = acctnum
        self.balance = balance
        self.history.append("b:"+str(self.balance))

    def deposit(self,d):
        self.balance += d
        self.history.append("+"+str(d)+" bal:"+str(self.balance))

    def withdraw(self,d):
        if(self.balance < d):
            print("not enough money")
        else:
            self.balance -= d
            self.history.append("-"+str(d)+" bal:"+str(self.balance))
    
    def disp(self):
        print("Current Balance : ",self.balance)
        print("Transaction History : ",self.history)
    
acNUM = int(input("Enter account number : "))
bal = int(input("Enter initial balance : "))
user = bank(acNUM , bal)

pick = 0
while(pick != 4):
    print("What would you like to do?")
    pick = int(input("Enter 1-deposit 2-withdraw 3-display 4-exit : "))
    if(pick == 1):
        d = int(input("Enter the amt you want to deposit : "))
        user.deposit(d)
    elif(pick == 2):
        d = int(input("Enter the amt you want to withdraw : "))
        user.withdraw(d)
    elif(pick == 4):
        print("Exit Successful.")
    else: user.disp()

        