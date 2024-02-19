# best time to buy and sell stock
# array price of stock on day i
# maximize profit (lucro) by choosing a single day to buy one stock and choosing a different day in the future to sell that stock
# return the maximum profit
# if you cannot achieve any profit, return 0
# [7,1,5,3,6,4] => 5
# [7,6,4,3,1] => 0
# [1,2] => 1
# [2,1] => 0
# [2,4,1] => 2

def maxProfit(prices):
    maxProfit = 0
    for i in range(len(prices)): # to find the least price to buy
        for j in range(i+1, len(prices)): # to find the highest price to sell
            profit = prices[j] - prices[i]
            if profit > maxProfit:
                maxProfit = profit
    return maxProfit

# prices = [7,1,5,3,6,4]
# print(maxProfit(prices))

# defining stuff
prices = []
value = ''

# recebe o array de preços
while True:
    value = input().split()
    if value == ['']:
        break
    prices.append(int(value))

print(maxProfit(prices))


