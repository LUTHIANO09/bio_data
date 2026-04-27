import cal


def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(cal.logo)
    first_num = float(input("Enter the first number: \n"))
    choice = input('kindly select  "+", "-", "*" or "/" \n')
    second_num = float(input("Enter the second number: \n"))

    should_accumulate = True
    while should_accumulate:
        if choice == "+":
            result = operation["+"](first_num, second_num)
            print(f"{first_num} {choice} {second_num} = {result}")
            cont = input(f"Did you want to continue with the previous {result} ? yes or no \n").lower()
        elif choice == "-":
            result = operation["-"](first_num, second_num)
            print(f"{first_num} {choice} {second_num} = {result}")
            cont = input(f"Did you want to continue with the {result} ? yes or no \n").lower()
        elif choice == "*":
            result = operation["*"](first_num, second_num)
            print(f"{first_num} {choice} {second_num} = {result}")
            cont = input(f"Did you want to continue with the {result} ? yes or no \n").lower()
        elif choice == "/":
            result = operation["/"](first_num, second_num)
            print(f"{first_num} {choice} {second_num} = {result}")
            cont = input(f"Did you want to continue with {result} ? yes or no \n").lower()
        else:
            print("invalid input")

        if cont == "yes":
            first_num = result
            choice = input('kindly select  "+", "-", "*" or "/" \n')
            second_num = float(input("Enter the second number: \n"))
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()
        # result_2 = operation[choice](first_num, second_num)
        # print(f"{first_num} {choice} {second_num} = {result_2}")


calculator()


# cont = input("Did you want to continue with the previous result? yes or no \n").lower()
# if cont == "yes":
#     work_out(result, second_num)



