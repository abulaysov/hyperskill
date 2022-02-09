import random
import itertools
import re

domino = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]]
for i in itertools.combinations([0, 1, 2, 3, 4, 5, 6], 2):
    domino.append(list(i))


def intelligence(snake, computer):
    d = {i:0 for i in range(7)}
    for i in snake:
        d[i[0]] += 1
        d[i[1]] += 1
    for i in computer:
        d[i[0]] += 1
        d[i[1]] += 1
    computer = sorted(computer, key=lambda x: d[x[0]] + d[x[1]], reverse=True)
    return computer


def distribution(elem=None):
    global domino
    if elem is None:
        p = random.sample(domino, 7)
        for i in p:
            domino.remove(i)
        c = random.sample(domino, 7)
        for i in c:
            domino.remove(i)
        return p, c
    else:
        domino.extend(elem)
        p = random.sample(domino, 7)
        for i in p:
            domino.remove(i)

        c = random.sample(domino, 7)
        for i in c:
            domino.remove(i)
        return p, c


while True:
    player, computer = distribution()
    max_player = list(filter(lambda x: x[0] == x[1], player))
    max_computer = list(filter(lambda x: x[0] == x[1], computer))
    if any(max_player) and any(max_computer):
        if max(max_player) > max(max_computer):
            snake = player.pop(player.index(max(max_player)))
            human= False
            break
        else:
            snake = computer.pop(computer.index(max(max_computer)))
            human = True
            break
    elif any(max_player):
        snake = player.pop(player.index(max(max_player)))
        human = False
        break
    elif any(max_computer):
        snake = computer.pop(computer.index(max(max_computer)))
        human = True
        break
    else:
        distribution(player + computer)

snake = [snake]
while True:
    print('=' * 70, f'Stock size: {len(domino)}', f'Computer pieces: {len(computer)}\n', sep='\n')

    if len(snake) > 6:
        print(f'{snake[0]}{snake[1]}{snake[2]}...{snake[-3]}{snake[-2]}{snake[-1]}\n')
    else:
        print(*snake, '\n')

    print('Your pieces:')
    for i, j in enumerate(player, 1):
        print(f'{i}: {j}')
    if len(player) == 0:
        print('Status: The game is over. You won!')
        break
    elif len(computer) == 0:
        print('Status: The game is over. The computer won!')
        break
    elif len(snake) >= 10 and snake[0][0] == snake[-1][1]:
        print("Status: The game is over. It's a draw!")
        break

    if human:
        print("\nStatus: It's your turn to make a move. Enter your command.")
        figures = input()
        while True:
            try:
                n = int(figures)
                if n == 0:
                    if len(domino) != 0:
                        dmn = domino.pop(domino.index(random.choice(domino)))
                        player.append(dmn)
                    break
                elif -len(player) <= n <= len(player) and n != 0:
                    if n < 0:
                        if snake[0][0] in player[abs(n)-1] or snake[0][0] in player[abs(n)-1]:
                            break
                    elif n > 0:
                        if snake[-1][1] in player[n-1] or snake[-1][1] in player[n-1]:
                            break
                if -len(player) <= n <= len(player):
                    figures = input('Illegal move. Please try again.\n')
                else:
                    figures = input('Invalid input. Please try again.\n')
            except Exception:
                figures = input('Invalid input. Please try again.\n')

        if figures.startswith('-'):
            dmn = player.pop(abs(n) - 1)
            if snake[0][0] == dmn[1]:
                snake.insert(0, dmn)
            else:
                snake.insert(0, dmn[::-1])
        elif n != 0:
            dmn = player.pop(abs(n) - 1)
            if snake[-1][1] == dmn[0]:
                snake.append(dmn)
            else:
                snake.append(dmn[::-1])
        human = False
    else:
        input("\nStatus: Computer is about to make a move. Press Enter to continue...\n")
        figures = intelligence(snake, computer)
        for i in figures:
            if i[0] in snake[0] or i[1] in snake[0]:
                if i[1] == snake[0][0]:
                    snake.insert(0, i)
                else:
                    snake.insert(0, i[::-1])
                computer.remove(i)
                break
            elif i[0] in snake[-1] or i[1] in snake[-1]:
                if i[0] == snake[-1][1]:
                    snake.append(i)
                else:
                    snake.append(i[::-1])
                computer.remove(i)
                break
        else:
            if len(domino) != 0:
                computer.append(domino.pop(domino.index(random.choice(domino))))
        human = True
