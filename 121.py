from typing import List

prices = [5,9,1,2]

def maxProfit(prices: List[int]) -> int:
    max_profit = 0
    min_buyprice = prices[0]
    num_days = len(prices)
    for i in range(1, num_days):
        if prices[i] > min_buyprice:
            max_profit = max(max_profit, prices[i] - min_buyprice)
        else:
            min_buyprice = min(min_buyprice, prices[i])
    return max_profit

test = maxProfit(prices)
print(test)