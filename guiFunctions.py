import random

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

def comp_rand_gen():
    return random.choice(list(options.keys()))


def gui_winner_loser(human_choice, comp_choice):
    if ((human_choice == 'Rock' and comp_choice in ['Paper', 'Spock']) or
        (human_choice == 'Paper' and comp_choice in ['Scissors', 'Lizard']) or
        (human_choice == 'Scissors' and comp_choice in ['Rock', 'Spock']) or
        (human_choice == 'Spock' and comp_choice in ['Lizard', 'Paper']) or
        (human_choice == 'Lizard' and comp_choice in ['Scissors', 'Rock'])):
        return "Lose"
    elif human_choice == comp_choice:
        return "Tie"
    else:
        return 'Win'


def close_program():
    quit()


def btn_press(btn_press, results, player_score, tie_score, computer_score):
    global options,comp_score,human_score,ties
    if btn_press in list(options.keys()):
        comp = comp_rand_gen()
        res = gui_winner_loser(btn_press,comp)
        if res == 'Lose':
            comp_score += 1
            results.configure(text=f"Computer's {comp} {options[comp][btn_press]} {btn_press}\n\nYou Lose")
            computer_score.configure(text=f'Computer\n\n{comp_score}')
        elif res == 'Tie':
            ties += 1
            results.configure(text=f"Your {btn_press} {options[btn_press][comp]} {comp}\n\nIt's a Tie")
            tie_score.configure(text=f'Ties\n\n{ties}')
        else:
            human_score += 1
            results.configure(text=f"Your {btn_press} {options[btn_press][comp]} {comp}\n\nYou Won!")
            player_score.configure(text=f'Player\n\n{human_score}')


def reset_scores(player_score, tie_score, computer_score):
    global comp_score,human_score,ties
    comp_score = 0
    human_score = 0
    ties = 0
    player_score.configure(text=f'Player\n\n{human_score}')
    tie_score.configure(text=f'Ties\n\n{ties}')
    computer_score.configure(text=f'Computer\n\n{comp_score}')