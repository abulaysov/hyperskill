import re
import random


def print_table():
    print('---------')
    for i in table:
        print('|', *i, '|')
    print('---------')


def win(board, le):
    return (board[0][0] == le and board[0][1] == le and board[0][2] == le) or\
            (board[1][0] == le and board[1][1] == le and board[1][2] == le) or\
            (board[2][0] == le and board[2][1] == le and board[2][2] == le) or\
            (board[0][0] == le and board[1][0] == le and board[2][0] == le) or\
            (board[0][1] == le and board[1][1] == le and board[2][1] == le) or\
            (board[0][2] == le and board[1][2] == le and board[2][2] == le) or\
            (board[0][0] == le and board[1][1] == le and board[2][2] == le) or \
            (board[2][0] == le and board[1][1] == le and board[0][2] == le)


def valid(x):
    """validation check"""
    if re.match(r'[\d]{1} [\d]{1}', x):
        return True
    return False


def end_game(letter):
    """Checking if the game is complete"""
    if win(table, letter):
        print(f'{letter} wins')
        return True
    elif finish():
        print('Draw')
        return True
    return False


def easy(symbol, sym2=None):
    """ easy level of complexity"""
    print('Making move level "easy"')
    while True:
        move = [random.randint(0, 2), random.randint(0, 2)]
        if table[move[0]][move[1]] == ' ':
            table[move[0]][move[1]] = symbol
            break


def finish():
    """check if the playing field is full"""
    for i in table:
        if ' ' in i:
            return False
    return True


def player_comp(letter_human, letter_comp, mod=None, human=True):
    """simulates a fight between a human and a bot"""
    while True:
        if human:
            move = input('Enter the coordinates: ')
            if valid(move):
                move = list(map(lambda x: int(x) - 1, move.split(' ')))
                if max(move) <= 2 and min(move) >= 0:
                    if table[move[0]][move[1]] == ' ':
                        table[move[0]][move[1]] = letter_human
                        human = False
                        print_table()
                        if end_game(letter_human):
                            break
                    else:
                        print('This cell is occupied! Choose another one!')
                else:
                    print('Coordinates should be from 1 to 3!')
            else:
                print('You should enter numbers!')
        else:
            mod(letter_comp, letter_human)
            print_table()
            human = True
            if end_game(letter_comp):
                break


def comp_comp(letter_x, letter_o, mod1, mod2):
    """simulates a fight between bots"""
    first = True
    while True:
        if first:
            mod1(letter_x, letter_o)
            print_table()
            first = False
        else:
            mod2(letter_o, letter_x)
            print_table()
            first = True
        if end_game(letter_x):
            break
        elif end_game(letter_o):
            break


def get_table_copy():
    table_copy = []
    for i in table:
        table_copy.append(i.copy())
    return table_copy


def check_the_winnings(le):
    """check if he wins by making a move"""
    for i in range(3):
        for j in range(3):
            copy_table = get_table_copy()
            if copy_table[i][j] == ' ':
                copy_table[i][j] = le
                if win(copy_table, le):
                    return i, j
    return False


def medium(symbol, sym2):
    """medium difficulty level"""
    print('Making move level "medium"')
    ind = check_the_winnings(sym2)
    if ind:
        table[ind[0]][ind[1]] = symbol
    else:
        while True:
            move = [random.randint(0, 2), random.randint(0, 2)]
            if table[move[0]][move[1]] == ' ':
                table[move[0]][move[1]] = symbol
                break


def hard(symbol, sym2):
    """hard level"""
    print('Making move level "hard"')
    for i in range(3):
        for j in range(3):
            copy_table = get_table_copy()
            if copy_table[i][j] == ' ':
                copy_table[i][j] = symbol
                if win(copy_table, symbol):
                    table[i][j] = symbol
                    return True
    ind = check_the_winnings(sym2)
    if ind:
        table[ind[0]][ind[1]] = symbol
    else:
        if table[1][1] == ' ':
            table[1][1] = symbol
        elif (table[0][0] + table[0][2] + table[2][0] + table[2][2]).count(' '):
            angels = [(0, 0), (0, 2), (2, 0), (2, 2)]
            random.shuffle(angels)
            for i in angels:
                if table[i[0]][i[1]] == ' ':
                    table[i[0]][i[1]] = symbol
                    break
        else:
            mid = [(0, 1), (1, 0), (1, 2), (2, 1)]
            random.shuffle(mid)
            for i in mid:
                if table[i[0]][i[1]] == ' ':
                    table[i[0]][i[1]] = symbol
                    break


levels = {'easy': easy, 'medium': medium, 'hard': hard}
command = input('Input command: ')
while command != 'exit':
    if re.match(r'start (hard|easy|user|medium) (hard|easy|user|medium)$', str(command)):
        table = [[' ' for j in range(3)] for i in range(3)]
        print_table()
        command = command.split()
        if 'user' not in command:
            comp_comp('X', 'O', levels[command[1]], levels[command[2]])
        elif command[1] == 'user':
            player_comp('X', 'O', levels[command[2]])
        else:
            player_comp('O', 'X', levels[command[1]])
    else:
        print('Bad parameters! ')
    command = input('Input command: ')
