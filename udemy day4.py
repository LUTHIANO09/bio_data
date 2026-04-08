import random
#task 1
print("welcome to my head or tail game ")

select= int(input("kindly select a num from 1 to 10 "))
random_= random.randint(0,10)
print(random_)

if select == random_:
    print("Head")
else:
    print("Tail")

if select == random_:
    print("you just won $500")
else:
    print("you just loose your stake")


#task2 random list

import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

randx= random.randint(0,4)
print(friends[randx])

#second option
print(random.choice(friends))

#Quiz

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][0])