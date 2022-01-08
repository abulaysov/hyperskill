import argparse
import os
import re
import ast


def s001(line, cod):
    if len(line[1]) > 79:
        print(f'{cod}: Line {line[0]}: S001 too long')


def s002(line, cod):
    total_sum = len(line[1]) - len(line[1].lstrip())
    if total_sum % 4 != 0:
        print(f'{cod}: Line {line[0]}: S002 Indentation is not a multiple of four')


def s003(line, cod):
    if line[1] != '':
        if ';' in line[1] and '#' in line[1]:
            if ';' in line[1][:line[1].find('#')]:
                print(f'{cod}: Line {line[0]}: S003 Unnecessary semicolon after a statement.')
        elif ';' in line[1] and line[1][-1] == ';':
            print(f'{cod}: Line {line[0]}: S003 Unnecessary semicolon after a statement.')


def s004(line, cod):
    ind = line[1].find('#')
    if ind != -1 and ind != 0:
        new_line = line[1][:ind]
        if new_line[-2:].count(' ') < 2:
            print(f'{cod}: Line {line[0]}: S004 Less than two spaces before inline comments')


def s005(line, cod):
    ind = line[1].find('#')
    if ind != -1 and 'todo' in line[1][ind:].lower():
        print(f'{cod}: Line {line[0]}: S005 TODO found (in comments only and case-insensitive)')


def s006(line, cod):
    global counter
    counter += 1
    if counter > 2:
        counter = 0
        print(f'{cod}: Line {line[0] + 1}: S006 More than two blank lines between lines.')


def s007(line, cod):
    if line[1].startswith('class'):
        if not re.match(r'class [\S]+:$', line[1]):
            print(f'{cod}: Line {line[0]}: S007 Too many spaces after class')
    elif line[1].startswith('def'):
        if not re.match(r'def [\S]+', line[1]):
            print(f'{cod}: Line {line[0]}: S007 Too many spaces after def')


def s008(line, cod):
    if line[1].startswith('class'):
        templ = r'class[\s]{1,10}[A-Z]{1}[a-z]+[A-Z]?[a-z]+:$'
        templ_1 = r'class[\s]{1,10}[A-Z]{1}[a-z]+[A-Z]?[a-z]+\([A-Z]{1}[a-z]+[A-Z]?[a-z]+\):$'
        name = line[1].replace('class', '')[:line[1].find('(')].strip()
        if not re.match(templ, line[1]) and not re.match(templ_1, line[1]):
            print(f"{cod}: Line {line[0]}: S008 Class name '{name}' should use CamelCase")


def s009(line, cod):
    if line[1].lstrip().startswith('def'):
        templ_def = re.match(r'def[\s]{1,10}[a-z0-9_]+_?[a-z0-9_]+$', line[1][line[1].find('d'):line[1].find('(')])
        name = line[1][line[1].find('f') + 1:line[1].find('(')].strip()
        if not templ_def:
            print(f"{cod}: Line {line[0]}: S009 Function name '{name}' should use snake_case")


def s010(line, cod, file):
    if line[1].lstrip().startswith('def'):
        name_funct = line[1][line[1].find('f') + 1:line[1].find('(')].strip()
        tree = ast.parse(file)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == name_funct:
                for argument in node.args.args:
                    if not re.match(r'[a-z0-9_]+$', argument.arg):
                        print(f"{cod}: Line {line[0]}: S010 Argument name '{argument.arg}' should be snake_case")
        s011(line, cod, file, name_funct)


def s011(line, cod, file, name_funct):
    tree = ast.parse(file)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == name_funct:
            for variable in node.body:
                if isinstance(variable, ast.Assign):
                    ver = ast.dump(variable.targets[0]).split("'")[1]
                    if not re.match(r'[a-z0-9_]+', ver):
                        print(f"{cod}: Line {variable.lineno}: S011 Variable '{ver}' in function should be snake_case")
    s012(line, cod, file, name_funct)


def s012(line, cod, file, name_funct):
    tree = ast.parse(file)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == name_funct:
            for argument in node.args.defaults:
                if not any([isinstance(argument, elem) for elem in [ast.Constant, ast.Tuple, ast.Call]]):
                    print(f"{cod}: Line {line[0]}: S012 Default argument value is mutable")
                    break


def open_file(file_code: list):
    if args.path[-3:] != '.py':
        file_code = list(map(lambda x: f'{args.path}/' + x, file_code))
    for code_path in file_code:
        with open(code_path) as file:
            string_code_file = file.read()
            file.seek(0)
            for line_code in enumerate(map(str.rstrip, file.readlines()), 1):
                if line_code[1] == '':
                    s006(line_code, code_path)
                    continue
                else:
                    global counter
                    counter = 0
                s001(line_code, code_path)
                s002(line_code, code_path)
                s003(line_code, code_path)
                s004(line_code, code_path)
                s005(line_code, code_path)
                s007(line_code, code_path)
                s008(line_code, code_path)
                s009(line_code, code_path)
                s010(line_code, code_path, string_code_file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    args = parser.parse_args()
    if args.path[-3:] != '.py':
        path = sorted([i for i in os.listdir(args.path) if i[-3:] == '.py'])
        counter = 0
        open_file(path)
    else:
        open_file([args.path])