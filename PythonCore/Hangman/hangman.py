import random

print('H A N G M A N')
words = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(words)
d = {word[i] + str(i): '-' for i in range(len(word))}
st = ''

command = input('Type "play" to play the game, "exit" to quit: ')
while command == 'play':
    count = 8
    while count != 0:
        print()
        print(''.join(list(d.values())))
        inp = input("Input a letter: ")
        if ''.join(list(d.values())) == word:
            print('You guessed the word!\nYou survived!')
            break
        elif inp in word and inp not in d.values():
            st += inp
            for key in d:
                if key[0] == inp:
                    d[key] = inp
        elif inp in st:
            print("You've already guessed this letter")
        elif len(inp) != 1:
            print('You should input a single letter')
        elif 122 < ord(inp) or ord(inp) < 97:
            print('Please enter a lowercase English letter')
        else:
            print("That letter doesn't appear in the word")
            st += inp
            count -= 1
    else:
        print('You lost!')
    command = input('Type "play" to play the game, "exit" to quit: ')
