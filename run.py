import random

# Welcome message



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
        ['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], # Rows
        ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9'], # Columns
        ['1', '5', '9'], ['3', '5', '7'] # Diagonals
    ]
    for combo in winning_combos:
        if all(board[pos] == player for pos in combo):
            return True
    return False

def player_move(board):
    """
    Gets and validates player's move.
    Updates the board with the player's move.
    """
    while True:
        move = input("Enter your move (1-9): ")
        if move in board.keys() and board[move] == ' ':
            return move
        else:
            print("Not a valid move. Please try again.")

def computer_move(board):
    """
    Generates computer's move.
    Randomly selects an available position on the board.
    """
    available_moves = []
    for pos in board.keys():
        if board[pos] == ' ':
            available_moves.append(pos)
    
    return random.choice(available_moves)

    def main():
        print("Welcome to Noughts and Crosses!")
        player_name = input("Please enter your name: ")
        print(f"Good luck {player_name}. Let's play!\n")

