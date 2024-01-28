n = int(input())
res = 0
n = bin(n)
n = n[2:]
for i in range(len(n)):
    res += 2 ** i * int(n[i])

print(res)
