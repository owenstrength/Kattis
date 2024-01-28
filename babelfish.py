from sys import stdin

dictionary = dict()

for line in stdin:
    line = line.strip()
    if line == "":
        break
    english, foreign = line.split()
    dictionary[foreign] = english

for line in stdin:
    line = line.strip()
    if line in dictionary:
        print(dictionary[line])
    else:
        print("eh")