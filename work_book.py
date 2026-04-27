# # # def check_if(a,b):
# # #     if b in a:
# # #         return "value exist"
# # #     else:
# # #         return "value does not exist"
# # #
# # # a=["pawpaw","pineapple","orange"]
# # # b= "pawpaw"
# # # print(check_if(a,b))
# # #
# # # if 2>1 :
# # #     print("higher")
# # #
# # # variable_1 = "v1"
# # # variable_2 = "v2"
# # # variable_3 = "v3"
# # # variable_4 = "v4"
# # # variable_5 = "v5"
# # #
# # # print(variable_1,variable_2,variable_3,variable_4,variable_5)
# # #
# # # fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# # # newlist = [x for x in range(11) if x <= 5]
# # # #newlist = [x if x != "banana" else "orange" for x in fruits]
# # # #newlist = [x for x in fruits]
# # # print(newlist)
# #
# # # def lst(a):
# # #     fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# # #     return a + float(a)
# # # fruits = ["apple", "banana", "Cherry", "kiwi", "Mango"]
# # # # fruits.sort(key = str.lower)
# # # # print(fruits)
# # #
# # # femz = fruits.copy()
# # # femzz = fruits[1:3]
# # #
# # # nw= []
# # #
# # # for fruit in femz:
# # #     nw.extend(fruit)
# # #
# # # print(nw)
# #
# # # thistuple = ("apple", "banana", "cherry")
# # # y = ("orange",)
# # # w = ("pawpaw",)
# # # #thistuple += y, w
# # # x = list(thistuple)
# # # x.remove("apple")
# # # thistuple = tuple(x)
# # # print(x)
# # #
# # # print(thistuple)
# #
# # # thistuple = ("apple", "banana", "cherry")
# # # for a in range(len(thistuple)):
# # #   print(thistuple[a])
# #
# # thistuple = ("apple", "banana", "cherry")
# # i = 0
# # while i < len(thistuple):
# #   print(thistuple[i])
# #   i += 1
#
#
# #LOVE CALCULATOR
# def calculate_love_score(name1, name2):
#     combine= name1 + name2
#     lower= combine.lower()
#
#     t= lower.count("t")
#     r=lower.count("r")
#     u=lower.count("u")
#     e=lower.count("e")
#     true= t+r+u+e
#
#     l=lower.count("l")
#     o=lower.count("o")
#     v=lower.count("v")
#     e=lower.count("e")
#     love= l+o+v+e
#     score= int(str(true)+str(love))
#     #print(score)
#
# calculate_love_score("olamide", "ayomide")


def pressure_tracker():
    current_max = 0

    def update_max(reading):
        if reading > current_max:
            current_max = reading
            print(current_max)

    update_max(3200)
    update_max(4800)
    update_max(1500)
    print(f'Peak pressure recorded: {current_max} psi')


pressure_tracker()