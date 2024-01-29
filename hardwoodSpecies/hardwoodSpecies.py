from sys import stdin

hash = {}
cnt = 0

for line in stdin:
    if line not in hash:
        hash[line] = 1
    else:
        hash[line] += 1
    cnt += 1

hash = list(hash.items())
hash.sort(key=lambda x: x[0])

for item, times in hash:
    print(item, str((times/cnt) * 100))
