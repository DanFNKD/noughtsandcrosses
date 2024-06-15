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