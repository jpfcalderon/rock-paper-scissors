'''
Created on May 12, 2020

@author: ITAUser
'''
import random

keepPlaying = True

while(keepPlaying == True):
    print("Welcome to the rock paper scissors!")
    print("Best 2 out of 3, press q to quit.")

playerScore = 0
computerScore = 0

while(playScore < 2 and computerScore > 2) 
    print("Welcome")
    print("First to 2 wins. Press q to quit.")
    #rock is 1, paper is 2, scissors is 3

    scoreComp = 0
    scorePlayer = 0

    while(scorePlayer < 2) and (scoreComp < 2):
        choiceComp = random.randint(1,3)
        choicePlayer = input("pick either rock, paper, or scissors!")

        if(choicePlayer == "q"):
            keepPlaying = False
            break
        elif((choicePlayer == "rock" ) and (choiceComp == 1)) or ((choicePlayer == "paper" ) and (choiceComp == 2)) or ((choicePlayer == "scissors" ) and (choiceComp == 3)):
            print("DRAAAW!")
            print("Computer's Score: ", + scoreComp)
            print("Your Score: ", + scorePlayer)

        elif((choicePlayer == "rock" ) and (choiceComp == 2)) or ((choicePlayer == "paper" ) and (choiceComp == 3)) or ((choicePlayer == "scissors" ) and (choiceComp == 1)):
            print("Uh oh, you missed")
            scoreComp = scoreComp + 1
            print("Computer's Score: ", + scoreComp)
            print("Your Score: ", + scorePlayer)
        elif((choicePlayer == "rock" ) and (choiceComp == 3)) or ((choicePlayer == "paper" ) and (choiceComp == 1)) or ((choicePlayer == "scissors" ) and (choiceComp == 2)):
            print("YOU WON THIS ROUND")
            scorePlayer = scorePlayer + 1
            print("Computer's Score: ", + scoreComp)
            print("Your Score: ", + scorePlayer)
        else :
            print("ROCK PAPER OR SCISSORS!")

    if (scorePlayer == 2):
            print("GOOD GAME!")


    if (scoreComp == 2):
            print("YOU LOSE!")

    print("Computer's Score: ", + scoreComp , "Your Score: ", + scorePlayer) 
