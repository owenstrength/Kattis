numBricks = int(input())
bricks = map(int, input().split())
prev = 9999999
count = 1
for b in bricks:
    if b > prev:
        count += 1
    prev = b
print(count)