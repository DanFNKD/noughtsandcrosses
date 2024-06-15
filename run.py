# Welcome message

print("Welcome to Noughts & Crosses!")
print("Let's play:")

def create_board():
    """
    Created the board
    Function returns a dictionary that represents
    the board
    """
    board = {
    '1': ' ', '2': ' ', '3': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '7': ' ', '8': ' ', '9': ' ',
}
return board

def print_board(board):
    """
    Prints the Noughts & Crosses board
    """
    print(' ' + board['1'] + ' | ' + board['2'] + ' | ' + board['3'] + ' ')
    print('---+---+---')
    print(' ' + board['4'] + ' | ' + board['5'] + ' | ' + board['6'] + ' ')
    print('---+---+---')
    print(' ' + board['7'] + ' | ' + board['8'] + ' | ' + board['9'] + ' ')

print_board(board)
    