import time
import random
from os import system

options = {'Rock': {'Rock': 'bounced off',
                    'Scissors': 'crushed',
                    'Lizard': 'crushed'},
            'Paper': {'Rock': 'covers',
                    'Paper': "didn't even scratch",
                    'Spock': 'disproved'},
            'Scissors': {'Paper': 'sliced right through',
                    'Scissors': 'sharpened',
                    'Lizard': 'decapitated'},
            'Spock': {'Rock': 'vaporized',
                    'Scissors': 'smashed',
                    'Spock': 'had a beer with'},
            'Lizard': {'Paper': 'swallowed',
                    'Spock': 'poisoned',
                    'Lizard': 'fell in love with'}}
comp_score = 0
human_score = 0
ties = 0

def main():
    while True:
        choice =  get_input()
        comp_selection = comp_rand_gen()
        print(winner_loser(choice, comp_selection))
        print(f'Human Score: {human_score} | Computer Score: {comp_score} | Ties: {ties}\n')
    
    
    
def comp_rand_gen():
    return random.choice(list(options.keys()))

def get_input():
    while True:
        human_choice = input('Select your choice [Rock/Paper/Scissors/Spock/Lizard] or [Quit] to quit: ').title()
        if human_choice in list(options.keys()):
            return human_choice
        elif human_choice == 'Quit':
            close_game()
        else:
            print('Please print valid option [Rock/Paper/Scissors/Spock/Lizard] or [Quit]: ')


def winner_loser(human_choice, comp_choice):
    global human_score, comp_score, ties
    if ((human_choice == 'Rock' and comp_choice in ['Paper', 'Spock']) or
        (human_choice == 'Paper' and comp_choice in ['Scissors', 'Lizard']) or
        (human_choice == 'Scissors' and comp_choice in ['Rock', 'Spock']) or
        (human_choice == 'Spock' and comp_choice in ['Lizard', 'Paper']) or
        (human_choice == 'Lizard' and comp_choice in ['Scissors', 'Rock'])):
        comp_score += 1
        return f"\nComputer's {comp_choice} {options[comp_choice][human_choice]} {human_choice}\nYou Lose\n"
    elif human_choice == comp_choice:
        ties += 1
        return f"\nYour {human_choice} {options[human_choice][comp_choice]} {comp_choice}\nIt's a Tie\n"
    else:
        human_score += 1
        return f'\nYour {human_choice} {options[human_choice][comp_choice]} {comp_choice}\nYou Win\n'
    


def close_game():
    print(f'Human Score: {human_score} | Computer Score: {comp_score} | Ties: {ties}\n')
    print('Thank you for playing!')
    time.sleep(5)
    quit()


main()