import random
import re

my_dic = {'start': [], 'end': []}

# Read in all the words in one go
with open("applications/markov/input.txt") as f:
    words = f.read()
    words = words.split()

# TODO: analyze which words can follow other words
# Your code here
    for i in range(len(words) - 1):
        w = words[i]
        next_w = words[i+1]
        if re.match(r'^"?[A-Z]\S*', w):
            my_dic.get('start').append(w)
        if re.match(r'\S*[.!?]"?$', w):
            my_dic.get('end').append(w)
        w_list = my_dic.get(w)
        if w_list is None:
            my_dic[w] = [next_w]
        else:
            w_list.append(next_w)

def sentence():
    w = random.choice(my_dic.get('start'))
    print(w, end=' ')
    while w not in my_dic.get('end'):
        w = random.choice(my_dic.get(w))
        print(w, end=' ')

# TODO: construct 5 random sentences
# Your code here
for i in range(5):
    print()
    sentence()
    print()