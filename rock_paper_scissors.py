import random

def get_choices():
    player_choice = input('Enter a choice (rock, paper, scissors): ')
    options = ['rock','paper','scissors']
    computer_choice = random.choice(options)
    choices = {'player': player_choice,'computer': computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player==computer:
        return "It's a tie"
    elif player == 'rock':
        if computer == 'scissors':
            return "Player wins"
        else: return 'Computer wins'
    elif player == 'paper':
            if computer == 'scissors':
                return "Computer wins"
            else: return 'Player wins'

choices = get_choices()
result = check_win(choices['player'],choices['computer'])
print(result)