print("Welcome to Tip Calculator")
bill= float(input("What was the total bill? $: "))
tip= int(input("how much will you like to tip? 10,12,15: "))
split= int(input("How many people to split the bill?"))
tip_percent=tip/100
total_tip= bill*tip_percent
total_bill= total_tip + bill
splitting= total_bill/split
rounded= round(splitting,2)
print(f"each person should pay ${rounded}")
