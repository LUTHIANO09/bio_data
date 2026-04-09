import random
# #task 1
# print("welcome to my head or tail game ")
#
# select= int(input("kindly select a num from 1 to 10 "))
# random_= random.randint(0,10)
# print(random_)
#
# if select == random_:
#     print("Head")
# else:
#     print("Tail")
#
# if select == random_:
#     print("you just won $500")
# else:
#     print("you just loose your stake")
#
#
# #task2 random list
#
# import random
# friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
#
# randx= random.randint(0,4)
# print(friends[randx])
#
# #second option
# print(random.choice(friends))
#
# #Quiz
#
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
#
# dirty_dozen = [fruits, vegetables]
#
# print(dirty_dozen[1][0])
#


#DAY 4 FINAL TASK


import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


choose= int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: \n"))
rand= random.randint(0,2)
print("USER CHOOSE: ")
if choose == 0 and rand == 0:
    print(paper)
if choose == 0 and rand == 2:
    print(rock)
elif choose == 1 and rand == 0:
    print(paper)
elif choose == 1 and rand == 2:
    print(scissors)
else:
    print(scissors)

print("COMPUTER CHOOSE: ")

if rand == 0 and choose == 0:
    print(paper)
elif rand == 0 and choose == 1:
    print(rock)
elif rand == 1 and choose == 0:
    print(paper)
elif rand == 1 and choose == 1:
    print(scissors)
else:
    print(scissors)

if choose == 1 and rand == 1:
        print("its a draw")
elif choose == 1 and rand == 2:
        print("you lose")
elif choose == 1 and rand == 0:
        print("you win")
elif choose == 2 and rand == 2:
        print("its a draw")
elif choose == 2 and rand == 0:
    print("you win")
elif choose == 2 and rand == 1:
        print("you lose")
elif choose == 0 and rand == 0:
    print("Its a draw")
elif choose == 0 and rand == 1:
    print("you lose")
elif choose == 0 and rand == 2:
    print("you lose")
elif choose == 1 and rand == 0:
        print("you win")
elif choose == 1 and rand == 2:
        print("you lose")
elif choose == 2 and rand == 1:
        print("you win")
else:
    print("You type an invalid number \'You loose\'")
