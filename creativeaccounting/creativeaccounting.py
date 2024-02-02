n, l, h = map(int, input().split())

min_profit = float('inf')
max_profit = float('-inf')

days = []
for _ in range(n):
    days.append(int(input()))

prefix = []
prefix.append(days[0])

for i in range(1, len(days)):
    prefix.append(prefix[i-1] + days[i])

def range_sum(i, j):
    if i == 0:
        return prefix[j]
    else:
        return prefix[j] - prefix[i-1]
    
for curr_k in range(l, h+1):
    for delay in range(0, curr_k):
        profit = 0
        if delay != 0:
            first = range_sum(0, delay-1)
            if first > 0:
                profit += 1
        passes = (n - delay) // curr_k


        profits = []
        for i in range(passes):
            profits.append(range_sum(delay + i*curr_k, delay + (i+1)*curr_k - 1))
        
        last_start = passes*curr_k + delay

        if last_start < n:
            profits.append(range_sum(last_start, n-1))

        profit += sum([(1 if p > 0 else 0) for p in profits])
        min_profit = min(min_profit, profit)
        max_profit = max(max_profit, profit)

print(min_profit, max_profit)
        
        
