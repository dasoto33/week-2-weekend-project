import time
import random

global options, comp_score, human_score, ties

options = ['Rock', 'Paper', 'Scissors', 'Spock', 'Lizard']

comp_score = 0

human_score = 0

ties = 0

def main():
    while True:
        choice =  get_input()
        comp_selection = comp_rand_gen()
        print(f'You chose {choice} and computer chose {comp_selection}\n')
        print(winner_loser(choice, comp_selection))
        print(f'\nHuman Score: {human_score} | Computer Score: {comp_score} | Ties: {ties}\n')
    
    
    
def comp_rand_gen():
    return  options[random.randint(0,4)]

def get_input():
    while True:
        human_choice = input('Select your choice [Rock/Paper/Scissors/Spock/Lizard] or [Quit] to quit: ').title()
        if human_choice in options:
            return human_choice
        elif human_choice == 'Quit':
            close_game()
        else:
            print('Please print valid option [Rock/Paper/Scissors/Spock/Lizard] or [Quit]: ')


def winner_loser(human_choice, comp_choice):
    global human_score, comp_score, ties
    if ((human_choice == 'Rock' and comp_choice in ['Paper', 'Spock']) or
        (human_choice == 'Paper' and comp_choice in ['Scisors', 'Lizard']) or
        (human_choice == 'Scisors' and comp_choice in ['Rock', 'Spock']) or
        (human_choice == 'Spock' and comp_choice in ['Lizard', 'Scisors']) or
        (human_choice == 'Lizard' and comp_choice in ['Scisors', 'Rock'])):
        comp_score += 1
        return 'You Lose'
    elif human_choice == comp_choice:
        ties += 1
        return "Tie"
    else:
        human_score += 1
        return 'You Win'


def close_game():
    print(f'Human Score: {human_score} | Computer Score: {comp_score} | Ties: {ties}\n')
    print('Thank you for playing!')
    time.sleep(5)
    quit()


main()