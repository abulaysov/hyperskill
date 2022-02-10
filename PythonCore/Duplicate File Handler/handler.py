import sys
import os
import hashlib


def file_check():
    d = {}
    form = input('Enter file format:\n')
    print('Size sorting option:\n1. Descending\n2. Ascending\n')
    sorting = input('Enter a sorting option:\n')
    while sorting not in '21':
        print('Wrong option\n')
        sorting = input('Enter a sorting option:\n')

    if any(form):
        for root, dirs, files in os.walk(arg[1]):
            for name in files:
                name_file = os.path.join(root, name)
                if name_file[name_file.find('.')+1:] == form:
                    abs_path = os.path.abspath(name_file)
                    if os.path.getsize(abs_path) not in d:
                        d[os.path.getsize(abs_path)] = [abs_path]
                    else:
                        d[os.path.getsize(abs_path)].append(abs_path)
    else:
        for root, dirs, files in os.walk(arg[1]):
            for name in files:
                name_file = os.path.join(root, name)
                abs_path = os.path.abspath(name_file)
                if os.path.getsize(abs_path) not in d:
                    d[os.path.getsize(abs_path)] = [name_file]
                else:
                    d[os.path.getsize(abs_path)].append(name_file)

    if sorting == '1':
        for i in sorted(d, reverse=True):
            if len(d[i]) > 1:
                print(i, 'bytes')
                for j in d[i]:
                    print(j)
    else:
        for i in sorted(d):
            if len(d[i]) > 1:
                print(i, 'bytes')
                for j in d[i]:
                    print(j)
    return d, sorting


def check_duplicate(d, sorting):
    new_d = {}
    result = {}
    x = 1
    ret_result = []
    
    for i in d:
        for j in d[i]:
            key = (i, hash_(j))
            if key not in new_d:
                new_d[key] = [j]
            else:
                new_d[key].append(j)

    for j, i in new_d:
        if len(new_d[(j, i)]) > 1:
            if j not in result:
                result[j] = [i] + new_d[(j, i)]
            else:
                result[j].extend([i] + new_d[(j, i)])

    if sorting == '1':
        for i in sorted(result, reverse=True):
            print(f'{i} bytes')
            for j in result[i]:
                if '/' not in j:
                    print(f'Hash: {j}')
                else:
                    ret_result.append(j)
                    print(f'{x}. {j}')
                    x += 1
    else:
        for i in sorted(result):
            print(f'{i} bytes')
            for j in result[i]:
                if '/' not in j:
                    print(f'Hash: {j}')
                else:
                    ret_result.append(j)
                    print(f'{x}. {j}')
                    x += 1
    return ret_result


def hash_(elem):
    f = hashlib.md5()
    with open(elem.strip(), 'rb') as file:
        f.update(file.readline())
    return f.hexdigest()


def delete_files(files):
    total_byte = 0
    while True:
        com = input('Enter file numbers to delete:\n').split()
        if any(com) and len([i for i in com if i.isdigit()]) == len(com):
            com = list(map(int, com))
            if max(com) <= len(files) and min(com) > 0:
                break
        com = input('Wrong format\n')
    print(files)
    for name_file in com:
        abs_path = os.path.abspath(files[name_file-1])
        total_byte += os.path.getsize(abs_path)
        print(abs_path)
        os.remove(abs_path)
    return total_byte


if __name__ == '__main__':
    arg = sys.argv
    if len(arg) > 1 and '.' not in arg[1]:
        d, sorting = file_check()
        check = input('Check for duplicates?\n')
        if check.lower() == 'yes':
            files = check_duplicate(d, sorting)
            delete = input('Delete files?\n')
            while delete != 'yes' and delete != 'no':
                delete = input('Wrong option\n')
            if delete == 'yes':
                total = delete_files(files)
                print(f'Total freed up space: {total} bytes')
    else:
        print('Directory is not specified')
