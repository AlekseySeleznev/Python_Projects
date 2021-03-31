'''A simple script that generates a new word to its Pig Latin equivalent'''

vowels = 'aeiouy'
word = str(input("Enter a word.\n").lower())
resume = 'y'

while True:
    if word[0] in vowels:
        word = word + 'way'
    else:
        word = word[1:] + word[0] + 'ay'
    print(word)
    resume = str(input("Do you want to try again? Type 'n' if no.\n"))
    if resume.lower() == 'n':
        break
    input('Enter any key to exit')