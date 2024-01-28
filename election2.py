n = int(input())
P = {}
for _ in range(n):
    s1 = input()
    s2 = input()
    P[s1] = s2

m = int(input())
C = {}
maxCnt = 0
freq = 0
winner = ""
for _ in range(m):
    s1 = input()
    C[s1] = C.get(s1, 0) + 1
    maxCnt = max(maxCnt, C[s1])

for name, k in C.items():
    if k == maxCnt:
        freq += 1
        winner = name

if freq != 1:
    print("tie")
else:
    print(P[winner])