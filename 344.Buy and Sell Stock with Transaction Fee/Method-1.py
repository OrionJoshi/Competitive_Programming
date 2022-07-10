# Method-1

def maxProfit(prices, fee):
    cash, hold = 0, -prices[0]

    for i in range(1, len(prices)):
        cash = max(cash, hold + prices[i] - fee)
        hold = max(hold, cash - prices[i])

    return cash

# Time Complexity : O(n)
# Space Complexity : O(1)