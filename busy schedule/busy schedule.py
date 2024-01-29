remaining = int(input())

while remaining != 0:
    time = []
    for _ in range(remaining):
        time.append(input())

    print(sorted(time))