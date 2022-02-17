import random as rm
import string


with open(input(), 'r', encoding='utf-8') as file:  # open the file for processing
    words = file.read().split()  # creating a corpus

    trigrams = {}  # Dictionary for Markov chain
    list_trigrams = [f'{words[i]} {words[i+1]} {words[i+2]}' for i in range(len(words)-2)]  # list of trigrams
    for i in list_trigrams:  # iterate the list of trigrams
        word = i.split()  # split a list item into a list of 3 items
        trigrams.setdefault(f'{word[0]} {word[1]}', [])  # query the item by the key, if not, we create an empty list
        trigrams[f'{word[0]} {word[1]}'].append(word[2])  # add a trigram to the dictionary trigrams

    for i in trigrams:  # iterate the Markov chain
        trigrams[i] = {j: trigrams[i].count(j) for j in trigrams[i]}  # adding a word repetition counter


    # filter the key dictionary of trigrams that match the condition
    first_word = list(filter(lambda x: x.split()[0][0] in string.ascii_uppercase and x.split()[0][-1] not in '.!?', trigrams.keys())) 

    for i in range(10):
        first = rm.choice(first_word)  # initial word (head) of the chain
        l = [first]  # list with the initial word (head) of the chain
        while True:
            # choose the next word for the chain, using the choices function from the random module
            token = ''.join(rm.choices(list(trigrams[first].keys()), list(trigrams[first].values())))
            if token[-1] in '.!?' and len(l) > 2:  # if the offer consists of more than 3 tokens and the token ends in ".!?"
                l.append(token)  # add a token and finish the sentence
                break
            l.append(token)  # add token in list of offer
            first = first.split()[1] + ' ' + token  # a new key from the last token of the previous head and its body
        print(' '.join(l))  # typing a sentence
