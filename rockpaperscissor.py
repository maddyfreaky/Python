import random

class rps:
    def __init__(self):
        self.game=["Rock","Paper","Scissor"]
        self.userp=0
        self.comp=0

        print("_______"*3,"Welcome to Rock Paper Scissor!!!","_______"*3)
        print()
        print("_______"*4,"Best of 3 wins!","_______"*4)
        print("\n")
    def start(self):
        self.user=input("User's Choice:").title()
        self.com=random.choice(self.game)
        
        if self.user==self.com:
            print("Computer:",self.com)
            print("Draw")
            print("\n")
            if self.comp<3 and self.userp<3:
                play.start()
        elif self.user=="Rock" and self.com=="Paper":
            self.comp+=1
            print("Computer:",self.com)
            print("Computer Earned one point!")
            print("\n")
            if self.comp<3 and self.userp<3:
                play.start()
        elif self.user=="Rock" and self.com=="Scissor":
            self.userp+=1
            print("Computer:",self.com)
            print("You've Earned one point!")
            print("\n")
            if self.comp<3 and self.userp<3:
                play.start()
        elif self.user=="Paper" and self.com=="Rock":
            self.userp+=1
            print("Computer:",self.com)
            print("You've Earned one point!")
            print("\n")
            if self.comp<3 and self.userp<3:
                play.start()
        elif self.user=="Paper" and self.com=="Scissor":
            self.comp+=1
            print("Computer:",self.com)
            print("Computer Earned one point!")
            print("\n")
            if self.comp<3 and self.userp<3:
                play.start()
        elif self.user=="Scissor" and self.com=="Paper":
            self.userp+=1
            print("Computer:",self.com)
            print("You've Earned one point!")
            print("\n")
            if self.comp<3 and self.userp<3:
                play.start()
        elif self.user=="Scissor" and self.com=="Rock":
            self.comp+=1
            print("Computer:",self.com)
            print("Computer Earned one point!")
            print("\n")
            if self.comp<3 and self.userp<3:
                play.start()
        else:
            print()
            print("Invalid entry!, try again......")
            print()
            play.__init__()
            play.start()
    def points(self):
        if self.comp==3:
            print("_____"*6,"Sorry you've lost","_____"*6)
        elif self.userp==3:
            print("_____"*5,"Congratulations you've won!!!","_____"*5)
        
      
play=rps()
play.start()
play.points()