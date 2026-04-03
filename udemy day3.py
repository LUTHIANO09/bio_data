#Task 1
print("Welcome to the rollercoaster!")
height = float(input("What is your height in cm? "))

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

#Task 3 nested IF/ELSE
if height >= 120:
    print("you are partially eligible to ride the rollercoaster ")
    age= int(input("enter your age: "))
    if age <= 12:
        print("please Pay $5")
    elif age <= 18:
        print("please pay $7.5")
    elif age >18:
    print("pleas pay $12.5 ")

