'''BUS 2/6'''
# Write your awesome code here
import json
import re

s = json.loads(input())

template = re.compile(r'[A-Z][a-zA-Z\s]+ (Road|Avenue|Boulevard|Street)$')

template1 = re.compile(r'[SOF]$')

template2 = re.compile(r'([0][\d]|[1][\d]|[2][123]):[012345][\d]$')


def stop_name(x):
    global counter_errors
    if not re.match(template, x):
        counter_errors['stop_name'] += 1


def stop_type(x):
    global counter_errors
    if x != '':
        if not re.match(template1, x):
            counter_errors['stop_type'] += 1


def a_time(x):
    global counter_errors
    if not re.match(template2, x):
        counter_errors['a_time'] += 1


string_errors = 'stop_name stop_type a_time'.split()
counter_errors = {i: 0 for i in string_errors}

d_funct = {'stop_name': stop_name,
           'stop_type': stop_type,
           'a_time': a_time}


for i in s:
    for j in i:
        if j in ['stop_name', 'stop_type', 'a_time']:
            d_funct[j](i[j])

print(f'Format validation: {sum([i for i in counter_errors.values()])} errors')
for i in counter_errors:
    print(f'{i}: {counter_errors[i]}')


'''BUS 4/6'''
#############################################################################################################
# Write your awesome code here
import json
import re

s = json.loads(input())


def bus_id(x):
    global d
    if x['stop_type'] == 'S':
        sof['s'].append(x['stop_name'])
    if x['stop_type'] == 'O' or x['stop_type'] == '' or x['stop_type'] == 'F':
        sof['o'].append(x['stop_name'])
    if x['stop_type'] == 'F':
        sof['f'].append(x['stop_name'])
    if x['bus_id'] not in d:
        d[x['bus_id']] = []
        d[x['bus_id']].append(x['stop_type'])
    else:
        d[x['bus_id']].append(x['stop_type'])


string_errors = 'bus_id'.split()

d_funct = {'bus_id': bus_id}
d = {}
dict_name = {}

sof = {'s': [], 'o': [], 'f': []}
for i in s:
    d_funct['bus_id'](i)


lo = sorted({i for i in sof['o'] if sof['o'].count(i) > 1})
lf = sorted({i for i in sof['f']})
ls = sorted({i for i in sof['s']})

for i in d:
    if d[i][0] != 'S' or d[i][-1] != 'F' or d[i].count('S') > 1 or d[i].count('F') > 1:
        print(f'There is no start or end stop for the line: {i}.')
        break
else:
    print(f'Start stops: {len(ls)} {ls}')
    print(f'Transfer stops: {len(lo)} {lo}')
    print(f'Finish stops: {len(lf)} {lf}')



'''BUS 6/6'''
#############################################################################################################
# Write your awesome code here


import json

s = json.loads(input())


def marsh(x):
    global d
    global a
    if x['stop_name'] not in a and x['stop_type'] not in 'SF':
        a.append(x['stop_name'])
    elif x['stop_name'] in a:
        d.append(x['stop_name'])


a, d = [], []
for i in s:
    marsh(i)

print('On demand stops test:')
if d:
    print('Wrong stop type:', sorted(d))
else:
    print('OK')