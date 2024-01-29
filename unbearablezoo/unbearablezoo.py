n = int(input())
i = 1
while n != 0:
    hash = {}
    for _ in range(n):
        s = input().split()[-1]
        s = s.lower()
        if s not in hash:
            hash[s] = 1
        else:
            hash[s] += 1
    hash = list(hash.items())
    hash.sort(key=lambda x: x[0])
    print("List " + str(i) + ":")
    for item, times in hash:
        print(str(item) + " | " + str(times))

    i += 1
    n = int(input())
