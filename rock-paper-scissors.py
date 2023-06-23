import time
import random

options = ['Rock', 'Paper', 'Scisors', 'Spock', 'Lizard']

comp_score = 0

human_score = 0

ties = 0

def main():
    while True:
       choice =  get_input()


    
    


def get_input():
    while True:
        human_choice = input('Select your choice [Rock/Paper/Scissors/Spock/Lizard] or [Quit] to quit: ').title()
        if human_choice in options:
            return human_choice
        elif human_choice == 'Quit':
            close_game()
        else:
            print('Please print valid option [Rock/Paper/Scissors/Spock/Lizard] or [Quit]: ')


def winner_loser(human_choice, comp_choice)
    if (
        (human_choice == 'Rock' and comp_choice == 'Paper', 'Spock') or
        (human_choice == 'Paper' and comp_choice == 'Scisors', 'Lizard') or
        (human_choice == 'Scisors' and comp_choice == 'Rock', 'Spock') or
        (human_choice == 'Spock' and comp_choice == 'Lizard', 'Scisors') or
        (human_choice == 'Lizard' and comp_choice == 'Scisors', 'Rock')
    ):
        return 'You Lose'
    elif human_choice == comp_choice:
        return "Tie"
    else:
        return 'You Win'


options = ['Rock', 'Paper', 'Scisors', 'Spock', 'Lizard']




def close_game():
    print(f'Human Score; {human_score} | Computer Score; {comp_score} | Ties; {ties}')
    time.sleep(5)
    quit()



main()