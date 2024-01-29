while True:
    n = int(input())
    if n == 0:
        break
    names = []
    for i in range(n):
        names.append(input())
    names.sort(key=lambda x: x[:2])
    for name in names:
        print(name)
    print()