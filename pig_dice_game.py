
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

    



