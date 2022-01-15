import re
import string
from collections import deque


class SmartCalculator:
    def __init__(self):
        self.dict_variables = {}
        self.command = {'/help': 'The program calculates the sum of numbers'}

    def commands(self, com):
        return self.command.get(com, 'Unknown command')

    def correctexpr(self, iterate):
        iterate = iterate.replace(' ', '', iterate.count(' '))
        x, oper = '', ''
        for i in iterate:
            if i.isdigit() or i in string.ascii_letters:
                if oper != '':
                    if '+' in oper:
                        x += ' + '
                    elif '-' in oper:
                        if len(oper) % 2 == 0:
                            x += ' + '
                        else:
                            x += ' - '
                    else:
                        x += f' {oper} '
                    oper = ''
                if i.isalpha():
                    x += str(self.dict_variables[i])
                else:
                    x += i
            else:
                if i in '-*+/':
                    oper += i
                elif i in '()':
                    if oper != '':
                        if '+' in oper:
                            x += ' + '
                        elif '-' in oper:
                            if len(oper) % 2 == 0:
                                x += ' + '
                            else:
                                x += ' - '
                        else:
                            x += f' {oper} '
                        oper = ''
                    if i == '(':
                        x += ' ( '
                    else:
                        x += ' ) '
        return list(map(lambda a: int(a) if a.isdigit() else a, x.split()))

    def infix_to_profix(self, iterate):
        result, stack = [],deque()
        for i in iterate:
            if isinstance(i, int):
                result.append(i)
            elif len(stack) == 0 or stack[0] == '(':
                stack.appendleft(i)
            elif i in '*/' and stack[0] in '+-':
                stack.appendleft(i)
            elif (i in '+-' and stack[0] in '*/') or (i in '+-' and stack[0] in '+-') or (
                    i in '*/' and stack[0] in '+-'):
                if i in '*/':
                    while True:
                        if stack[0] in '+-' or stack[0] in '(':
                            break
                        result.append(stack.popleft())
                    stack.appendleft(i)
                else:
                    while True:
                        if len(stack) == 0 or stack[0] in '(':
                            stack.appendleft(i)
                            break
                        result.append(stack.popleft())
            elif i in '*/' and stack[0] in '*/':
                if i in '*/':
                    while True:
                        if len(stack) == 0 or stack[0] in '+-' or stack[0] in '(':
                            break
                        result.append(stack.popleft())
                    stack.appendleft(i)
            elif i == '(':
                stack.appendleft(i)
            elif i == ')':
                while stack[0] != '(':
                    result.append(stack.popleft())
                else:
                    stack.popleft()
        for i in stack:
            result.append(i)
        return result

    def error_check(self, iterate):
        x = ''
        if ('(' in iterate and ')' not in iterate) or (')' in iterate and '(' not in iterate):
            return 'Invalid expression'
        else:
            for i in iterate:
                if i in '*/':
                    x += i
                    if len(x) > 1:
                        return 'Invalid expression'
                else:
                    x = ''

    def profix_to_result(self, iterate):
        stack = deque()
        for i in iterate:
            if isinstance(i, int):
                stack.appendleft(i)
            elif i in '+-*/':
                if i == '+':
                    stack.appendleft(stack.popleft() + stack.popleft())
                elif i == '-':
                    b, a = stack.popleft(), stack.popleft()
                    stack.appendleft(a - b)
                elif i == '/':
                    b, a = stack.popleft(), stack.popleft()
                    stack.appendleft(a / b)
                elif i == '*':
                    stack.appendleft(stack.popleft() * stack.popleft())
        return stack

    def variables(self, var):
        var = var.strip()
        elem = var.split('=')
        try:
            if re.match(r'[a-zA-Z]+\s*=\s*[\d]+', var) and len(elem) == 2:
                self.dict_variables[elem[0].strip()] = int(elem[1])

            elif re.match(r'[a-zA-Z]+\s*=\s*[a-zA-Z]+', var):
                if elem[1].strip() in self.dict_variables:
                    self.dict_variables[elem[0].strip()] = self.dict_variables[elem[1].strip()]
                else:
                    print('Unknown variable')
            else:
                if True in [i.isdigit() for i in elem[0]]:
                    print('Invalid identifier')
                else:
                    print('Invalid assignment')
        except ValueError:
            print('Invalid assignment')


operands = input()
obj = SmartCalculator()
while operands != '/exit':
    if operands.startswith('/'):
        print(obj.commands(operands))
    elif len(operands.split('=')) > 1:
        obj.variables(operands)
    elif re.match(r'[a-zA-Z\d]+\s*[-+*/]{1}\s*.+', operands):
        res_obj = obj.error_check(operands)
        if res_obj is None:
            transf_expr = obj.infix_to_profix(obj.correctexpr(operands))
            result_expt = obj.profix_to_result(transf_expr).popleft()
            print(int(result_expt))
        else:
            print(res_obj)
    elif operands.isalpha():
        if operands in obj.dict_variables:
            print(obj.dict_variables[operands])
        else:
            print('Unknown variable')
    else:
        if operands.isdigit():
            print(operands)
        elif operands != '':
            print('Invalid identifier')
    operands = input().strip()
else:
    print('Bye!')
