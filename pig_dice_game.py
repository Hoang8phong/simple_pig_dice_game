# Run the game until a player wins
# Player 1 takes a turn
#   Roll a die
#   if roll == 1
#       Turn point = 0
#       Turn ends
#   Else
#       Add roll to the turn points
#       Ask the user if they want to roll again?
#       if yes, repeat
#       else, turn ends and we return turn points
#
# Update player1 point
# print static
# check if player 1 win
# if yes, terminate the game
# otherwise we swap players
# import random
#
# print("Welcome to Pig Dice Game")
# player1_score = 0
# player2_score = 0
#
# while True:
#     # Player 1 turn
#     print("----- Player's 1 turn -----")
#     turn_score = 0
#     while True:
#         player1_roll = random.randint(1, 6)
#         print("Player 1 roll: ", player1_roll)
#         player1_score += player1_roll
#
#         if player1_roll == 1:
#             print("Player 1 roll a 1, turn over.!")
#             print("Player 1 score: ", player1_score)
#             turn_score = 0
#             break
#         else:
#             turn_score += player1_roll
#             print("Current score: ", player1_score)
#             player1_choice = input("Play again? (y/n): ").lower()
#             if player1_choice == "n":
#                 print("Current score: ", player1_score, "turn over.")
#                 break
#
#     print("----- Player 2 turn -----")
#     while True:
#         player2_roll = random.randint(1, 6)
#         print("Player 2 roll: ", player2_roll)
#         player2_score += player2_roll
#
#         if player2_roll == 1:
#             print("Player 2 roll a 1, turn over.!")
#             print("Player 2 score: ", player2_score)
#             break
#         else:
#             print("Current score: ", player2_score)
#             player2_choice = input("Play again? (y/n): ").lower()
#             if player2_choice == "n":
#                 print("Current score: ", player2_score, "turn over.")
#                 break

import random

player1_score = 0
player2_score = 0
winning_score = int(input("Choose your winning score (10 - ...): "))

while True:
    # Player 1 turn
    print("\n----- Player 1's Turn -----")
    turn_score = 0
    while True:
        roll = random.randint(1, 6)
        print(f"Player 1 rolled a {roll}")

        if roll == 1:
            print("Rolled a 1! Turn over. No points this round.")
            turn_score = 0
            break
        else:
            turn_score += roll
            print(f"Current turn score: {turn_score}")
            choice = input("Roll again? (y/n): ")
            if choice.lower() != 'y':
                break

    player1_score += turn_score
    print(f"Player 1 total score: {player1_score}")

    if player1_score >= winning_score:
        print("Player 1 wins!")
        break

    # Player 2 turn
    print("\n----- Player 2's Turn -----")
    turn_score = 0
    while True:
        roll = random.randint(1, 6)
        print(f"Player 2 rolled a {roll}")

        if roll == 1:
            print("Rolled a 1! Turn over. No points this round.")
            turn_score = 0
            break
        else:
            turn_score += roll
            print(f"Current turn score: {turn_score}")
            choice = input("Roll again? (y/n): ")
            if choice.lower() != 'y':
                break

    player2_score += turn_score
    print(f"Player 2 total score: {player2_score}")

    if player2_score >= winning_score:
        print("Player 2 wins!")
        break

    



