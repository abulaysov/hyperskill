def stage_1():
    global department
    for key, value in students.items():
        for j in value:
            if j[0] == 1:
                department[key].append(j[1:])
    for i in department:
        department[i] = sorted(department[i], key=lambda x: x[0])
        department[i] = sorted(department[i], key=lambda x: x[1], reverse=True)
    for i in department:
        department[i] = department[i][:number]


def stage_23():
    global department
    for stage in range(2, 4):
        for key, value in students.items():
            new_list = []
            std = []
            for i in department.values():
                for k in i:
                    std.append(k[0])
            for j in value:
                if j[0] == stage:
                    if j[1] not in std:
                        std.append(j[1])
                        new_list.append(j[1:])
            if len(department[key]) != number:
                new_list = sorted(new_list, key=lambda x: x[0])
                new_list = sorted(new_list, key=lambda x: x[1], reverse=True)
                department[key].extend(new_list)
                department[key] = department[key][:number]
                department[key] = sorted(department[key], key=lambda x: x[0])
                department[key] = sorted(department[key], key=lambda x: x[1], reverse=True)


if __name__ == '__main__':
    number = int(input())
    f = open('applicant_list.txt')
    list_stidents = list(map(str.strip, f.readlines()))
    f.close()
    students = {'Biotech': [], 'Chemistry': [], 'Engineering': [], 'Mathematics': [], 'Physics': []}

    for i in list_stidents:
        student = i.split()
        for j, k in enumerate(student[7:], 1):
            name = ' '.join(student[:2])
            y = float(student[6])
            if k == 'Physics':
                x = round((float(student[2]) + float(student[4])) / 2, 1)
                students[k].append([j] + [name] + [str(max(x, y))])
            elif k == 'Chemistry':
                x = float(student[3])
                students[k].append([j] + [name] + [str(max(x, y))])
            elif k == 'Mathematics':
                x = float(student[4])
                students[k].append([j] + [name] + [str(max(x, y))])
            elif k == 'Engineering':
                x = round((float(student[4]) + float(student[5])) / 2, 1)
                students[k].append([j] + [name] + [str(max(x, y))])
            elif k == 'Biotech':
                x = round((float(student[3]) + float(student[2])) / 2, 1)
                students[k].append([j] + [name] + [str(max(x, y))])

    department = {'Biotech': [], 'Chemistry': [], 'Engineering': [], 'Mathematics': [], 'Physics': []}

    stage_1()
    stage_23()

    for i, j in department.items():
        with open(i.lower() + '.txt', 'w') as f:
            for k in j:
                print(' '.join(k), file=f)
