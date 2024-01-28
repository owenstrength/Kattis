times = int(input())
total = 0
for i in range(times):
    q, y = map(float, input().split())
    total += q * y
print(f'{total:.3f}')
