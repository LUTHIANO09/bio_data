student_scores = {
    "Harry": 88,
    "Ron": 78,
    "Hermione": 95,
    "Draco": 75,
    "Neville": 60
}

student_grades = {
    "Outstanding": "91 - 100",
    "Exceeds Expectations": "81 - 90",
    "Acceptable": "71 - 80",
    "Fail": "0 - 70",
}

for student in student_scores:
    score = student_scores[student]

    if 91 <= score <= 100:
        grade = "Outstanding"
    elif 81 <= score <= 90:
        grade = "Exceeds Expectations"
    elif 71 <= score <= 80:
        grade = "Acceptable"
    else:
        grade = "Fail"

    print(f"{student}: {grade}")


#blind auction

import art
print(art.logo)

#
# # TODO-1: Ask the user for input
# name= input("What is your name? ")
# price= int(input("What is your Bid?: #"))
#
# bids= {}
# # TODO-2: Save data into dictionary {name: price}
# bids[name] = price
#
#
# # TODO-3: Whether if new bids need to be added
# should_continue = input("Are there any other bidders? Type 'Yes' or 'No'.\n").lower()

def highest_bidder(bidding_dictionary):
    winner=""
    biggest_bid = 0
    for bid in bidding_dictionary:
        bid_amount = bidding_dictionary[bid]
        if bid_amount > biggest_bid:
            biggest_bid = bid_amount
            winner = bid

    print(f"The winner is {winner} with a bid of ${biggest_bid}")


bids= {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name? ")
    price = int(input("What is your Bid?: #"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'Yes' or 'No'.\n").lower()
    if should_continue == "no":
        continue_bidding = False
        highest_bidder(bids)
    elif should_continue == "yes":
        print("\n"*100)


# TODO-4: Compare bids in dictionary

