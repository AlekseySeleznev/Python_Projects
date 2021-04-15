'''
Find palindromes in a dictionary file
'''

import load_dictionary

# FOR ENGLISH LANGUAGE
# file = load_dictionary.load('words.txt')
# FOR RUSSIAN LANGUAGE
file = load_dictionary.load('russian_words.txt')
palindromes = []

for a in file:
    if len(a) > 3:
        if a == a[::-1]:
            palindromes.append(a)

print("\nNumber of palindromes found : {}\n".format(len(palindromes)))
print(*palindromes, sep='\n')