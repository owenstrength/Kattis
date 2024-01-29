n,m = map(int, input().split())

groups = list(map(int, input().split()))
index = 0

for i in range(m):
    if groups[index] <= n:
        n -= groups[index]
        index += 1
    else:
        print(m-i)
        break