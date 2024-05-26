def game():
    choices = ['Rock', 'Paper', 'Scissors']
    player_choice = input("Choose Rock, Paper or Scissors:").capitalise()
    import random
    computer_choice = random.choice(choices)

    print(f"Player chosen: {player_choice}")
    print(f"Computer chosen: {computer_choice}")

    if player_choice == computer_choice:
        print("Draw!")
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
            (player_choice == 'Scissors' and computer_choice == 'Paper') or \
            (player_choice == 'Paper' and computer_choice == 'Rock'):
        print("Playeris won!")
    else:
        print("Lost!")

while True:
    game()
    play_again = input("Do you want to play again? (Yes/No): ").capitalise()
    if play_again != 'Yes':
        break