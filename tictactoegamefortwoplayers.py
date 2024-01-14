

def display_board(board):
    print('\n'*100)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def player_input():
    
    marker = ''

    # keep asking player to choose X or 0
    while not (marker == 'X' or marker == '0'):
        marker = input("Player 1, choose X or 0: ").upper()

    if marker == 'X':
        return ('X', '0')
    else:
        return ('0', 'X')


def place_maker(board, marker, position):
    
    board[position] = marker


def win_check(board, mark):

    # check all rows for same markers
    # marker matches check for columns
    # diagonals check for match
    return((board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or (board[7] == mark and
    board[8] == mark and board[9] == mark) or (board[1] == board[4] == board[7] == mark) 
    or (board[2] == board[5] == board[8] == mark) or (board[3] == board[6] == board[9] == 
    mark) or (board[1] == board[5] == board[9] == mark) or (board[3] == board[5] == board[7]))


import random

def choose_first():

    flip = random.randint(0, 1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):

    # check availability of a place of the board
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
    
    return position


def replay():

    choice = input("Play again? Enter Yes or No: ")

    return choice == 'Yes'


print('Welcome to Tic Tac Toe!')

# while loop to keep running the game

while True:

    # play the game

    # set everything up (board, who's first, choose markers)
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first!')

    play_game = input('Ready to play? y or n?: ')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    # game play
        
    while game_on:

        if turn == 'Player 1':
            
            # show the board
            display_board(the_board)
            # choose a position
            position = player_choice(the_board)
            # place the marker on the position
            place_maker(the_board, player1_marker, position)

            # check if they won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 has won!!')
                game_on = False
            else:
                # or check if there is a tie
                # check if the board is full
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie game!')
                    game_on = False
                else:
                    # no tie and no win? then text player's turn
                    turn = 'Player 2'

        else:
        
            # player two turn
            # show the board
            display_board(the_board)
            # choose a position
            position = player_choice(the_board)
            # place the marker on the position
            place_maker(the_board, player2_marker, position)

            # check if they won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has won!!')
                game_on = False
            else:
                # or check if there is a tie
                # check if the board is full
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie game!')
                    game_on = False
                else:
                    # no tie and no win? then text player's turn
                    turn = 'Player 1'

    # break out of the while loop on replay()
    if not replay():
        break

