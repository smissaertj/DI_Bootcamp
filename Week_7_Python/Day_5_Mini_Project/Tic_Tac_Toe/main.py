"""
Create a TicTacToe game in python, where two users can play together.

1. The game is played on a grid that’s 3 squares by 3 squares.
2. Players take turns putting their marks (O or X) in empty squares.
3. The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.
4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.

"""

# Matrix which holds the board data - initialize as empty
board_data = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]


def display_board(data):
    """ Draw the board borders and data on screen """

    print('*************')
    print('* ' + data[0][0] + ' | ' + data[0][1] + ' | ' + data[0][2] + ' *')
    print('------------')
    print('* ' + data[1][0] + ' | ' + data[1][1] + ' | ' + data[1][2] + ' *')
    print('------------')
    print('* ' + data[2][0] + ' | ' + data[2][1] + ' | ' + data[2][2] + ' *')
    print('*************\n')


def update_board_data(*player_data):
    """ Update the board_data global variable with the player input """

    row, column, mark = player_data
    board_data[row][column] = mark
    display_board(board_data)


def player_input(player, player_mark):
    """ Capture player input """

    print(f'{player}\'s turn...')

    row = int(input('Enter row number: ')) - 1
    column = int(input('Enter column number: ')) - 1

    if 'X' in board_data[row][column] or 'O' in board_data[row][column]:
        print('You cannot overwrite a previously set marker.')
    else:
        update_board_data(row, column, player_mark)


def check_win(marker):
    """ We need to check for 8 conditions to determine a winner:
        Horizontal row 1, row 2 and row 3
        Vertical column 1, column 2 and column 3
        Diagonal top left to bottom right
        Diagonal top right to bottom left
    """

    return \
        board_data[0][0] == marker and board_data[0][1] == marker and board_data[0][2] == marker or \
        board_data[1][0] == marker and board_data[1][1] == marker and board_data[1][2] == marker or \
        board_data[2][0] == marker and board_data[2][1] == marker and board_data[2][2] == marker or \
        board_data[0][0] == marker and board_data[1][0] == marker and board_data[2][0] == marker or \
        board_data[0][1] == marker and board_data[1][1] == marker and board_data[2][1] == marker or \
        board_data[0][2] == marker and board_data[1][2] == marker and board_data[2][2] == marker or \
        board_data[0][0] == marker and board_data[1][1] == marker and board_data[2][2] == marker or \
        board_data[0][2] == marker and board_data[1][1] == marker and board_data[2][0] == marker


def play():
    player_x = input('Player X, what is your name? ')
    player_o = input('Player O, what is your name? ')

    turn_count = 1
    while turn_count <= 10:
        print(f'\nRound {turn_count}!')
        if turn_count % 2 == 0:
            player_input(player_x, 'X')
            winner = check_win('X')
        else:
            player_input(player_o, 'O')
            winner = check_win('O')
        turn_count += 1

        if winner:
            print('Congrats, we have a winner!')
            break
    else:
        # No more turns are left, so all 9 squares have a value
        print('Game Tie!')


play()
