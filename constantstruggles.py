n, k = map(int, input().split())
d,s = map(int, input().split())

total = n * d
total_solved = k * s

unsolved = n - k
res = (total - total_solved) / unsolved

if res < 0 or res > 100:
    print("impossible")
else:
    print(f"{res:.10f}")