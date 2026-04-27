import random
import art



def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    """takes a list of cards and calculates the score"""
    if sum(cards) == 21 and  len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) == 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(use_score, comp_score):
    if use_score == comp_score:
        return "DRAW"
    elif comp_score == 0:
        return "loose opponent has blackjack"
    elif use_score == 0:
        return "Win with a blackjack"
    elif use_score > 21:
        return "you went over. you loose"
    elif comp_score > 21:
        return "opponent went over. you win"
    elif use_score > comp_score:
        return "you win"
    else:
        return "you loose"

def play_game():
    print(art.logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"your cards: {user_cards}, current score: {user_score}")
        print(f"computer's first card is {computer_cards[0 ]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal= input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"your final hand: {user_cards}, current score: {user_score}")
    print(f"computer final hand: {computer_cards}, final score: {computer_score}")
    print(compare(computer_score, user_score))
while input("Do you want to play a game of blackjack? Type 'y' or 'n': ") ==  "y":
    print("\n" * 20)
    play_game()