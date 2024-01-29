n = int(input())

for m in range(2, n):
    p = n * m
    valid = True
    i = 2
    while i * i <= p:
        if p % (i*i) == 0:
            valid = False
            break
        i += 1
    if valid:
        print(m)
        break
