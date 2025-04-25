class Passwords:
    pw = []
    def set_password(self,val):
        if val in self.pw:
            print("Password already used.\n")
        else:
            self.pw.append(val)
    def get_password(self):
        return self.pw[-1]
    def is_correct(self,s):
        return s == self.get_password()
    def display(self):
        print("All passwords are :" , self.pw)

user = Passwords()
pick = 0
while(pick != 4):
    print("Enter your choice\n1. set_password\n2. get_password\n3. is_correct\n4. Exit.\n")
    pick = int(input())
    if(pick == 1):
        pasw = input("Enter new password : ")
        user.set_password(pasw)
    elif(pick == 2):
        s = user.get_password()
        print("The current password is : ",s)
    elif(pick == 3):
        inp = input("Enter password to check : ")
        s = user.is_correct(inp)
        print(s)
    else:
        print("Exit successful")
    user.display()