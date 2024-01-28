def dist(a, b):
    delta = b - a
    if delta < 0:
        return 0
    if delta & 1:
        return (delta + 1) // 2
    return delta // 2 + 1

s, n = map(int, input().split())
N = list(map(int, input().split()))

res = dist(N[-1] + 2, s + N[0] - 2)
for i in range(1, n):
    res += dist(N[i - 1] + 2, N[i] - 2)

print(res)