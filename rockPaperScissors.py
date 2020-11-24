import random


def play():
    player = input("'r' for rock, 's' for scissors, 'p' for paper\n")
    computer = random.choice(['r', 'p', 's'])

    if player == computer:
        return 'It\'s a tie'

    # r > s, s > p, p > r
    if win(player, computer):
        return 'You won!'
    return 'You lost!'


def win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r

    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


print(play())
