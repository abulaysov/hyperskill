import random


name = input('Enter your name: ')
print(f'Hello, {name}')

rating = 0

with open('rating.txt', 'r') as file:
    l = [i for i in file.readlines() if i.strip().split()[0] == name]
    if any(l):
        rating += int(l[0].strip().split()[1])


def options(li: list):
    if any(li):
        d = {}
        list_ = li.copy()
        lenthg = len(list_)
        for i in li:
            x = (li.index(i) + lenthg // 2)
            if x >= len(l):
                li += li[:li.index(i)]
                d[i] = li[li.index(i)+1:x+1]
            else:
                d[i] = li[li.index(i)+1:x+1]
        return d
    return {'scissors': ['rock'], 'rock': ['paper'], 'paper': ['scissors']}


l = input().split(',')
d = options(l)

print("Okay, let's start")
inp = input()
opt = [i for i in d]

while inp != '!exit':
    if inp == '!rating':
        print(f'Your rating: {rating}')
    elif inp not in d:
        print('Invalid input')
    else:
        r = random.choice(opt)
        if r in d[inp]:
            print(f'Sorry, but the computer chose {r}')
        elif inp == r:
            print(f'There is a draw ({r})')
            rating += 50
        else:
            print(f'Well done. The computer chose {r} and failed')
            rating += 100
    inp = input()
else:
    print('Bye!')
