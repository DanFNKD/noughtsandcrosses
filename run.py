# Welcome message

print("Welcome to Noughts and Crosses!")
print("Let's play:")

def create_board():
    """
    Created the board
    Function returns a dictionary that represents
    the board.
    """
    board = {
    '1': ' ', '2': ' ', '3': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '7': ' ', '8': ' ', '9': ' ',
    }
    return board

def print_board(board):
    """
    Prints the Noughts and Crosses board.
    """
    print(' ' + board['1'] + ' | ' + board['2'] + ' | ' + board['3'] + ' ')
    print('---+---+---')
    print(' ' + board['4'] + ' | ' + board['5'] + ' | ' + board['6'] + ' ')
    print('---+---+---')
    print(' ' + board['7'] + ' | ' + board['8'] + ' | ' + board['9'] + ' ')

board = create_board()

print_board(board)

def check_winner(board, player):
    """
    Checks if the player has won.
    Returns True if the player wins and false if not.
    """
    winning_combos = [
        ['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'] # Rows
        ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9'] # Columns
        ['1', '5', '9'], ['3', '5', '7'] # Diagonals
    ]
    for combo in winning_combos:
        if all(board[pos] == player for pos in combo):
            return True
    return False