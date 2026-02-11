import random
from IPython.display import clear_output


# ---------------- FUNCTIONS ---------------- #

def display_board(board):
    clear_output()  # Works in Jupyter. Remove if using normal Python.
    
    print('    |    |')
    print(' ' + board[7] + '  | ' + board[8] + '  | ' + board[9])
    print('    |    |')
    print('----|----|----')
    print('    |    |')
    print(' ' + board[4] + '  | ' + board[5] + '  | ' + board[6])
    print('    |    |')
    print('----|----|----')
    print('    |    |')
    print(' ' + board[1] + '  | ' + board[2] + '  | ' + board[3])
    print('    |    |')


def player_input():
    marker = ''
    while marker not in ['X', 'O']:
        marker = input("Player 1: Choose X or O: ").upper()
    
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return (
        (board[1] == board[2] == board[3] == mark) or
        (board[4] == board[5] == board[6] == mark) or
        (board[7] == board[8] == board[9] == mark) or
        (board[1] == board[4] == board[7] == mark) or
        (board[2] == board[5] == board[8] == mark) or
        (board[3] == board[6] == board[9] == mark) or
        (board[1] == board[5] == board[9] == mark) or
        (board[3] == board[5] == board[7] == mark)
    )


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0
    while position not in range(1, 10) or not space_check(board, position):
        try:
            position = int(input("Choose a position (1-9): "))
        except:
            position = 0
    return position


def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def replay():
    choice = input("Play Again? Enter Yes or No: ")
    return choice.lower().startswith('y')


# ---------------- GAME LOOP ---------------- #

print("Welcome to Tic Tac Toe!")

while True:
    the_board = [' '] * 10
    display_board(the_board)

    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + " will go first.")

    play_game = input("Ready to play? Enter Y or N: ")

    if not play_game.lower().startswith('y'):
        break

    game_on = True

    while game_on:

        # PLAYER 1 TURN
        if turn == 'Player 1':
            display_board(the_board)
            print("Player 1's Turn")
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)

            if win_check(the_board, player1_marker):
                display_board(the_board)
                print("🎉 Player 1 Wins!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("It's a Tie!")
                    break
                else:
                    turn = 'Player 2'

        # PLAYER 2 TURN
        else:
            display_board(the_board)
            print("Player 2's Turn")
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)

            if win_check(the_board, player2_marker):
                display_board(the_board)
                print("🎉 Player 2 Wins!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("It's a Tie!")
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
