
text = "Like the castle in its corner. In a medieval game. I foresee terrible trouble. And I stay here just the same."

dict = {"a": [], "b": [], "c": [], "d": [], "e": [], "f": [], "g": [], "h": [], "i": [], "j": [], "k": [], "l": [], "m": [], "n": [], "o": [], "p": [],
             "q": [], "r": [], "s": [], "t": [], "u": [], "v": [], "w": [], "x": [], "y": [], "z": []}

i = 0
b = 0
text = text.lower()
for l in text:
    if l in dict:
        dict[l].append(l)

for k in dict:
    if len(dict[k]) > 0:
        print("{} : {}".format(k.upper(), len(dict[k])))
        i += len(dict[k])

