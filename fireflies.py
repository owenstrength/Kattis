from sys import stdin

n, h = 0, 0
heights = []

for line in stdin:
    try:
        n, h = map(int, line.split())
    except:
        heights.append(int(line))


heights.sort()
heights.reverse()
count = 0
for i in range(n):
    if h - heights[i] >= 0:
        h -= heights[i]
        count += 1
print(count)
