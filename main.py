import json
import re
f = open("bad-words.txt", "r")
names = f.read()
names = names.split("\n")
print(len(names))

consonants = ['c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
vowels = ['a','e','i','o','u']

letterDictionary = {}
letter_frequenc_list = []

# for name in names:
#     for letter in name:
#         if letter in consonants:
#             if letter.lower() not in letterDictionary:
#                 letterDictionary[letter.lower()] = 1
#             else:
#                 letterDictionary[letter.lower()] += 1


# names = ["Andy", "Deanna", "adam", "andy"]
# for name in names:
#     grouping = re.split(r'[bcdfghjklmnpqrstvwxyz]', name.lower())
#     for letter in grouping:
#         if letter.lower() == "":
#             continue
#         elif letter.lower() not in letterDictionary:
#             letterDictionary[letter.lower()] = 1
#         else:
#             letterDictionary[letter.lower()] += 1

# names = ["aaron", "Andy", "Deanna", "Ben", "amy"]

# for name in names:
#     grouping = re.split(r'[aeiou]', name.lower())
#     if grouping[0].lower() == "":
#         continue
#     elif grouping[0].lower() not in letterDictionary:
#         letterDictionary[grouping[0].lower()] = 1
#     else:
#         letterDictionary[grouping[0].lower()] += 1


def shrinkDictionary(d):
    new_dict = {}
    smallest = min(d, key=d.get)
    print(smallest)
    counter = 0
    for value in d:
        # print(d[value])
        new_dict[value] = d[value] // d[smallest]
        for i in range(new_dict[value]):
            letter_frequenc_list.append(value)
        counter += d[value]
    return new_dict, counter


# letterDictionary, count = shrinkDictionary(letterDictionary)
# print("letters", count)
# with open('letterFrequencyConsonants.json', 'w') as fp:
#     json.dump(letterDictionary, fp)
# print(letterDictionary)

with open('badWords.txt', 'w') as f:
    f.write("let badWords = [")
    for item in names:
        f.write("\'%s\'," % item)
    f.write("]")