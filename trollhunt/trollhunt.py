from math import ceil
b,k,g = map(int, input().split())

groups = k // g
b -= 1

print(ceil(b/groups))