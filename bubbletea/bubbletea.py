n = int(input())
teas = list(map(int, input().split()))
m = int(input())
toppings = list(map(int, input().split()))

tea_toppings = []


for _ in range(n):
    tea_toppings.append(list(map(int, input().split()))[1:])

pvh = int(input())

min_cost = float('inf')

for i in range(n):
    for j in range(len(tea_toppings[i])):
        min_cost = min(min_cost, teas[i] + tea_toppings[i][j])

if min_cost == float('inf'):
    print(0)
else:
    print(pvh // min_cost - 1 if pvh // min_cost > 1 else 0)