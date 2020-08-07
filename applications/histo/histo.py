# Your code here
import re
dic = {}
text = open('applications/histo/robin.txt').read()

def count_w(str):
    global dic
    filtered = re.sub(r"[^\w\d'\s]", '', str)
    for w in filtered.lower().split():
        if w not in dic.keys():
            dic[w] = '#'
        else:
            dic[w] += '#'
    return dic

result = count_w(text)

for word in sorted(result, key=lambda word: len(result[word]), reverse=True):
    print(word, result[word])