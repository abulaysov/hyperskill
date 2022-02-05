class Markdown:
    def __init__(self):
        self.text = ''

    def plain(self, text):
        self.text += text
        return self.text

    def bold(self, text):
        self.text += f'**{text}**'
        return self.text

    def italic(self, text):
        self.text += f'*{text}*'
        return self.text

    def inline_code(self, text):
        self.text += f'`{text}`'
        return self.text

    def link(self, label, url):
        self.text += f'[{label}]({url})'
        return self.text

    def header(self, text, level):
        self.text += f'{"#" * level} {text}\n'
        return self.text

    def new_line(self):
        self.text += '\n'
        return self.text

    def un_or_list(self, number, elem=None):
        ls = []
        for i in range(1, number+1):
            if elem == '0':
                ls.append(f'{i}. ' + input(f'Row #{i}: '))
            else:
                ls.append('* ' + input(f'Row #{i}: '))
        self.text += '\n'.join(ls) + '\n'
        return self.text


def main():
    ls_com = ['plain', 'bold', 'italic', 'link', 'header', 'new-line', 'inline-code', 'ordered-list', 'unordered-list']
    obj = Markdown()

    command = input('Choose a formatter: ')
    while command != '!done':
        if command == '!help':
            print('Available formatters ' + ' '.join(ls_com) + '\nSpecial commands: !help !done')
        elif command not in ls_com:
            print('Unknown formatting type or command')
        elif command == 'plain':
            print(obj.plain(input('Text: ')))
        elif command == 'bold':
            print(obj.bold(input('Text: ')))
        elif command == 'italic':
            print(obj.italic(input('Text: ')))
        elif command == 'inline-code':
            print(obj.inline_code(input('Text: ')))

        elif command == 'link':
            label = input('Label: ')
            url = input('URL: ')
            print(obj.link(label, url))

        elif command == 'header':
            lev = int(input('Level: '))
            while lev > 6 or lev < 1:
                print('The level should be within the range of 1 to 6')
                lev = int(input('Level: '))
            txt = input('Text: ')
            print(obj.header(txt, lev))

        elif command in ['ordered-list', 'unordered-list']:
            num = int(input('Number of rows: '))
            while num < 1:
                print('The number of rows should be greater than zero')
                num = int(input('Number of rows: '))
            if command.startswith('o'):
                print(obj.un_or_list(num, '0'))
            else:
                print(obj.un_or_list(num))
        else:
            print(obj.new_line())
        command = input('Choose a formatter: ')

    with open('output.md', 'w', encoding='utf-8') as file:
        file.write(obj.text)


if __name__ == '__main__':
    main()
