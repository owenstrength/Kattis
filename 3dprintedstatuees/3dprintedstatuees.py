n = int(input())
days = 0
printers = 1

while (n > 0):
    if (n/printers > 3):
        days += 1
        printers *= 2
    else:
        n -= printers
        days += 1
print(days)

