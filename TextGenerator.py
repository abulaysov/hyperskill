import random as rm
import string


with open(input(), 'r', encoding='utf-8') as file:
    words = file.read().split()  # 

    trigrams = {}  # 
    list_trigrams = [f'{words[i]} {words[i+1]} {words[i+2]}' for i in range(len(words)-2)]  # 
    for i in list_trigrams:  # 
        word = i.split()  # 
        trigrams.setdefault(f'{word[0]} {word[1]}', [])  # 
        trigrams[f'{word[0]} {word[1]}'].append(word[2])  # 

    for i in trigrams:  # 
        trigrams[i] = {j: trigrams[i].count(j) for j in trigrams[i]}  # 

    first_word = list(filter(lambda x: x.split()[0][0] in string.ascii_uppercase and x.split()[0][-1] not in '.!?', trigrams.keys()))  # 

    for i in range(10):  # 
        first = rm.choice(first_word)  # 
        l = [first]  # 
        while True:
            token = ''.join(rm.choices(list(trigrams[first].keys()), list(trigrams[first].values())))  # 
            if token[-1] in '.!?' and len(l) > 2:  # 
                l.append(token)  # 
                break
            l.append(token)  # 
            first = first.split()[1] + ' ' + token  # 
        print(' '.join(l))  # 
