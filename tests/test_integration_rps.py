import sys
import os
import subprocess

import pytest

from OpenAltPyTest import rps


def make_fake(input_fake):
    def input_faked(prompt):  # monkey patching
        print(prompt)
        return input_fake
    return input_faked


# Does not work with new parameter input in functions
# @pytest.fixture(params=['rock', 'paper', 'scissors'])
# def fake_input_rock(request, monkeypatch):
#     monkeypatch.setattr('builtins.input', make_fake(request.param))
#
#
# def test_full_game_a(capsys, fake_input_rock):  # fixtures used - capsys, fake_input_rock - automatic call
#     rps.main()
#     captured = capsys.readouterr()
#     assert 'rock, paper, or scissors?' in captured.out


@pytest.mark.parametrize('fake_input', [
    'rock', 'paper', 'scissors'])
def test_with_fake_input(fake_input, capsys):
    rps.main(input=make_fake(fake_input))
    captured = capsys.readouterr()
    assert 'rock, paper, or scissors?' in captured.out


def test_wrong_play_results_in_repeated_question():
    # cp = subprocess.run(['python', './OpenAltPyTest/rps.py'], encoding='utf-8', stdout=subprocess.PIPE)
    cp = subprocess.run([sys.executable, './OpenAltPyTest/rps.py'], encoding='utf-8', stdout=subprocess.PIPE,
                        check=True, input='Spock\nrock\n')  # enforce correct python usage
    #  text=True misto encoding='...' pro Python 3.7

    assert cp.stdout.count('rock, paper, or scissors?') == 2


@pytest.mark.parametrize('user_input, cpu_input, return_value', [
    ('rock', 'paper', 'Computer won.'), ('rock', 'scissors', 'User won.'), ('rock', 'rock', "It's a tie!"),
    ('paper', 'scissors', 'Computer won.'), ('paper', 'rock', 'User won.'), ('paper', 'paper', "It's a tie!"),
    ('scissors', 'rock', 'Computer won.'), ('scissors', 'paper', 'User won.'), ('scissors', 'scissors', "It's a tie!")
])
def test_play(user_input, cpu_input, return_value):
    computer_played = None
    while computer_played != cpu_input:
        cp = subprocess.run([sys.executable, './OpenAltPyTest/rps.py'], encoding='utf-8', stdout=subprocess.PIPE,
                            check=True, input=user_input+'\n')
        if cp.stdout.splitlines()[0].rstrip().endswith(cpu_input):
            computer_played = cpu_input

    assert cp.stdout.splitlines()[1].rstrip() == return_value
