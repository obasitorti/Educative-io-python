def buy_and_sell_stock(prices):
    profit = []
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            sub = prices[j] - prices[i]
            profit.append(sub) 
        # return profit
    max_profit = max(profit)
    if max_profit < 0:
        return 0
    else:
        return max_profit

prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
print(buy_and_sell_stock(prices))

