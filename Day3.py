print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

L_R = input('You are at a crossroad. Where do you want to go? "left" or "right" ')
L_R = L_R.lower()

if L_R == "left":
    W_S = input('You came to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across: ')
    W_S = W_S.lower()
    if W_S ==  "wait":
       colour = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which colour do you choose? ')
       colour = colour.lower()
       if colour == "blue": 
           print("You enter a room of beasts. Game Over...")
       elif colour == "yellow":
           print("You Win!")
       elif colour == "red":
           print("It's a room full of fire. Game Over...")
       else:
           print("You choose a door that doesn't exist. Game Over...")

    else:
        print("You got attacked by an angry trout. Game Over...")   

else:
    print("You fell into a hole. Game Over...")
