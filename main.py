## This is a Battleboats game, that uses boats placed on an 8 by 8 grid, placed by the player, that are later hit by a different player, if they guess the placement of the boats correcttly. 

play = False
playinput = str(input("Would you Like to Play. Enter Y or N: "))
if playinput == "Y":
  play = True
elif playinput == "N":
  play = False
  print ("We hope you play another day")
else:
  print ("Please enter Y or N")

while play == True:
  print ("Welcome To BATTLEABOATS! ")
  ("\n")
  print ("-Menu-")
  ("\n")
  print ("1. New Game")
  print ("2. Continue Game")
  print ("3. Information")
  print ("4. Quit")
  play = False