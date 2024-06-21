import random


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
        ['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'],  # Rows
        ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9'],  # Columns
        ['1', '5', '9'], ['3', '5', '7']  # Diagonals
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


def check_tie(board):
    """
    Checks if the game is a tie.
    Does so by checking if the board is filled and if
    there has been a winner.
    """
    if ' ' in board.values():
        return False

    if check_winner(board, 'X') or check_winner(board, 'O'):
        return False

    return True


def get_player_name():
    """
    Ensures the player enters at least one non-space character.
    Returns a valid player name.
    """
    while True:
        player_name = input("Please enter your name: ")
        if player_name.strip():
            return player_name
        else:
            print("Please enter a valid name.")


def new_game():
    """
    Offers the player the chance to play another
    game of Noughts and Crosses.
    """
    while True:
        response = input("Do you want to play again? (yes/no): ").lower()
        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            return False
        else:
            print("Invalid input. Please enter 'yes', 'y', 'no' or 'n'.")


def main():
    print("Welcome to Noughts and Crosses!")
    player_name = get_player_name()
    print(f"Good luck {player_name}. Let's play!\n")

    while True:
        board = create_board()
        print_board(board)

        player_symbol = 'X'
        computer_symbol = 'O'

        while True:
            # Player's move
            player_move_pos = player_move(board)
            board[player_move_pos] = player_symbol
            print_board(board)

            # Check for player win
            if check_winner(board, player_symbol):
                print(f"Congratulations {player_name}! You've won the game!\n")
                break

            # Check for tie
            if check_tie(board):
                print("It's a tie. What not play again?\n")
                break

            # Computer's move
            print("Computer's turn:")
            computer_move_pos = computer_move(board)
            board[computer_move_pos] = computer_symbol
            print_board(board)

            # Check for computer win
            if check_winner(board, computer_symbol):
                print(f"Computer wins! Unlucky {player_name}!")
                break

            # Check for tie
            if check_tie(board):
                print("It's a tie. What not play again?\n")
                break

        # Asking if the player wants to play again
        if not new_game():
            print("Thanks for playing!")
            return
        else:
            print("\nStarting a new game...\n")


main()
