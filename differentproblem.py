from sys import stdin

for line in stdin:
    a,b = line.split()
    a = int(a)
    b = int(b)
    if a >= b:
        print(a - b)
    else:
        print(b-a)