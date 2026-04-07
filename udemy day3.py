#Task 1
print("Welcome to the rollercoaster!")
height = float(input("What is your height in cm? "))
bill= 0
#if height >= 120:
    #print("you are partially eligible to ride the rollercoaster ")
#else:
    #print("sorry!! you are \"NOT\" eligible to ride the rollercoaster")

#Task 2
##ent= int(input("kindly enter a number(1-9): "))

#if ent % 2 == 0:
    #print("\"Even\"")
#else:
    #print("\"Odd\"")

#Task 3 nested if/else and elif
#if height >= 120:
    #print("you are partially eligible to ride the rollercoaster ")
    #age= int(input("enter your age: "))
    #if age <= 12:
        #print("please Pay $5")
    #elif age <= 18:
        #print("please pay $7.5")
    #elif age > 18:
        #print("pleas pay $12.5 ")
#else:
    #print("sorry!! you are \"NOT\" eligible to ride the rollercoaster")

#Task4 multiple if
if height >= 120:
    print("you are partially eligible to ride the rollercoaster ")
    age= int(input("enter your age: "))
    if age <= 12:
        bill= 5
        print("children ticket are $5")
    elif age <= 18:
        bil= 7
        print("Youth ticket are $7")
    elif age > 18:
        bill= 12
        print("Adult ticket are $12 ")

    want_a_photo= input("Do you want a photo? enter Y for yes and N for no ")
    if want_a_photo == "y" or "Y":
        bill = bill + 3
        print(f"your final bill is ${ bill}")
else:
    print("sorry!! you are \"NOT\" eligible to ride the rollercoaster")

#Task 4
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

if size == "S":
    bill = bill + 15
elif size == "M":
    bill = bill + 20
elif size == "L":
    bill = bill + 25
else:
    print("Sorry, please enter S, M, or L")


if pepperoni == "Y":
    if size == "S":
        bill = bill + 2
    else:
        bill = bill + 3
if extra_cheese == "Y":
    bill = bill + 1

    print("Your total bill is $" + str(bill))


#Task 5

print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
print("you're at a cross road. where do you want to go?")
Type= input("Type \"left\" or \"right\" ")

if Type== "left":
    if Type == "left" or "Left":
     print("you've come to a lake. there is an island in the middle of the lake."
           "\n type \"wait\" to wait for a boat. Type \"swim\" to swim across the lake.")
    wait= input("swim or wait ")
    if wait == "wait":
        print("you arrive at the island unharmed. there is a house with 3 doors. "
              "\n One red, one yellow and one blue. which colour do you choose?")
        door= input("choose the door ")
        if door =="yellow" or "Yellow":
            print("you found the treasure You Win!")
        elif door =="Blue" or "blue":
            print("Eaten by beasts.\nGame Over.")
        elif door =="Red" or "red":
            print("Burned by fire.\nGame Over.")
        else:
            print("Game Over")
    else:
        print("Attacked by trout.\nGame Over.")
else:
    print("Fall into a hole.\nGame Over.")

