## This is a Battleboats game, that uses boats placed on an 8 by 8 grid, placed by the player, that are later hit by a different player, if they guess the placement of the boats correcttly. 
import sys
#Defining the Variables
gamestart = 0
#Defines The Empty Board
board = [[" ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " "]]
#Creates The Lines in The Board


def displayboard(board):
    print(" ", board[0][0], "│", board[0][1], "│", board[0][2], "│", board[0][3], "│", board[0][4], "│", board[0][5], "│", board[0][6], "│", board[0][7])
    print(" ───┼───┼───┼───┼───┼───┼───┼───")
    print(" ", board[1][0], "│", board[1][1], "│", board[1][2], "│", board[1][3], "│", board[1][4], "│", board[1][5], "│", board[1][6], "│", board[1][7])
    print(" ───┼───┼───┼───┼───┼───┼───┼───")
    print(" ", board[2][0], "│", board[2][1], "│", board[2][2], "│", board[2][3], "│", board[2][4], "│", board[2][5], "│", board[2][6], "│", board[2][7])
    print(" ───┼───┼───┼───┼───┼───┼───┼───")
    print(" ", board[3][0], "│", board[3][1], "│", board[3][2], "│", board[3][3], "│", board[3][4], "│", board[3][5], "│", board[3][6], "│", board[3][7])
    print(" ───┼───┼───┼───┼───┼───┼───┼───")
    print(" ", board[4][0], "│", board[4][1], "│", board[4][2], "│", board[4][3], "│", board[4][4], "│", board[4][5], "│", board[4][6], "│", board[4][7])
    print(" ───┼───┼───┼───┼───┼───┼───┼───")
    print(" ", board[5][0], "│", board[5][1], "│", board[5][2], "│", board[5][3], "│", board[5][4], "│", board[5][5], "│", board[5][6], "│", board[5][7])
    print(" ───┼───┼───┼───┼───┼───┼───┼───")
    print(" ", board[6][0], "│", board[6][1], "│", board[6][2], "│", board[6][3], "│", board[6][4], "│", board[6][5], "│", board[6][6], "│", board[6][7])
    print(" ───┼───┼───┼───┼───┼───┼───┼───")
    print(" ", board[7][0], "│", board[7][1], "│", board[7][2], "│", board[7][3], "│", board[7][4], "│", board[7][5], "│", board[7][6], "│", board[7][7])

#Defining the subroutine information, holds the information on what the game is.
def information():
  print("This is a Battleboats game. This game uses boats placed on an 8 by 8 grid, placed by the player, that are later hit by a different player, if they guess the placement of the boats correcttly. The game ends when one players boats are all destroyed.")
def grid():
  print ("Here is the grid you will be playing on!")
  print (board)
#Deciding if the player wants to play. 
while gamestart == 0:
  play = False
  playinput = str(input("Would you Like to Play. Enter Yes or No: "))
  playinput = playinput.upper()
  #Depending on the user input, a different output will be displayed, ie Y = Start the game.
  if playinput == "YES" or playinput == "Y":
    play = True
    gamestart += 1
  elif playinput == "NO" or playinput == "N":
    play = False
    print ("We hope you play another day")
    print ("\n")
  else:
    print ("Please enter Y or N")
    print ("\n")


#Checks if the play variable is true. If it is, game starts. Defined by the inputs above. 
menuchoice = 0
while menuchoice == 0:
  ("\n")
  print ("---Welcome To BATTLEABOATS!--- ")
  print ("\n")
  print ("-Menu-")
  print ("1. New Game")
  print ("2. Continue Game")
  print ("3. Information")
  print ("4. Quit")
  print ("\n")
  print ("\n")
  playchoice = str(input("What Number would you like to choose: "))
  if playchoice == "1":
    print ("New Game!")
    menuchoice += 1
    print (displayboard(board))
  elif playchoice == "2":
    print ("Continue Game!")
    menuchoice += 1
  elif playchoice == "3":
    print ("-Here is the Information!-")
    print ("\n")
    menuchoice += 1
    #Calls the information
    information()
  elif playchoice == "4":
    print("The game will now shut down")
    menuchoice += 1
    sys.exit()
  else:
    print ("Please enter a number from the list, 1 - 4")
    print ("\n")
    print ("\n")



playerinput =int (input("What would you like to input: "))
if playerinput == 1:
  board[0][0] = "X"