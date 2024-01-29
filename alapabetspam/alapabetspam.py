[print("\n".join(map(lambda i: str(x.count(i) / len(x)), range(4))))
 for x in [[(0 if c == "_" else (1 if c.islower() else (2 if c.isupper() else 3))) for c in input()]]]
