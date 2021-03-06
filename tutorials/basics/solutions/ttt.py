import math

turn = 'X'
round_ended = False
game_ended = False
board = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]


def print_board():
    for row in board:
        for col in row:
            print(col, end=" ")
        print()


def check(a, b, c):
    return a == b == c and not a == '-'


def check_for_win():
    # checking columns
    for x in range(0, 3):
        if check(board[x][0], board[x][1], board[x][2]):
            return board[x][0]
        if check(board[0][x], board[1][x], board[2][x]):
            return board[0][x]
    # checking diagonals
    if check(board[0][0], board[1][1], board[2][2]) or check(board[2][0], board[1][1], board[0][2]):
        return board[1][1]


while not game_ended:
    while not round_ended:
        row = int(input(
            f'Player {turn}, enter a row to place your marker [0, 2]: '))
        col = int(input(
            f'Player {turn}, enter a column to place your marker [0, 2]: '))
        if board[row][col] != '-':
            print('You cannot place a marker at that location!')
            continue
        board[row][col] = turn
        print_board()
        win = check_for_win()
        turn = 'O' if turn == 'X' else 'X'
        if(win):
            print(f'Congratulations, player {win} won the game!')
            round_ended = True
    play_again = input('Would you like to play again? (y / n): ')
    if play_again == 'y':
        round_ended = False
        board = [['-', '-', '-'],
                 ['-', '-', '-'],
                 ['-', '-', '-']]
    else:
        game_ended = True
