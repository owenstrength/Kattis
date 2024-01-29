t = int(input())
vals = []
for _ in range(t):
    n = int(input())
    temp = set()
    for _ in range(n):
        temp.add(input())
    vals.append(len(temp))
for val in vals:
    print(val)
