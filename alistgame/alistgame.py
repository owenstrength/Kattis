x = int(input())


factors = []
for i in range(1, x+1):
    if x % i == 0:
        factors.append(i)

print(len(factors) - 1)