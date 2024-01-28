inp = input()
h = ""
instruction = ""
for c in inp:
    if c.isnumeric():
        h += c
    elif c == 'L' or c == 'R':
        instruction += c

h = int(h)

i = 1
for c in instruction:
    i <<= 1
    if c != 'L':
        i += 1
print(2**(h+1) - i)
