num_of_teas = int(input())
tea_prices = list(map(int, input().split()))
num_of_toppings = int(input())
topping_prices = list(map(int, input().split()))

tea_toppings = {}

for i in range(num_of_teas):
    tea_toppings[i] = list(map(int, input().split()))[1:]

x = int(input())

min_cost = float('inf')

for i in range(num_of_teas):
    for topping_index in tea_toppings[i]:
        topping_price = topping_prices[topping_index - 1] 
        min_cost = min(min_cost, tea_prices[i] + topping_price)

if min_cost == float('inf'):
    print(0)
else:
    print(x // min_cost - 1 if x // min_cost > 1 else 0)