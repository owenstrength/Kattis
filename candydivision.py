# o(log n)
n = int(input())
res = []
res2 = []
for i in range(1, int(n**0.5)+1):
    if n % i == 0:
        a = i - 1
        b = n//i - 1
        if a != b:
            res.append(a)
            res2.insert(0, b)
        else:
            res.append(a)
res3 = res + res2
print(" ".join(map(str, res3)))
