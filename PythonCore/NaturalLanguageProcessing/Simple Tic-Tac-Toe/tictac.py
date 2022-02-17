import re


def print_table():
    print('---------')
    for i in l:
        print('|', *i, '|')
    print('---------')



def win():
    winner = ''
    if (table[0][0] == 'X' and table[0][1] == 'X' and table[0][2] == 'X') or\
            (table[1][0] == 'X' and table[1][1] == 'X' and table[1][2] == 'X') or\
            (table[2][0] == 'X' and table[2][1] == 'X' and table[2][2] == 'X') or\
            (table[0][0] == 'X' and table[1][0] == 'X' and table[2][0] == 'X') or\
            (table[0][1] == 'X' and table[1][1] == 'X' and table[2][1] == 'X') or\
            (table[0][2] == 'X' and table[1][2] == 'X' and table[2][2] == 'X') or\
            (table[0][0] == 'X' and table[1][1] == 'X' and table[2][2] == 'X') or \
            (table[2][0] == 'X' and table[1][1] == 'X' and table[0][2] == 'X'):
        winner += 'X'

    if (table[0][0] == 'O' and table[0][1] == 'O' and table[0][2] == 'O') or\
            (table[1][0] == 'O' and table[1][1] == 'O' and table[1][2] == 'O') or\
            (table[2][0] == 'O' and table[2][1] == 'O' and table[2][2] == 'O') or\
            (table[0][0] == 'O' and table[1][0] == 'O' and table[2][0] == 'O') or\
            (table[0][1] == 'O' and table[1][1] == 'O' and table[2][1] == 'O') or\
            (table[0][2] == 'O' and table[1][2] == 'O' and table[2][2] == 'O') or\
            (table[0][0] == 'O' and table[1][1] == 'O' and table[2][2] == 'O') or \
            (table[2][0] == 'O' and table[1][1] == 'O' and table[0][2] == 'O'):
        winner += 'O'

    return winner



def finish():
    for i in l:
        if ' ' in i:
            return False
    return True


def valid(x):
    if re.match(r'[123]{1} [123]{1}', x):
        return True
    return False


l = [[' ' for j in range(3)] for i in range(3)]
print_table()
flag = True
while win() == '' :
    if finish():
        print('Draw')
        break
    elif flag:
        hod = input('Enter the coordinates: ')
        if valid(hod):
            hod = list(map(lambda x: int(x)-1, hod.split(' ')))
            if l[hod[0]][hod[1]] == ' ':
                l[hod[0]][hod[1]] = 'X'
                flag = False
                print_table()
            else:
                print('This cell is occupied! Choose another one!')
        else:
            print('You should enter numbers!')
    else:
        hod = input('Enter the coordinates: ')
        if valid(hod):
            hod = list(map(lambda x: int(x)-1, hod.split(' ')))
            if l[hod[0]][hod[1]] == ' ':
                l[hod[0]][hod[1]] = 'O'
                flag = True
                print_table()
            else:
                print('This cell is occupied! Choose another one!')
        else:
            print('You should enter numbers!')
else:
    print(f'{win()} wins')
