import re
list_msg = ["Enter an equation", "Do you even know what numbers are? Stay focused!",
            "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
            "Yeah... division by zero. Smart move...",
            "Do you want to store the result? (y / n):",
            "Do you want to continue calculations? (y / n):",
            " ... lazy",
            " ... very lazy",
            " ... very, very lazy",
            "You are",
            "Are you sure? It is only one digit! (y / n)",
            "Don't be silly! It's just one number! Add to the memory? (y / n)",
            "Last chance! Do you really want to embarrass yourself? (y / n)"]

memory = 0.0


def valid(x, y):
    global memory
    if x == 'M' and y == 'M':
        return memory, memory
    elif x == 'M':
        return memory, float(y)
    elif y == 'M':
        return float(x), memory
    try:
        return float(x), float(y)
    except Exception:
        return False


def is_one_digit(x):
    if re.match(r'\d(\.0)?$', x) and 10 > int(float(x)) > -10:
        return True


def check(v1, v2, v3):
    msg = ''
    if v1 == 'M':
        v1 = memory
    if v2 == 'M':
        v2 = memory
    if is_one_digit(str(v1)) and is_one_digit(str(v2)):
        msg += list_msg[6]
    if (v1 == '1' or v2 == '1') and v3 == '*':
        msg += list_msg[7]
    if (float(v1) == 0.0 or float(v2) == 0.0) and (v3 == '*' or v3 == '-' or v3 == '+'):
        msg += list_msg[8]
    if msg != '':
        msg = list_msg[9] + msg
        print(msg)


def main():
    flag = True
    global memory
    while flag:
        expr = input(list_msg[0]).split()
        res = valid(expr[0], expr[2])
        if not res:
            print(list_msg[1])
        elif res:
            a, b = res
            oper = expr[1]
            if oper not in '+*/-':
                print(list_msg[2])
            else:
                check(expr[0], expr[2], oper)
                flg = True
                if oper == '/' and b == 0:
                    flg = False
                    print(list_msg[3])
                else:
                    if oper == '+':
                        result = a + b
                    elif oper == '-':
                        result = a - b
                    elif oper == '*':
                        result = a * b
                    else:
                        if oper == '/' and b == 0.0:
                            print(list_msg[3])
                        else:
                            result = a / b
                if flg:
                    print(result)
                    while True:
                        com1 = input(list_msg[4])
                        if com1 == 'n' or com1 == 'y':
                            break
                    if com1 == 'y':
                        if is_one_digit(str(result)):
                            msg_index = 10
                            while True:
                                com4 = input(list_msg[msg_index])
                                if com4 == 'y' and msg_index < 12:
                                    msg_index += 1
                                elif com4 == 'n':
                                    break
                                elif com4 == 'y' or msg_index > 12:
                                    memory = result
                                    break
                        else:
                            memory = result
                    while True:
                        com2 = input(list_msg[5])
                        if com2 == 'n':
                            flag = False
                            break
                        elif com2 == 'y':
                            break


if __name__ == '__main__':
    main()
