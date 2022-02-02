import random


d = {}
n = int(input('Enter the number of friends joining (including you):\n'))
if n > 0:
    print('Enter the name of every friend (including you), each on a new line:')
    for i in range(n):
        d[input()] = 0
    else:
        m = int(input('Enter the total bill value:\n'))
        val = round(m / len(d), 2)
        for i in d:
            d[i] = val
        inp = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
        if inp.lower() == 'yes':
            name = random.choice(list(d.keys()))
            print(name, 'is the lucky one!')
            val = round(m / (len(d) - 1), 2)
            for i in d:
                d[i] = val
            d[name] = 0
        else:
            print('No one is going to be lucky')
        print(d)
else:
    print('No one is joining for the party')
