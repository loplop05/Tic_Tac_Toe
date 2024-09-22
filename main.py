def display_board(board):
    print(f"{board[7]} | {board[8]} | {board[9]}")
    print("---------")
    print(f"{board[4]} | {board[5]} | {board[6]}")
    print("---------")
    print(f"{board[1]} | {board[2]} | {board[3]}")


def player_input():
    marker = input("Enter the side you want (X OR O): ")
    while marker not in ['x', 'o']:
        marker = input('Please enter a correct side (X OR O): ')

    if marker == 'x':
        return ('X', 'O')
    else:
        return ('O', 'X')


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return (
            (board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark)
    )


import random


def choose_first():
    player = random.randint(1, 2)
    return f"Player {player} is gonna start (:"


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = int(input('Choose your next position: (1-9): '))
    while position not in range(1, 10) or not space_check(board, position):
        position = int(input('Full position. Please choose a number in the range of (1-9): '))
    return position


def replay():
    return input('Do you want to continue playing (Y OR N)? ').lower().startswith('y')


print('WELCOME TO TIC TAC TOE GAME (: ')

while True:
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player1_marker, player2_marker = player_input()

    play_game = input('Are you ready to play? Enter Y or N: ')

    if play_game.lower() == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        # Player 1's turn
        display_board(board)
        print("It's Player 1's turn (X)")
        position = player_choice(board)
        place_marker(board, player1_marker, position)

        if win_check(board, player1_marker):
            display_board(board)
            print('Congrats Player 1 won!')
            game_on = False
        else:
            if full_board_check(board):
                print('THE GAME IS A DRAW!')
                break

            # Player 2's turn
            display_board(board)
            print("It's Player 2's turn (O)")
            position = player_choice(board)
            place_marker(board, player2_marker, position)

            if win_check(board, player2_marker):
                display_board(board)
                print('Congrats Player 2 won!')
                game_on = False
            else:
                if full_board_check(board):
                    print('THE GAME IS A DRAW!')
                    break

    if not replay():
        break
