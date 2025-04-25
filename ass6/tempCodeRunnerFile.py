import random

class RPS:
    user_win = 0
    comp_win = 0
    draw = 0
    pick = ["R","P","S"]
    def __init__(self , rounds):
        self.rounds = rounds
        for i in range(rounds):
            self.comp_choice = random.choice(self.pick)
            print("Enter R for Rock,P for Paper and S for Scissors for Round ",self.user_win + self.comp_win + self.draw + 1,": ")
            s = input()
            print("Computer choice : ",self.comp_choice)
            if(s == "R"): #user picks rock
                if(self.comp_choice == "P"):
                    self.comp_win += 1
                elif(self.comp_choice == "S"):
                    self.user_win += 1
                else:
                    self.draw += 1
            elif(s == "P"): #user picks paper
                if(self.comp_choice == "P"):
                    self.draw += 1
                elif(self.comp_choice == "S"):
                    self.comp_win += 1
                else:
                    self.user_win += 1
            else: #user picks scissors
                if(self.comp_choice == "P"):
                    self.user_win += 1
                elif(self.comp_choice == "S"):
                    self.draw += 1
                else:
                    self.comp_win += 1
        if(self.comp_win > self.user_win):
            print("Computer wins!")
        elif(self.comp_win < self.user_win):
            print("User wins!")
        else:
            print("Draw!")
        print("Score : " ,self.comp_win , " - " , self.user_win)

r = int(input("Enter number of rounds you want to play : "))
game = RPS(r)