# pick a triplet of day (i,j,k) such that i < j < k and price[i] < price[j] < price[k] such that profit = price[i] + price[j] + price[k] is maximized
# ex price = [1,5,3,4,6] profit = [2, 3, 4, 5, 6] thus optimal triplet is (3,4,5) with profit = 15

# return tuples of indexs or -1 if max profit is less than or equal to 0
# brute force solution
def getMaximumProfit2(price, profit):
    n = len(price)
    max_profit = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if price[i] < price[j] < price[k]:
                    if profit[i] + profit[j] + profit[k] > max_profit:
                        max_profit = profit[i] + profit[j] + profit[k]

    if max_profit <= 0:
        print(-1)
    else:
        print(max_profit)

# optimized solution
# single pass through the array
# keep track of the maximum profit for each index


def getMaximumProfit(price, profit):
    n = len(price)
    max_profit = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if price[i] < price[j] < price[k]:
                    if profit[i] + profit[j] + profit[k] > max_profit:
                        max_profit = profit[i] + profit[j] + profit[k]

    if max_profit <= 0:
        print(-1)
    else:
        print(max_profit)

    return


getMaximumProfit([1, 5, 3, 4, 6], [2, 3, 4, 5, 6])
