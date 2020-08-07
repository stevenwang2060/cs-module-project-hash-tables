# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
cipher_text = open('applications/crack_caesar/ciphertext.txt').read()
alphabet = 'ETAOHNRISDLWUGFBMYCPKVQJXZ'

def get_frequency(text):
    text = text.upper()
    letter_freq = {}

    for letter in alphabet:
        letter_freq[letter] = 0
    for letter in text:
        if letter in alphabet:
            letter_freq[letter] += 1
    return letter_freq

freq = get_frequency(cipher_text)
frequency_list = ''.join(sorted(freq, key=lambda k: freq[k], reverse=True))
print(frequency_list)

def decrypt(text):
    plain_txt = ''
    for c in text:
        index = frequency_list.find(c)
        if alphabet[index] == 'Z':
            plain_txt += ' '
        else:
            plain_txt += alphabet[index]
    return plain_txt


print(decrypt(cipher_text))