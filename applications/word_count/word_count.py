import re
calculate = {}

def word_count(s):
    # Your code here
    global calculate
    filtered_str = re.sub(r"[^\w\d'\s]", '', s)
    for word in filtered_str.lower().split():
        if word not in calculate.keys():
            calculate[word] = 1
        else:
            calculate[word] += 1
    s = calculate
    calculate = {}
    return s


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))