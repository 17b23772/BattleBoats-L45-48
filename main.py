## This is a Battleboats game, that uses boats placed on an 8 by 8 grid, placed by the player, that are later hit by a different player, if they guess the placement of the boats correcttly. 
#Deciding if the player wants to play. 
play = False
playinput = str(input("Would you Like to Play. Enter Yes or No: "))
playinput = playinput.upper()

#Defining the subroutine information, holds the information on what the game is.
def information():
  print("This is a Battleboats game. This game uses boats placed on an 8 by 8 grid, placed by the player, that are later hit by a different player, if they guess the placement of the boats correcttly. The game ends when one players boats are all destroyed.")

#depending on the user input, a different output will be displayed, ie Y = Start the game.
if playinput == "YES" or playinput == "Y":
  play = True
elif playinput == "NO" or playinput == "N":
  play = False
  ("\n")
  print ("We hope you play another day")
else:
  ("\n")
  print ("Please enter Y or N")
#Checks if the play variable is true. If it is, game starts. Defined by the inputs above. 
while play == True:
  ("\n")
  print ("---Welcome To BATTLEABOATS!--- ")
  ("\n")
  print ("-Menu-")
  ("\n")
  print ("1. New Game")
  print ("2. Continue Game")
  print ("3. Information")
  print ("4. Quit")
  print ("\n")
  print ("\n")
  playchoice = str(input("What Number you like to choose: "))
  if playchoice == "1":
    print ("New Game!")
  elif playchoice == "2":
    print ("Continue Game!")
  elif playchoice == "3":
    print ("-Here is the Information!-")
    print ("\n")
    #Calls the information
    information()
  elif playchoice == "4":
    print("The game will now shut down")
    break
  else:
    print ("Please enter a number from the list, 1 - 4")
  play = False

