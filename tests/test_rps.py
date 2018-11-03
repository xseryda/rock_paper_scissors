import pytest

from OpenAltPyTest import rps


@pytest.mark.parametrize('input_value, return_value', [
    ('rock', True), ('paper', True), ('scissors', True),
    ('lizard', False), ('Spock', False)
])
def test_is_valid_play(input_value, return_value):
    assert rps.check_input(input_value) is return_value


def test_computer_play_is_valid():
    for _ in range(5000):
        assert rps.check_input(rps.get_computer_input())


def test_computer_plays_randomly():
    generated_tests = [rps.get_computer_input() for _ in range(5000)]
    rocks = generated_tests.count('rock')
    papers = generated_tests.count('paper')
    scissors = generated_tests.count('scissors')
    print(rocks, papers, scissors)
    assert rocks > 500
    assert papers > 500
    assert scissors > 500


@pytest.mark.parametrize('user_input, cpu_input, return_value', [
    ('rock', 'paper', -1), ('rock', 'scissors', 1), ('rock', 'rock', 0),
    ('paper', 'scissors', -1), ('paper', 'rock', 1), ('paper', 'paper', 0),
    ('scissors', 'rock', -1), ('scissors', 'paper', 1), ('scissors', 'scissors', 0)
])
def test_rps(user_input, cpu_input, return_value):
    for input_value in [user_input, cpu_input]:
        assert rps.check_input(input_value)
    assert rps.compare_choices(user_input, cpu_input) == return_value


def main():
    test_rps()


if __name__ == '__main__':
    main()
