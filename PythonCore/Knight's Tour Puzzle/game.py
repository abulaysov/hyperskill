def data_processing(len_x, len_y):
    x1, y1 = 0, 0
    while True:
        position = input("Enter the knight's starting position: ").split()
        if len(position) != 2:
            print("Invalid dimensions!")
            continue
        try:
            x1, y1 = int(position[0]), int(position[1])
        except Exception:
            print("Invalid dimensions!")
            continue
        if not 1 <= x1 <= len_x or not 1 <= y1 <= len_y:
            print("Invalid dimensions!")
        else:
            break
    return x1, y1


def input_dimension():
    len_x1, len_y1 = 0, 0
    while True:
        dimension = input("Enter your board dimensions: ").split()

        if len(dimension) != 2:
            print("Invalid dimensions!")
            continue
        try:
            len_x1, len_y1 = int(dimension[0]), int(dimension[1])
        except ValueError:
            print("Invalid dimensions!")
            continue
        if len_x1 <= 0 or len_y1 <= 0:
            print("Invalid dimensions!")
        else:
            break
    return len_x1, len_y1


def create_board(len_x, len_y):
    for _i in range(len_x):
        current_row = []
        for _j in range(len_y):
            current_row.append("_")
        board.append(current_row)


def fill_board(board1, index, len_x, len_y):
    for i in range(len_x):
        for j in range(len_y):
            if board1[i][j] == '_' and countr(board1, i + 1, j + 1, str(index), len_x, len_y) != 0:
                board2 = next_move(board1, i + 1, j + 1, index + 1, len_x, len_y)
                if index + 1 == len_x * len_y:
                    return board2
                board3 = fill_board(board2, index + 1, len_x, len_y)
                if board3 is not None:
                    return board3
    return None


def move(board1, new_x1, new_y1, len_x, len_y):
    result = []
    for i in range(len_x):
        current_row = []
        for j in range(len_y):
            if board1[i][j] == 'X':
                current_row.append('*')
            else:
                current_row.append(board1[i][j])
        result.append(current_row)
    result[new_x1 - 1][new_y1 - 1] = "X"
    return result


def countr(board1, x1, y1, symbol, len_x, len_y):
    counter = []
    counter.append(x1 + 1 <= len_x and y1 + 2 <= len_y and board1[x1][y1 + 1] == symbol)
    counter.append(x1 + 1 <= len_x and y1 - 2 > 0 and board1[x1][y1 - 3] == symbol)
    counter.append(x1 - 1 > 0 and y1 + 2 <= len_y and board1[x1 - 2][y1 + 1] == symbol)
    counter.append(x1 - 1 > 0 and y1 - 2 > 0 and board1[x1 - 2][y1 - 3] == symbol)
    counter.append(x1 - 1 > 0 and y1 - 2 > 0 and board1[x1 - 2][y1 - 3] == symbol)
    counter.append(x1 + 2 <= len_x and y1 + 1 <= len_y and board1[x1 + 1][y1] == symbol)
    counter.append(x1 + 2 <= len_x and y1 - 1 > 0 and board1[x1 + 1][y1 - 2] == symbol)
    counter.append(x1 - 2 > 0 and y1 + 1 <= len_y and board1[x1 - 3][y1] == symbol)
    counter.append(x1 - 2 > 0 and y1 - 1 > 0 and board1[x1 - 3][y1 - 2] == symbol)
    return len(list(filter(lambda x: x, counter)))


def next_move(board1, new_x1, new_y1, index, len_x, len_y):
    result = []
    for i in range(len_x):
        current_row = []
        for j in range(len_y):
            current_row.append(board1[i][j])
        result.append(current_row)
    result[new_x1 - 1][new_y1 - 1] = str(index)
    return result


def check_solution(board1, len_x, len_y):
    total = 0
    for i in range(len_x):
        for j in range(len_y):
            if board1[i][j] == '_' and countr(board1, i + 1, j + 1, 'X', len_x, len_y) != 0:
                board2 = move(board1, i + 1, j + 1, len_x, len_y)
                if check_solution(board2, len_x, len_y):
                    return True
            elif board1[i][j] in '*X':
                total += 1
    return total == len_x * len_y


def play(board1, len_x, len_y):
    print_board(board1, len_x, len_y)
    inv = False
    count_squares = 1
    while True:
        if inv:
            mov = input("Invalid move! Enter your next move: ").split()
        else:
            mov = input('Enter your next move: ').split()
        new_x = int(mov[0])
        new_y = int(mov[1])
        if board1[new_x - 1][new_y - 1] != '_' or countr(board1, new_x, new_y, 'X', len_x, len_y) == 0:
            inv = True
        else:
            inv = False
            board1 = move(board1, new_x, new_y, len_x, len_y)
            count_squares += 1
            if countr(board1, new_x, new_y, '_', len_x, len_y) == 0:
                if len_x * len_y == count_squares:
                    print('What a great tour! Congratulations!')
                else:
                    print('No more possible moves!')
                    print(f'Your knight visited {count_squares} squares!')
                break
            print_board(board1, len_x, len_y)


def print_board(board1, len_x, len_y):
    max_len = len(str(len_x * len_y))
    print(" " + "-" * (len_x * (max_len + 1) + 3))
    for i in range(len_y, 0, -1):
        s = ""
        for j in range(1, len_x + 1):
            if board1[j - 1][i - 1] != '_':
                s += " " + " " * (max_len - len(board1[j - 1][i - 1])) + board1[j - 1][i - 1]
            elif countr(board1, j, i, 'X', len_x, len_y) != 0:
                next_count = str(countr(board1, j, i, '_', len_x, len_y))
                s += " " + " " * (max_len - len(next_count)) + next_count
            else:
                s += " " + "_" * max_len
        print(f"{i}|{s} |")
    print(" " + "-" * (len_x * (max_len + 1) + 3))


def print_solution(board1, len_x, len_y):
    board2 = fill_board(board1, 1, len_x, len_y)
    print_board(board2, len_x, len_y)


def main():
    len_x, len_y = input_dimension()
    create_board(len_x, len_y)
    x, y = data_processing(len_x, len_y)
    board[x - 1][y - 1] = "X"
    while True:
        inp = input('Do you want to try the puzzle? (y/n): ')
        match inp:
            case 'y':
                if not check_solution(list(board), len_x, len_y):
                    print('No solution exists!')
                else:
                    play(board, len_x, len_y)
                break
            case 'n':
                if not check_solution(list(board), len_x, len_y):
                    print('No solution exists!')
                else:
                    board[x - 1][y - 1] = "1"
                    print("Here's the solution!")
                    print_solution(board, len_x, len_y)
                break
            case _:
                print('Invalid dimensions!')


if __name__ == '__main__':
    board = []
    main()
