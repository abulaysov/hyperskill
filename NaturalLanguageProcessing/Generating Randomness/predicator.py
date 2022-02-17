import itertools
import random


def line_count(comp_string, user_string):
    global wallet
    total = 0
    for i, j in zip(comp_string, user_string):
        if i == j:
            total += 1
            wallet -= 1
        else:
            wallet += 1
    return total


def format_string(s):
    return ''.join([i for i in s if i in '01'])


def triad(tr, s):
    result, ind = [0, 0], 0
    try:
        while True:
            ind = s.find(tr, ind)
            if ind == -1:
                break
            if s[ind+3] == '0':
                result[0] += 1
            else:
                result[1] += 1
            ind += 1
    except IndexError:
        return result
    return result


def prediction(test_inp):
    computer_result = random.choice(list(triad_dict.keys()))
    for i in range(len(test_inp) - 3):
        char = triad_dict.get(test_inp[i:i + 3], [])
        if char[0] > char[1]:
            computer_result += '0'
        elif char[0] == char[1]:
            computer_result += random.choice('01')
        else:
            computer_result += '1'
    return computer_result


def read_input():
    result = ''
    while True:
        inp = input('Print a random string containing 0 or 1:')
        result += format_string(inp)
        if len(result) >= 100:
            break
        print(f'Current data length is {len(result)}, {100 - len(result)} symbols left')
    print(f'Final data string:\n{result}')
    return result


if __name__ == '__main__':
    print('Please give AI some data to learn...')
    triad_dict = {}
    final_string = read_input()
    for i in itertools.product('01', repeat=3):
        triad_dict[''.join(i)] = triad(''.join(i), final_string)
    print('You have $1000. Every time the system successfully predicts your next press, you lose $1.')
    print("""Otherwise, you earn $1. Print "enough" to leave the game. Let"s go!""")
    wallet = 1000
    while True:
        try:
            test_string = input('Print a random string containing 0 or 1:\n')
            if test_string == 'enough':
                print('Game over')
                break
            predict_string = prediction(test_string)
            right_digits = line_count(predict_string[3:], test_string[3:])
            percent = right_digits / len(predict_string[3:]) * 100
            print('prediction:', predict_string, sep='\n')
            print(f'Computer guessed right {right_digits} out of {len(test_string) - 3} symbols ({percent} %)')
            print(f'Your balance is now ${wallet}')
        except IndexError:
            ...
