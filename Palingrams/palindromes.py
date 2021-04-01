'''
Find palindromes in a dictionary file
'''

import load_dictionary

file = load_dictionary.load('words.txt')
palindromes = []

for a in file:
    if a == a[::-1]:
        palindromes.append(a)

print("\nNumber of palindromes found : {}\n".format(len(palindromes)))
print(*palindromes, sep='\n')