n = int(input())
res_prev = 1
for _ in range(n):
    a, op, b = input().split()
    a = int(a)
    b = int(b)
    if op == '+':
        res = a + b - res_prev
    elif op == '-':
        res = (a - b) * res_prev
    elif op == '*':
        res = a * a * b * b
    elif op == '/':
        res = a // 2
        if a % 2 == 1:
            res += 1
    print(res)
    res_prev = res
