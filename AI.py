"""
This is basic AI module for Tic Tac Toe game.
Algorithm behaviour:
1. If board is empty pick a random corner
2. If opposite corner empty pick it
3. If no threat from opponent and any corner left pick it
4. Finish

All other cases are basically avoiding loss.
"""
import random

corner = None
new_corner = None


def validate_move(board, col, row):
    """Function to validate AI generated move. Returns True if move is possible, False if not.
    col coord in 1,2,3 """
    if board[['a', 'b', 'c'].index(row)][int(col) - 1] == ' ':
        return True
    else:
        return False


def check(board, mode):
    """
    Function to check if there is an opportunity for victory or opponent has occupied two fields in one line
    in a way that may lead to his victory in next move (based on 'mode' parameter).
    Returns False if no such threat/opportunity exists or coordinates of suggested move otherwise.
    """
    # Choose mode (threat or win)
    if mode == 'threat':
        mark = 'O'
    else:
        mark = 'X'
    # Check diagonals.
    cols = ['0', '1', '2']
    rows = ['a', 'b', 'c']
    counter = 0  # take account of previously popped items
    for i in range(3):
        if board[i][i] == mark:
            rows.pop(i - counter)
            cols.pop(i - counter)
            counter += 1
    if len(rows) == 1 and validate_move(board, str(int(cols[0]) + 1), rows[0]):
        return str(int(cols[0]) + 1), rows[0]

    cols = ['0', '1', '2']
    rows = ['a', 'b', 'c']
    counter = 0  # take account of previously popped items
    for i in range(3):
        if board[2-i][i] == mark:
            rows.pop(2 - i)
            cols.pop(i - counter)
            counter += 1
    if len(rows) == 1 and validate_move(board, str(int(cols[0]) + 1), rows[0]):
        return str(int(cols[0]) + 1), rows[0]

    # Check rows
    cols = ['0', '1', '2']
    rows = ['a', 'b', 'c']
    for i in range(3):  # rows
        counter = 0
        for j in range(3):  # cols
            if board[i][j] == mark:
                cols.pop(j - counter)
                counter += 1
        if len(cols) == 1 and validate_move(board, str(int(cols[0]) + 1), rows[i]):
            return str(int(cols[0]) + 1), rows[i]
        cols = ['0', '1', '2']

    # Check cols
    cols = ['0', '1', '2']
    rows = ['a', 'b', 'c']
    for i in range(3):  # cols
        counter = 0
        for j in range(3):  # rows
            if board[j][i] == mark:
                rows.pop(j - counter)
                counter += 1
        if len(rows) == 1 and validate_move(board, str(int(cols[i]) + 1), rows[0]):
            return str(int(cols[i]) + 1), rows[0]
        rows = ['a', 'b', 'c']

    return False


def move(board):
    """Function returning AI's move, based on strategy described above and involving threat assessment.
    Note value '2' returned as the last argument denoting that move was performed by player 2, that is AI"""
    global corner, new_corner
    # if board empty, pick random corner
    if 'X' not in board and 'O' not in board:
        row = random.choice(['a', 'c'])
        col = random.choice(['1', '3'])
        corner = (col, row)
        return col, row, 2

    # subtle nuance - if player was first and middle empty - take it
    if 'X' not in board and validate_move(board, '2', 'b'):
        return '2', 'b', 2

    # check for win/lose in next move
    alert = check(board, 'win') or check(board, 'threat')  # prioritize win before threat
    # if alert present, make suggested move
    if alert:
        return alert[0], alert[1], 2

    # check if two opposite corners picked, if so try to pick third
    if new_corner:
        if validate_move(board, corner[0], new_corner[1]):
            return corner[0], new_corner[1], 2

        if validate_move(board, new_corner[0], corner[1]):
            return new_corner[0], corner[1], 2

    # check if corner picked in previous moves, if so pick opposite one if able,
    # if not pick random position - victory improbable
    if corner:
        if corner[0] == '1':
            new_corner = ['3']
        else:
            new_corner = ['1']

        if corner[1] == 'a':
            new_corner.append('c')
        else:
            new_corner.append('a')

        if validate_move(board, new_corner[0], new_corner[1]):
            return new_corner[0], new_corner[1], 2

    while True:
        random_move = [random.choice(['1', '2', '3']), random.choice(['a', 'b', 'c'])]
        if validate_move(board, random_move[0], random_move[1]):
            return random_move[0], random_move[1], 2
