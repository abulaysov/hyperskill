# write your code here
import random
import re


def easy():
    count = 0
    for i in range(5):
        op1 = random.randint(2, 9)
        op2 = random.randint(2, 9)
        oper = random.choice(['+', '-', '*'])
        expr = str(op1) + ' ' + oper + ' ' + str(op2)
        print(expr)
        inp = input()
        while not re.match(r'-?[\d]+$', inp):
            print('Wrong format! Try again.')
            inp = input()
        if str(eval(expr)) == inp:
            print('Right!')
            count += 1
        else:
            print('Wrong!')
    ans = input(f'Your mark is {count}/5. Would you like to save the result? Enter yes or no.\n')
    if ans.lower() == 'yes' or ans == 'y':
        name = input('What is your name?\n')
        with open('results.txt', 'a', encoding='utf-8') as file:
            print(f'{name}: {count}/5 in level 1 (simple operations with numbers 2-9)', file=file)
            print('The results are saved in "results.txt".')


def middle():
    count = 0
    for i in range(5):
        op1 = random.randint(11, 29)
        print(op1)
        inp = input()
        while not re.match(r'[\d]+$', inp):
            print('Wrong format! Try again.')
            inp = input()
        if op1 ** 2 == int(inp):
            print('Right!')
            count += 1
        else:
            print('Wrong!')
    ans = input(f'Your mark is {count}/5. Would you like to save the result? Enter yes or no.\n')
    if ans.lower() == 'yes' or ans == 'y':
        name = input('What is your name?\n')
        with open('results.txt', 'a', encoding='utf-8') as file:
            print(f'{name}: {count}/5 in level 2 (integral squares of 11-29)', file=file)
            print('The results are saved in "results.txt".')


if __name__ == '__main__':    
    command = input('Which level do you want? Enter a number:\n'
                    '1 - simple operations with numbers 2-9\n'
                    '2 - integral squares of 11-29\n')
    while command not in '12':
        print('Incorrect format.')
        command = input('Which level do you want? Enter a number:\n'
                        '1 - simple operations with numbers 2-9\n'
                        '2 - integral squares of 11-29\n')
    if command == '1':
        easy()
    else:
        middle()
