n, p = map(int, input().split())
commercials = list(map(int, input().split()))
for i in range(n):
    commercials[i] -= p

best = -1
current = 0
for i in range(n):
    current += commercials[i]
    if current < 0:
        current = 0
        continue
    best = max(best, current)
print(best)
