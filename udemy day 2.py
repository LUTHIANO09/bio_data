print("Welcome to the tip calculator")
bill= float(input("what was the total bill $"))
tip= int(input("how much tip would you like to give ? 10, 12, 0r 15"))
split= int(input("how many people to split the bill"))



print("Each person should pay: $")

print("Welcome to the tio Calculator")
bill=float(input("What was the total bill ? $\n"))
tip=int(input("How much tip would you like to give? 10,12, or 15?\n"))
split=int(input("how many people to split the bill?\n"))
tip_percent= tip/100
total_tip= bill * tip_percent
total_bill= bill + total_tip
bill_per_person= total_bill/split
final_amount= round(bill_per_person,2)
print(f"each person should pay: ${final_amount}")