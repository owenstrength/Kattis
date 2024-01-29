from itertools import permutations
x = int(input())
str_x = str(x)

best = 100000000
possibilities = permutations(str_x)
for possibility in possibilities:
    num_p = int(''.join(possibility))
    if num_p > x:
        best = min(num_p, best)
print(best) if best != 100000000 else print(0)
