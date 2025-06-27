# program to Implement Rock, Paper, Scissor
import random
l=["rock","Scissor","Paper"]

while True:
    ccount=0
    ucount=0
    uc=int(input('''Game Start
            1. Yes
            2. No/exit
            '''))
    if uc==1:
        for a in range(1,6):
            userInput = int (input('''
            1 Rock
            2 Scissor
            3 Paper
            '''))
            if userInput==1:
                uchoice="rock"
            elif userInput==2:
                uchoice="scissor"
            elif userInput==3:
                uchoice="paper"
            Cchoice=random.choice(l)
            if Cchoice==uchoice:
                print("computer Value: ",Cchoice)
                print("User Value: ",uchoice)
                print("Game Draw")
                ucount=ucount+1
                ccount=ccount+1

            elif (uchoice=="Paper" and Cchoice=="rock") or (uchoice=="rock" and Cchoice=="scissor") or (uchoice=="scissor" and Cchoice=="paper"):
                print("Computer Value: ", Cchoice)
                print("User Value: ", uchoice)
                print("you Win")
                ucount=ucount+1

            else:
                print("Computer Value",Cchoice)
                print("User Value",uchoice)
                print("Computer Win")
                ccount=ccount+1

            break


