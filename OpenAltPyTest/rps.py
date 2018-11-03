import random

import click

RPS = ['rock', 'paper', 'scissors']
OUTPUT_STYLE = {1: click.style('User won.', fg='green', bold=True),
                0: click.style("It's a tie!", fg='yellow', bold=True),
                -1: click.style('Computer won.', fg='red', bold=True)}


def get_player_input(input=input):
    human = None
    while not check_input(human):
        human = input('rock, paper, or scissors?')
    return human


def get_computer_input():
    return random.choice(RPS)


def check_input(input_value):
    return input_value in RPS


def compare_choices(user, computer):
    """
    Check if user wins against computer
    :param user: User's choice
    :param computer: Computer's choice
    :return: -1 when computer won, 0 when tied, 1 when user won
    """
    if user == computer:
        return 0
    else:
        c_index = RPS.index(computer) if RPS.index(computer) != 0 else 3  # n+1 wins over n
        h_index = RPS.index(user)
        if c_index-h_index == 1:
            return -1
        else:
            return 1


def main(input=input):
    human = get_player_input(input=input)
    computer = get_computer_input()

    print(computer)

    user_won = compare_choices(human, computer)

    click.echo(OUTPUT_STYLE[user_won])


if __name__ == '__main__':
    main()
