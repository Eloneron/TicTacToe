"""
Tic Tac Toe, initial release 01.08.2021
Project started 16.07.2021
---------------------------------------
Popular game in console version. 2 players or 1 player vs basic AI.

Release notes:
Coordinates grid could be more standardised!
There are two ways in which AI may sometimes lose.
In general, algorithm is close to average human performance.

Copyright Robert Pralicz 2021
"""
import random
import numpy as np
import AI


def show_board(state):
    """Function to print board of given state with a coord grid"""

    print('\n   1   2   3')
    print(f'a  {state[0][0]} | {state[0][1]} | {state[0][2]} ')
    print(f'  -----------')
    print(f'b  {state[1][0]} | {state[1][1]} | {state[1][2]} ')
    print(f'  -----------')
    print(f'c  {state[2][0]} | {state[2][1]} | {state[2][2]} \n')


def update_board(move, board):
    """Function to update a board. Only to be used after checking coordinates for validity
    Move col coord in 1,2,3 """
    if move[2] == 1:
        player = 'O'
    else:
        player = 'X'

    board[['a', 'b', 'c'].index(move[1])][int(move[0]) - 1] = player

    return board


def check_winner(board):
    """Function to check if there is a winner on current state of board
    Provide a board, returns X or O or False or Draw"""

    # 1. Check diagonals
    if board[0][0] != ' ' and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]

    if board[0][2] != ' ' and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    # 2. Check rows
    for row in board:
        if row[0] != ' ' and row[0] == row[1] == row[2]:
            return row[0]

    # 3. Check columns:
    for row in board.T:  # iterating through columns = iterating through rows of transposed array
        if row[0] != ' ' and row[0] == row[1] == row[2]:
            return row[0]

    # 4. Check for draw:
    if ' ' not in board:
        return 'Draw'

    # If no match, return False
    return False


def get_move(player, board):
    """Function to get and validate player's move or display help."""

    while True:
        move = input(f'Player {player} turn: ').lower()
        if move == 'help':
            print('Enter your move in format "1a" (up to "3c")')
            continue
        # Check if user input is 2 characters long
        if len(move) == 2:
            # print('len OK')
            # Check if user input is in correct format and range
            if move[0] in ['1', '2', '3'] and move[1] in ['a', 'b', 'c']:
                # print('format and range OK')
                # Check if chosen field is not occupied
                if board[['a', 'b', 'c'].index(move[1])][int(move[0]) - 1] == ' ':
                    # print('Free field OK')
                    # update_board(int(move[0]), ['a', 'b', 'c'].index(move[1]))
                    return move[0], move[1], player

        print('Incorrect format or field already occupied. Try Again.')
        continue


def change_player(player):
    """Function to switch players before next move"""

    if player == 1:
        player = 2
    else:
        player = 1

    return player


# Main loop
while True:
    AI.corner = None
    AI.new_corner = None

    game_mode = input('Player vs AI or 2 players? (1/2): ')
    # Computer will always be player 2 (X)

    # Randomly pick who is first to move
    player = random.choice([1, 2])

    # Reset board
    board = np.array([[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']])

    # Match loop
    while True:
        show_board(board)
        if game_mode == '1' and player == 2:
            move = AI.move(board)
        else:
            move = get_move(player, board)
        board = update_board(move, board)
        winner = check_winner(board)
        if winner:
            show_board(board)
            if winner == "Draw":
                print('Draw!')
                break
            print(f'{winner} wins!')
            break
        else:
            player = change_player(player)

    # After the game is finished, ask for continuation
    again = input('Do you want to play again? (y/n): ')
    if again == 'n':
        print('Goodbye!')
        break
