def dot(reg, inp, ind):
    if (reg == '' and len(inp)) or (reg == '' and inp == ''):
        return True
    elif any(reg) and any(inp):
        if ind == len(reg):
            return True
        if '$' not in reg and '^' not in reg and len(reg) < len(inp):
            return reg.replace('.', '') in inp
        if reg[ind] == inp[ind] or reg[ind] == '.' and inp[ind] != '':
            if len(reg) - 1 == ind:
                return True
            return dot(reg, inp, ind + 1)
    return False


def beginning(reg, inp, ind=0):
    for i, j in zip(reg[1:], inp):
        if not dot(i, j, 0):
            return False
    return True


def end(reg, inp, ind=0):
    for i, j in zip(reg[::-1][1:], inp[::-1]):
        if not dot(i, j, 0):
            return False
    return True


def escape(reg, inp):
    reg = reg.replace('\\.', 'ⴰ')
    reg = reg.replace('\\+', '₊')
    reg = reg.replace('\\?', '‽')
    reg = reg.replace('\\*', '⁎')
    reg = reg.replace('\\\\', '\\')

    inp = inp.replace('+', '₊')
    inp = inp.replace('?', '‽')
    inp = inp.replace('*', '⁎')
    inp = inp.replace('.', 'ⴰ')

    return question_meta(reg, inp)


def question_meta(reg, inp):
    while '?' in reg:
        if reg[reg.find('?') - 1] != inp[reg.find('?') - 1] and reg[reg.find('?') - 1] != '.':
            reg = reg.replace(reg[reg.find('?') - 1], '', 1)
            reg = reg.replace('?', '', 1)
        else:
            reg = reg.replace('?', '', 1)
    return asterisk_meta(reg, inp)


def asterisk_meta(reg, inp):
    flag = False
    if reg.startswith('^'):
        flag = True
        reg = reg[1:]
    while '*' in reg:
        if reg.find('*') > len(inp):
            reg = reg[:-2]
            break
        if reg[reg.find('*') - 1] != inp[reg.index('*') - 1] and reg[reg.find('*') - 1] != '.':
            reg = reg.replace(reg[reg.find('*') - 1], '', 1)
            reg = reg.replace('*', '', 1)
        else:
            total = 0
            for i in inp[reg.find('*') - 1:]:
                if i == inp[reg.find('*') - 1]:
                    total += 1
                elif reg[reg.find('*') - 1] == '.':
                    total += 1
                else:
                    break
            if total == 1:
                reg = reg.replace('*', '', 1)
            else:
                if reg[reg.find('*') - 1] != '.':
                    reg = reg[:reg.find('*') - 1] + reg[reg.find('*') - 1] * total + reg[reg.find('*') + 1:]
                else:
                    if reg.endswith('$'):
                        s = reg[-2]
                        reg = reg[:reg.find('*') - 1] + inp[reg.find('*') - 1:]
                        if s != reg[-1]:
                            reg += s
                        reg += '$'
                    else:
                        reg = reg[:reg.find('*') - 1] + inp[reg.find('*') - 1:]

    if flag:
        reg = '^' + reg
    return plus_meta(reg, inp)


def plus_meta(reg, inp):
    flag = False
    if reg.startswith('^'):
        flag = True
        reg = reg[1:]
    while '+' in reg:
        if reg.find('+') > len(inp):
            reg = reg[:-2]
            break
        if reg[reg.find('+') - 1] != inp[reg.index('+') - 1] and reg[reg.find('+') - 1] != '.':
            reg = reg.replace('+', '', 1)
        else:
            total = 0
            for i in inp[reg.find('+') - 1:]:
                if i == inp[reg.find('+') - 1]:
                    total += 1
                elif reg[reg.find('+') - 1] == '.':
                    total += 1
                else:
                    break
            if total == 1:
                reg = reg.replace('+', '', 1)
            else:
                if reg[reg.find('+') - 1] != '.':
                    reg = reg[:reg.find('+') - 1] + reg[reg.find('+') - 1] * total + reg[reg.find('+') + 1:]
                else:
                    if reg.endswith('$'):
                        s = reg[-2]
                        reg = reg[:reg.find('+') - 1] + inp[reg.find('+') - 1:]
                        if s != reg[-1]:
                            reg += s
                        reg += '$'
                    else:
                        reg = reg[:reg.find('+') - 1] + inp[reg.find('+') - 1:]
    if flag:
        reg = '^' + reg
    return reg, inp


def main(reg, inp):
    if reg.startswith('^') and reg.endswith('$'):
        if beginning(reg, inp) and end(reg, inp):
            return True
        return False
    if reg.startswith('^'):
        if beginning(reg, inp):
            return True
        return False
    if reg.endswith('$'):
        if end(reg, inp):
            return True
        return False
    if len(reg) > len(inp) and ('$' not in reg or '^' not in reg):
        return False
    return dot(reg, inp, 0)


if __name__ == '__main__':
    reg, inp = input().split('|')
    print(main(*escape(reg, inp)))
