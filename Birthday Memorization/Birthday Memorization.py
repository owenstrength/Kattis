from collections import Counter
from itertools import groupby

num_inputs = int(input())
lines = []
for _ in range(num_inputs):
    line = input()
    list(line.split(' '))
    lines.append(tuple((line).split()))

lines.sort(key = lambda x: x[2])
an_iterator = groupby(lines, lambda x : x[2])

temp = []
for key, group in an_iterator:
    key_and_group = list(group)
    temp.append(key_and_group)

res = []
for group in temp:
    maxRank = -1
    name = ""
    for items in group:
        if int(items[1]) > maxRank:
            maxRank = int(items[1])
            name = items[0]
    res.append(name)

print(len(res))
res.sort()
for item in res:
    print(item)