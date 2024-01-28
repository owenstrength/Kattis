n = int(input())

res = 1 + (100-n)/n
res2 = 1 + n/(100-n)

print(f'{res:.10f}')
print(f'{res2:.10f}')