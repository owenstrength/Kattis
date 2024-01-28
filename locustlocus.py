def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return a * b // gcd(a, b)



k = int(input())
res = 10**9
for _ in range(k):
    y, c1, c2 = map(int, input().split())
    res = min(res, y + lcm(c1, c2))

print(res)