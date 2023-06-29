# import random function to use in the program
import random

# list of options 
options=["Rock", "Paper", "Scissors", "Lizard", "Spock"]



game=0 # allows for the game to be repeated
while (game!=1):
  game=input("Lets play a game (press any key to continue, or q to quit) ")
  if game.upper()=="Q": #If the user enters a "q" or a "Q" for their question, the loop will end 
    print("Thanks for playing!")
    game=1 #makes the while loop false
  else:
    #player makes a choice, while the cpu randomly selects from the list
    player=input("Rock, Paper, Scissors, Lizard, or Spock? ")
    cpu=(random.choice(options))

    # changes the user input into a comparable form with the computer, takes into account capitalization 
    if (player).upper() == 'ROCK':
      player = "Rock"
    elif (player).upper() == 'PAPER':
      player = "Paper"
    elif (player).upper() == 'SCISSORS':
      player = "Scissors"
    elif (player).upper() == 'LIZARD':
      player = "Lizard"
    elif (player).upper() == 'SPOCK':
      player = "Spock"

    # if players doesn't type in a requested option, this message will appear
    elif (player != "Rock", "Paper", "Scissors", "Lizard", "Spock"):
      print("That is not an available option, please pick something else")

    # takes into account of ties
    if (cpu == player):
      print("You Tied")

    elif (cpu != player):
      while (player=="Rock"):
        if (cpu == "Paper" or cpu=="Spock"):
          print ("You Lose!")
          # change the value of player so it doesn't print "You Lose!" forever
          player=0
        else:
          print ("You Win!")
          # same for here when the player wins the game 
          player=0 
        
      while (player=="Paper"):
        if (cpu == "Scissors" or cpu=="Lizard"):
          print ("You Lose!")
          player=0
        elif (cpu == "Rock" or "Spock"):
          print ("You Win!")
          player=0
        
      while (player=="Scissors"):
        if (cpu == "Rock" or cpu=="Spock"):
          print ("You Lose!")
          player=0
        else:
          print ("You Win!")
          player=0
        
      while (player =="Lizard"):
        if (cpu == "Rock" or cpu=="Scissor"):
          print ("You Lose!")
          player=0
        else:
          print ("You Win!")
          player=0

      while (player=="Spock"):
        if (cpu == "Paper" or cpu=="Lizard"):
          print ("You Lose!")
          player=0
        else:
          print ("You Win!")
          player=0
