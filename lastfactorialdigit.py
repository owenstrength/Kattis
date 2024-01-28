n = int(input())


for _ in range(n):
    a = int(input())
    if a != 3 and a < 5:
        print(a)
    elif a == 3:
        print(6)
    else:
        print(0)
