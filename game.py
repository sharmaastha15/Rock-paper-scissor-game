
import random
options = ("rock","paper","scissor")

playing=True
while playing:
    
    computer = random.choice(options)
    player=None

    while player not in options:
      player=input("enter the choice (rock, paper,scissor):")

    print("player:",player)
    print("computer:",computer)

#winning conditions
    if player==computer:
     print("Its tie!")
    elif player =="rock" and computer== "scissor":
     print("you win!")
    elif player=="scissor" and computer =="rock":
     print("I win!")
    elif  player=="rock" and computer =="paper":
     print("I win!")
    elif  player=="paper" and computer =="scissor":
     print("I win!")
    elif  player=="paper" and computer =="rock":
     print(" you win!")
    else :
     print("you win!")
     
