n, m = map(int, input().split())

if n <= m:
    print("Dr. Chaz will have", m - n, "piece" + ("s" if m - n > 1 else "") + " of chicken left over!")
else:
    print("Dr. Chaz needs", n - m, "more piece" + ("s" if n - m > 1 else "") + " of chicken!")