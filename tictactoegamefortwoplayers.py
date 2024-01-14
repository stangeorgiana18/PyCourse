

def display_board(board):
    #print('\n'*100)
    print(board[1] + '|' + board[2] + '|' + board[3])
    print("-----")
    print(board[4] + '|' + board[5] + '|' + board[6])
    print("-----")
    print(board[7] + '|' + board[8] + '|' + board[9])

test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)


def player_input():
    
    marker = ''

    # keep asking player to choose X or 0
    while marker != 'X' and marker != '0':
        marker = input("Player 1, choose X or 0: ")

        # assign player 2 the opposite marker
        player1 = marker
        if player1 == 'X':
            player2 = '0'
        else:
            player2 = 'X'


    return (player1, player2)
    
player1, player2 = player_input()
print(f"Player 1 plays with: {player1}")
print(f"Player 2 plays with: {player2}")


def place_marker(board, marker, position):
    
    board[position] = marker

place_marker(test_board,'$',8)
display_board(test_board)

def win_check(board, mark):

    # check all rows for same markers
    # marker matches check for columns
    # diagonals check for match
    return((board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or (board[7] == mark and
    board[8] == mark and board[9] == mark) or (board[1] == board[4] == board[7] == mark) 
    or (board[2] == board[5] == board[8] == mark) or (board[3] == board[6] == board[9] == 
    mark) or (board[1] == board[5] == board[9] == mark) or (board[3] == board[5] == board[7]))

print(win_check(test_board,'X'))
display_board(test_board)

import random

def choose_first():

    flip = random.randint(0, 1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

print(choose_first())

def space_check(board, position):

    return board[position] == ' '

def full_board_check(board):

    for i in range(1, 10):
        # if I have a space
        if space_check(board, i):
            return False
    
    # board is full, return true
    return True 

def player_choice(board):

    # position 0 because nothing is there
    position = 0 
    while position not in list(range(1, 10)) or not space_check(board, position):
        position = int(input("Choose a position: (1-9): "))

def replay():

    choice = input("Play again? Enter Yes or No.")

    return choice == 'Yes'










