import os


class FlashCards:
    def __init__(self):
        self.term_definition = {}

    def add(self):
        key = input(f'The card:\n')
        while True:
            if key in self.term_definition:
                print(f'The term "{key}" already exists. Try again:')
                key = input()
            else:
                break
        value = input(f'The definition of the card:\n')
        while True:
            if value in self.term_definition.values():
                print(f'The definition "{value}" already exists. Try again:')
                value = input()
            else:
                break
        self.term_definition[key] = value
        print(f'The pair ("{key}":"{value}") has been added')

    def remove(self):
        rmcard = input('Which card?\n')
        if rmcard in self.term_definition:
            del self.term_definition[rmcard]
            print('The card has been removed.')
        else:
            print(f'''Can't remove "{rmcard}": there is no such card.''')

    def importt(self):
        import_card = {}
        impcard = input('File name:\n')
        if impcard not in os.listdir():
            print('File not found.')
        else:
            with open(impcard, 'r') as file:
                import_card = {i.split()[0].strip(): i.split()[1].strip() for i in file.readlines()}
        print(f'{len(import_card)} cards have been loaded.')
        for key in import_card:
            self.term_definition[key] = import_card[key]

    def export(self):
        expcard = input('File name:\n')
        with open(expcard, 'w') as excard:
            for key, value in self.term_definition.items():
                print(key, value, file=excard)
        print(f'{len(self.term_definition)} cards have been saved')

    def ask(self):
        askcard = int(input('How many times to ask?\n'))
        count = 0
        for j in range(askcard):
            for i in self.term_definition:
                print(f'Print the definition of "{i}":')
                defin = input()
                if defin in self.term_definition.values() and defin != self.term_definition[i]:
                    keys = ''.join([i for i in self.term_definition if defin == self.term_definition[i]])
                    print(f'Wrong. The right answer is "{self.term_definition[i]}", but your definition is correct for "{keys}".')
                elif defin == self.term_definition[i]:
                    print('Correct!')
                else:
                    print(f'Wrong. The right answer is "{self.term_definition[i]}".')
                count += 1
                if count == askcard:
                    break
            if count == askcard:
                break


obj = FlashCards()
command = input('Input the action (add, remove, import, export, ask, exit):\n')

while command != 'exit':
    if command == 'add':
        obj.add()
    elif command == 'remove':
        obj.remove()
    elif command == 'import':
        obj.importt()
    elif command == 'export':
        obj.export()
    elif command == 'ask':
        obj.ask()
    command = input('Input the action (add, remove, import, export, ask, exit):\n')
else:
    print('Bye bye')




