import os
import io
import argparse


class FlashCards:
    def __init__(self):
        self.term_definition = {}
        self.buffer = io.StringIO()
        parser = argparse.ArgumentParser()
        parser.add_argument('--import_from', default=None)
        parser.add_argument('--export_to', default=None)
        self.args = parser.parse_args()
        if self.args.import_from is not None:
            self.import_()

    def add(self):
        key = self.input_buffer(f'The card:')
        while True:
            if key in self.term_definition:
                key = self.input_buffer(f'The term "{key}" already exists. Try again:')
            else:
                break
        value = self.input_buffer(f'The definition of the card:')
        while True:
            if value in [i[0] for i in self.term_definition.values()]:
                value = self.input_buffer(f'The definition "{value}" already exists. Try again:')
            else:
                break
        value = [value, 0]
        self.term_definition[key] = value
        self.print_buffer(f'The pair ("{key}":"{value[0]}") has been added')

    def remove(self):
        rmcard = self.input_buffer('Which card?')
        if rmcard in self.term_definition:
            del self.term_definition[rmcard]
            self.print_buffer('The card has been removed.')
        else:
            self.print_buffer(f'''Can't remove "{rmcard}": there is no such card.''')

    def import_(self):
        if self.args.import_from is not None:
            import_card = {}
            impcard = self.args.import_from
            if impcard not in os.listdir():
                self.print_buffer('File not found.')
            else:
                with open(impcard, 'r') as file:
                    import_card = {i.split(':')[0]: [i.split(':')[1], int(i.split(':')[2])] for i in file.readlines()}
            self.print_buffer(f'{len(import_card)} cards have been loaded.')
            for key in import_card:
                self.term_definition[key] = import_card[key]
        elif com == 'import':
            import_card = {}
            impcard = self.input_buffer('File name:')
            if impcard not in os.listdir():
                self.print_buffer('File not found.')
            else:
                with open(impcard, 'r') as file:
                    import_card = {i.split(':')[0]: [i.split(':')[1], int(i.split(':')[2])] for i in file.readlines()}
            self.print_buffer(f'{len(import_card)} cards have been loaded.')
            for key in import_card:
                self.term_definition[key] = import_card[key]

    def export(self):
        if self.args.export_to is not None:
            expcard = self.args.export_to
            with open(expcard, 'w') as excard:
                for key, value in self.term_definition.items():
                    print(f'{key}:{value[0]}:{value[1]}', file=excard)
            self.print_buffer(f'{len(self.term_definition)} cards have been saved')
        elif com == 'export':
            expcard = self.input_buffer('File name:')
            with open(expcard, 'w') as excard:
                for key, value in self.term_definition.items():
                    print(f'{key}:{value[0]}:{value[1]}', file=excard)
            self.print_buffer(f'{len(self.term_definition)} cards have been saved')

    def ask(self):
        askcard = int(self.input_buffer('How many times to ask?'))
        count = 0
        terms = [i[0] for i in list(self.term_definition.values())]
        for j in range(askcard):
            for i in self.term_definition:
                defin = self.input_buffer(f'Print the definition of "{i}":')
                if defin in terms and defin != self.term_definition[i][0]:
                    keys = ''.join([i for i in self.term_definition if defin == self.term_definition[i][0]])
                    self.print_buffer(f'Wrong. The right answer is "{self.term_definition[i][0]}", '
                                      f'but your definition is correct for "{keys}".')
                    self.term_definition[i][1] += 1
                elif defin != self.term_definition[i][0]:
                    self.print_buffer(f'Wrong. The right answer is "{self.term_definition[i][0]}".')
                    self.term_definition[i][1] += 1
                else:
                    self.print_buffer('Correct!')
                count += 1
                if count == askcard:
                    break
            if count == askcard:
                break

    def log(self):
        saved_file = self.input_buffer('File name:')
        with open(saved_file, 'w', encoding='utf-8') as file:
            for i in self.buffer.getvalue().split('\n'):
                print(i, file=file)
            self.print_buffer('The log has been saved.')

    def hardest_card(self):
        if len(self.term_definition) != 0:
            max_word = max(tuple(i[1] for i in self.term_definition.values()))
            if max_word == 0:
                self.print_buffer('There are no cards with errors.')
            else:
                max_words = [i for i in self.term_definition if self.term_definition[i][1] == max_word]
                max_words = ', '.join(max_words)
                self.print_buffer(f'The hardest card is "{max_words}". You have {max_word} errors answering it')
        else:
            self.print_buffer('There are no cards with errors.')

    def reset_stats(self):
        for i in self.term_definition:
            self.term_definition[i][1] = 0
        self.print_buffer('Card statistics have been reset.')

    def print_buffer(self, text):
        print(text)
        print(text, file=self.buffer)

    def input_buffer(self, text=None):
        inp = input(text + '\n')
        if text is not None:
            print(text, file=self.buffer)
        print(inp, file=self.buffer)
        return inp


def main():
    obj = FlashCards()
    global com
    com = obj.input_buffer('Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):')

    while com != 'exit':
        if com == 'add':
            obj.add()
        elif com == 'remove':
            obj.remove()
        elif com == 'import':
            obj.import_()
        elif com == 'export':
            obj.export()
        elif com == 'ask':
            obj.ask()
        elif com == 'log':
            obj.log()
        elif com == 'hardest card':
            obj.hardest_card()
        elif com == 'reset stats':
            obj.reset_stats()
        com = obj.input_buffer(
            'Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):')
    else:
        if obj.args.export_to is not None:
            obj.export()
        obj.buffer.close()
        print('Bye bye')


if __name__ == '__main__':
    main()

